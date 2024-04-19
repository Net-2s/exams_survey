# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    question_image = fields.Image('Image', max_width=1024, max_height=1024)
    question_image_filename = fields.Char('Image Filename')

    question_audios = fields.Many2many(
        comodel_name='ir.attachment',
        relation='survey_question_audio_rel',
        column1='question_id',
        column2='attachment_id',
        string='Audios'
    )
