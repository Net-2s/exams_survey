from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.osv import expression


class RegistrationFolder(models.Model):
    _inherit = 'edof.registration.folder'

    entry_tests = fields.Many2one('survey.user_input',related='crm_id.prospect_test')

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