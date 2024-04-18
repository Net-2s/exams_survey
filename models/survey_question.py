# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    question_image = fields.Image('Image', max_width=1024, max_height=1024)
    question_audio = fields.Binary(string='Audio')
    question_image_filename = fields.Char('Image Filename')
    question_audio_filename = fields.Char('Audio Filename')
