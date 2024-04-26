from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Dossier(models.Model):
    _inherit = 'gestion.formation.dossier'

    entry_tests = fields.Many2one('survey.user_input')

    @api.model
    def create(self, vals):
        folders = super().create(vals)

        for folder in folders:
            crm_lead = self.env['crm.lead'].sudo().search([
                '|',
                    ('folder_number','=',folder.number),
                    ('phone','=',folder.phone),
            ], limit=1)
            if crm_lead and crm_lead.prospect_test:
                folder.sudo().write({
                    'entry_tests': crm_lead.prospect_test
                })
                
        return folders

    def open_test_result(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': "Test d'entrée",
            'res_model': 'survey.user_input',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': self.entry_tests.id,
        }