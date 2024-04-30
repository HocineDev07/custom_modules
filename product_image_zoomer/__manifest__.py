# -*- coding: utf-8 -*-
{
    'name': "product_image_zoomer",

    'summary': "Product Image Zoomer",

    'description': """
    Product Image Zoomer
    """,

    # 'author': "My Company",
    # 'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'views/image_zoom_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'product_image_zoomer/static/src/scss/image_zoomer_style.scss',
            # 'product_image_zoomer/static/src/js/image_zoomer.js',
            # 'product_image_zoomer/static/src/xml/image_zoomer_templates.xml',
        ],
    },
}
