# -*- coding: utf-8 -*-
{
    'name': "ITS Survey Sample",

    'summary': """This module help embark a sample survey into the survey model""",

    'description': """
        It can also be use to embark several survey which could be use
    """,

    'author': "IT Service, Simo Larissa",
    'website': "http://www.its-nh.com",
    'category': 'survey',
    'version': '11.1.0.0',

    # odoo dependencies
    'depends': ['base', 'survey'],

    # setting data files
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
