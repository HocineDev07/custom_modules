# -*- coding: utf-8 -*-
{
    'name': "dev_hospital",

    'summary': """Hospital management""",

    'description': """
        Hospital management system
    """,

    'author': "Hocine Dev",
    'sequence': -101,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorials',
    'version': '1.0.0',
    'installable': True,
    'application': True,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/dev_hospital_patient_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
