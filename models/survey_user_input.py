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


