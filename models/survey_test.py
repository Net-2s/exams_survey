# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    entry_test = fields.Boolean("Est un Test d'entrée")
    
    @api.onchange('certification')
    def _compute_certification(self):
        for survey in self:
            if survey.certification == True :
                survey.entry_test = False
            
    @api.onchange('entry_test')
    def _compute_is_entry_test(self):
        for reccord in self:
            if(reccord.entry_test == True):
                reccord.certification = False

                reccord.access_mode = "token"
                reccord.is_time_limited = False
                reccord.scoring_type = "scoring_without_answers"
                reccord.questions_layout = "page_per_question"
                reccord.questions_selection = "random"


   
    
