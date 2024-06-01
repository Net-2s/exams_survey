from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.addons.base.models.ir_qweb import keep_query


import logging

_logger = logging.getLogger(__name__)


class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'
    _description = 'CRM Lead Inherit'

    exam_to_pass = fields.Many2one(
        'survey.survey',
        "Examen d'entrée",
        domain=[('entry_test','=',True)])
    
    prospect_test = fields.Many2one('survey.user_input')
    recommanded_hours = fields.Float(
        "Nombre d'heures recommandé",
        related='prospect_test.recommended_hours'
    )
    entry_test_score = fields.Float(
        "Score au test d'entrée",
        related='prospect_test.scoring_total'
        )

    
    
    def launch_folder_test(self):
        self.ensure_one()
        if not self.exam_to_pass:
            raise models.ValidationError("Aucune Examen d'entrée n'a été selectionné")
        if not  self.prospect_test:
            self.prospect_test = self.exam_to_pass.sudo()._create_answer(user=self.env.user, test_entry=True)

        return {
            'type': 'ir.actions.act_url',
            'name': "Test Survey",
            'target': 'self',
            'url': '/survey/start/%s?%s' % (self.exam_to_pass.access_token, keep_query('*', answer_token=self.prospect_test.access_token)),
        }
    
    def open_test_result(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': "Test d'entrée",
            'res_model': 'survey.user_input',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': self.prospect_test.id,
        }
