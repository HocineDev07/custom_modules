# -*- coding: utf-8 -*-
{
    'name': "odoo_inheritance",
    'summary': """odoo odoo_inheritance summery""",
    'sequence': -101,
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['om_hospital'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hospital_patient_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
