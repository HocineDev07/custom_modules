# -*- coding: utf-8 -*-
{
    'name': "product_image_zoom",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product',
                'web_tour',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/image_zoom_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            ('include', "web.chartjs_lib"),
            'product_image_zoom/static/src/scss/image_zoom_style.scss',
            'product_image_zoom/static/src/js/image-zoom.js',
            #'product_image_zoom/static/src/js/survey_image_zoomer.js',
        ],
    },
}
