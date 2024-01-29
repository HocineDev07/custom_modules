# -*- coding: utf-8 -*-
{
    'name': 'Upload Videos',
    'version': '1.0.0',
    'sequence': -125,
    'summary': 'Upload local videos',
    # 'website': 'https://www.hocinedev.com',
    'category': 'Website/eLearning',

    # any module necessary for this one to work correctly
    'depends': ['website_slides',],

    # always loaded
    'data': [
       # 'security/ir.model.access.csv',
        'views/slide_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
