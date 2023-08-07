# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class its_mrp_product_survey_sample(models.Model):
#     _name = 'its_mrp_product_survey_sample.its_mrp_product_survey_sample'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100