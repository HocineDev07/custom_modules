# -*- coding: utf-8 -*-
{
    'name': "Ui Executing Code",
    'sequence': -120,
    'category': "Coding",
    'summary': """
        User interface for executing code""",
    'description': """
        User interface for executing ORM & SQL expressions
    """,
    'license': "AGPL-3",
    'author': "Hocine Dev",
    'version': "1.0.0",
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/orm_execution_view.xml',
        'views/sql_execution_view.xml',
        'views/sql_execution_result_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ui_execution_code/static/src/css/custom_styles.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
