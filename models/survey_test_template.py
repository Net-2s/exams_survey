# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import ast

from odoo import api, models, _


class SurveyTestTemplate(models.Model):

    """This model defines additional actions on the 'survey.survey' model that
       can be used to load a survey sample. The model defines a sample for:
       (1) A feedback form
       (2) A certification
       (3) A live presentation
    """

    _inherit = 'survey.survey'

    @api.model
    def action_load_sample_test_level(self):
        survey_values = {
            'title': _('Test de niveau'),
            'certification': False,
            'access_mode': 'token',
            'is_time_limited': True,
            'time_limit': 60, # 15 minutes
            'is_attempts_limited': True,
            'attempts_limit': 1,
            'progression_mode': 'number',
            'scoring_type': 'scoring_without_answers',
            'users_can_go_back': True,
            'description': ''.join([
                _('Welcome to this level Test. You will receive 2 random questions out of a pool of 3.'),
                '(<span style="font-style: italic">',
                _('Cheating on your neighbors will not help!'),
                '</span> 😁).<br>',
                _('Good luck!')
            ]),
            'description_done': _('Thank you. We will contact you soon.'),
            'questions_layout': 'page_per_section',
            'questions_selection': 'random',
            'question_and_page_ids': [
                (0, 0, { # survey.question
                    'title': _('Odoo Certification'),
                    'is_page': True,
                    'question_type': False,
                    'random_questions_count': 2
                }),
                (0, 0, { # survey.question
                    'title': _('What does "ODOO" stand for?'),
                    'question_type': 'simple_choice',
                    'suggested_answer_ids': [
                        (0, 0, { # survey.question.answer
                            'value': _('It\'s a Belgian word for "Management"')
                        }),
                        (0, 0, { # survey.question.answer
                            'value': _('Object-Directed Open Organization')
                        }),
                        (0, 0, { # survey.question.answer
                            'value': _('Organizational Development for Operation Officers')
                        }),
                        (0, 0, { # survey.question.answer
                            'value': _('It does not mean anything specific'),
                            'is_correct': True,
                            'answer_score': 10
                        }),
                    ]
                }),
                (0, 0, { # survey.question
                    'title': _('On Survey questions, one can define "placeholders". But what are they for?'),
                    'question_type': 'simple_choice',
                    'suggested_answer_ids': [
                        (0, 0, { # survey.question.answer
                            'value': _('They are a default answer, used if the participant skips the question')
                        }),
                        (0, 0, { # survey.question.answer
                            'value': _('It is a small bit of text, displayed to help participants answer'),
                            'is_correct': True,
                            'answer_score': 10
                        }),
                        (0, 0, { # survey.question.answer
                            'value': _('They are technical parameters that guarantees the responsiveness of the page')
                        })
                    ]
                }),
                (0, 0, { # survey.question
                    'title': _('What does one need to get to pass an Odoo Survey?'),
                    'question_type': 'simple_choice',
                    'suggested_answer_ids': [
                        (0, 0, { # survey.question.answer
                            'value': _('It is an option that can be different for each Survey'),
                            'is_correct': True,
                            'answer_score': 10
                        }),
                        (0, 0, { # survey.question.answer
                            'value': _('One needs to get 50% of the total score')
                        }),
                        (0, 0, { # survey.question.answer
                            'value': _('One needs to answer at least half the questions correctly')
                        })
                    ]
                }),
            ]
        }
        mail_template = self.env.ref('survey.mail_template_certification', raise_if_not_found=False)
        if mail_template:
            survey_values.update({
                'certification_mail_template_id': mail_template.id
            })
        return self.env['survey.survey'].create(survey_values).action_show_sample()


    def action_show_sample(self):
        action = self.env['ir.actions.act_window']._for_xml_id('exams_survey.action_survey_test_form')
        action['views'] = [[self.env.ref('exams_survey.survey_test_view_form').id, 'form']]
        action['res_id'] = self.id
        action['context'] = dict(ast.literal_eval(action.get('context', {})),
            create=False
        )
        return action