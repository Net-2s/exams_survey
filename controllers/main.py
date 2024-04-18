
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging
import werkzeug

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import fields, http, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.http import request, content_disposition
from odoo.osv import expression
from odoo.tools import format_datetime, format_date, is_html_empty
from odoo.addons.base.models.ir_qweb import keep_query


class Survey(http.Controller):


    @http.route('/survey/get_title_question_image/<string:survey_token>/<string:answer_token>/<int:question_id>', type='http', auth="public", website=True, sitemap=False)
    def survey_get_title_question_image(self, survey_token, answer_token, question_id):
        access_data = self._get_access_data(survey_token, answer_token, ensure_token=True)
        if access_data['validity_code'] is not True:
            return werkzeug.exceptions.Forbidden()

        survey_sudo, answer_sudo = access_data['survey_sudo'], access_data['answer_sudo']

        if int(question_id) in survey_sudo.question_ids.ids:
            question = request.env['survey.question'].sudo().search([
                ('id', '=', int(question_id)),
            ])

        if not question:
            return werkzeug.exceptions.NotFound()

        return request.env['ir.binary']._get_image_stream_from(
            question, 'question_image'
        ).get_response()

