# -*- coding: utf-8 -*-

{
    'name': "Survey Image",
    'summary': """Disable zooming image in surveys""",
    'description': """
        Disable zooming image in surveys
    """,
    'author': "Hocine Dev",
    # 'website': "https://www.HocineDev.com",
    'sequence': 100,
    'license': 'AGPL-3',
    'category': 'Marketing/Surveys',
    'version': '1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['survey'],
    # always loaded
    'data': [
        'views/survey_image_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}


