{
    'name': 'Custom Report Wizard',
    'version': '1.0',
    'depends': ['base', 'web'],  # Ensure you have the necessary dependencies
    'data': [
        'security/ir.model.access.csv',
        'views/report_hello_wizard_view.xml',
    ],
    'installable': True,
    'application': False,
}
