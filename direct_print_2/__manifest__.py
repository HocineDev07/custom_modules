{
    'name': 'Direct Print 2',
    'version': '17.0.1.0.0',
    'summary': 'Open reports in a wizard instead of downloading',
    'description': 'This module allows users to open reports in a wizard with a binary field named "pdf_view" instead of downloading them.',
    'author': 'Your Name',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/direct_print_wizard_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'direct_print_2/static/src/js/direct_print.js',
        ],
    },
    'installable': True,
    'application': False,
}
