{
    'name': 'Custom Report Wizard',
    'version': '1.0',
    'depends': ['base', 'sale', 'web'],  # Ensure you have the necessary dependencies
    'data': [
        'security/ir.model.access.csv',
        'wizard/print_wizard_view.xml',
        'views/sale_order_wizard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_wizard/static/src/js/report_intercept.js',
        ],
    },
    'installable': True,
    'application': False,
}
