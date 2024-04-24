# -*- coding: utf-8 -*-

from odoo import models, fields, api

RESULT_BORNE = [
    {'borne': 5/26, 'heures': 60 },
    {'borne': 10/26, 'heures': 40 },
    {'borne': 15/26, 'heures': 30 },
    {'borne': 20/26, 'heures': 20 },
    {'borne': 24/26, 'heures': 10 },
    {'borne': 26/26, 'heures': 4 },
]

class SurveySurvey(models.Model):
    _inherit = 'survey.user_input'

    lead_ids = fields.One2many(
        comodel_name='crm.lead',
        string="Participants",
        inverse_name="prospect_test"
    )
    
    recommended_hours =  fields.Float(
        string="Nombre d'heures recommandé:",
        default=0,
        compute="_compute_recommended_hours",
        store=True,
        readonly=False,
    )
    
    api.depends('scoring_total')
    def _compute_recommended_hours(self):
        for rec in self:
            for resl in RESULT_BORNE:
                if rec.scoring_percentage/100 <= resl['borne']:
                    rec.recommended_hours = resl['heures']
                    return rec.recommended_hours


class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input.line'

    @api.model
    def _get_answer_score_values(self, vals, compute_speed_score=True):
        """ Get values for: answer_is_correct and associated answer_score.

        Requires vals to contain 'answer_type', 'question_id', and 'user_input_id'.
        Depending on 'answer_type' additional value of 'suggested_answer_id' may also be
        required.

        Calculates whether an answer_is_correct and its score based on 'answer_type' and
        corresponding question. Handles choice (answer_type == 'suggestion') questions
        separately from other question types. Each selected choice answer is handled as an
        individual answer.

        If score depends on the speed of the answer, it is adjusted as follows:
         - If the user answers in less than 2 seconds, they receive 100% of the possible points.
         - If user answers after that, they receive 50% of the possible points + the remaining
            50% scaled by the time limit and time taken to answer [i.e. a minimum of 50% of the
            possible points is given to all correct answers]

        Example of returned values:
            * {'answer_is_correct': False, 'answer_score': 0} (default)
            * {'answer_is_correct': True, 'answer_score': 2.0}
        """
        user_input_id = vals.get('user_input_id')
        answer_type = vals.get('answer_type')
        question_id = vals.get('question_id')
        if not question_id:
            raise ValueError(_('Computing score requires a question in arguments.'))
        question = self.env['survey.question'].browse(int(question_id))

        # default and non-scored questions
        answer_is_correct = False
        answer_score = 0

        # record selected suggested choice answer_score (can be: pos, neg, or 0)
        if question.question_type in ['simple_choice', 'multiple_choice']:
            if answer_type == 'suggestion':
                suggested_answer_id = vals.get('suggested_answer_id')
                if suggested_answer_id:
                    question_answer = self.env['survey.question.answer'].browse(int(suggested_answer_id))
                    answer_score = question_answer.answer_score
                    answer_is_correct = question_answer.is_correct
        # for all other scored question cases, record question answer_score (can be: pos or 0)
        elif question.question_type in ['date', 'datetime', 'numerical_box']:
            answer = vals.get('value_%s' % answer_type)
            if answer_type == 'numerical_box':
                answer = float(answer)
            elif answer_type == 'date':
                answer = fields.Date.from_string(answer)
            elif answer_type == 'datetime':
                answer = fields.Datetime.from_string(answer)
            if answer and answer == question['answer_%s' % answer_type]:
                answer_is_correct = True
                answer_score = question.answer_score

        # Chages
        elif question.question_type in ['text_box', 'char_box'] and question.is_recopy_execise:
            answer = vals.get('value_%s' % answer_type)
            answer_traitee = answer.strip().lower()
            
            rep_traitee = question.copy_text.strip().lower()
            if answer_traitee == rep_traitee:
                answer_is_correct = True
                answer_score = question.answer_score

        # end Change

        if compute_speed_score and answer_score > 0:
            user_input = self.env['survey.user_input'].browse(user_input_id)
            session_speed_rating = user_input.exists() and user_input.is_session_answer and user_input.survey_id.session_speed_rating
            if session_speed_rating:
                max_score_delay = 2
                time_limit = question.time_limit
                now = fields.Datetime.now()
                seconds_to_answer = (now - user_input.survey_id.session_question_start_time).total_seconds()
                question_remaining_time = time_limit - seconds_to_answer
                # if answered within the max_score_delay => leave score as is
                if question_remaining_time < 0:  # if no time left
                    answer_score /= 2
                elif seconds_to_answer > max_score_delay:
                    time_limit -= max_score_delay  # we remove the max_score_delay to have all possible values
                    score_proportion = (time_limit - seconds_to_answer) / time_limit
                    answer_score = (answer_score / 2) * (1 + score_proportion)

        return {
            'answer_is_correct': answer_is_correct,
            'answer_score': answer_score
        }
