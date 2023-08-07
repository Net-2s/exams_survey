# -*- coding: utf-8 -*-
from odoo import http

# class ItsMrpProductSurveySample(http.Controller):
#     @http.route('/its_mrp_product_survey_sample/its_mrp_product_survey_sample/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/its_mrp_product_survey_sample/its_mrp_product_survey_sample/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('its_mrp_product_survey_sample.listing', {
#             'root': '/its_mrp_product_survey_sample/its_mrp_product_survey_sample',
#             'objects': http.request.env['its_mrp_product_survey_sample.its_mrp_product_survey_sample'].search([]),
#         })

#     @http.route('/its_mrp_product_survey_sample/its_mrp_product_survey_sample/objects/<model("its_mrp_product_survey_sample.its_mrp_product_survey_sample"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('its_mrp_product_survey_sample.object', {
#             'object': obj
#         })