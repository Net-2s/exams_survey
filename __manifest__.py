# -*- coding: utf-8 -*-
{
    'name': "Exams Survey",

    'summary': """This module help embark a sample survey into the survey model""",

    'description': """
        It can also be use to embark several survey which could be use
    """,

    'author': "SIMO Larissa",
    'website': "http://www.its-nh.com",
    'category': 'survey',
    'version': '16.1.0.0',
    'application': True,

    # odoo dependencies
    'depends': ['base', 'survey', 'polyx_lead'],

    # setting data files
    'data': [
        'views/menu.xml',
        'views/survey_question.xml',
        'views/survey_survey_views.xml',
        'views/survey_template.xml',
        'views/survey_test_template_view.xml',
        'views/crm_lead_form_view.xml',
        'views/dossier_view.xml',
        'views/registration_folder_view.xml',
        'views/survey_user_view.xml',
        'data/specification_survey_sheet.xml',
        'data/section_one.xml',
        'data/section_two.xml',
        'data/section_three.xml',
        'data/section_four.xml',
        'data/section_five.xml',
        'data/personal_infos.xml',
    ],
    "assets": {
        "web.assets_frontend": {
            "exams_survey/static/css/style.css",
        }
    },
}
