# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    entry_test = fields.Boolean(string="Est un test d'entré")

    @api.onchange('entry_test')
    def on_entry_test_change(self):
        for survey in self:
            if survey.entry_test == True:
                survey.certification = False
                survey.is_time_limited = False
                survey.access_mode = 'token'
                survey.scoring_type = 'scoring_without_answers'
                survey.questions_layout = 'page_per_question'

    @api.onchange('certification')
    def on_certification_change(self):
        for survey in self:
            if survey.entry_test == True:
                survey.certification = False

    