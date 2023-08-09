# -*- coding: utf-8 -*-
{
    'name': "its_mrp_product_survey_sample",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '11.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'survey'],

    # always loaded
    'data': [
        'data/specification_sheet_sample.xml',
        'data/specification_header_page.xml',
        'data/specification_finished_format_page.xml',
        'data/specification_color_page.xml',
        'data/specification_support_page.xml',
        'data/specification_creation_page.xml',
        'data/specification_shaping_page.xml',
        'data/specification_observation_page.xml',
    ],
}
