# -*- coding: utf-8 -*-
{
    'name' : 'Practice Leon',
    'version' : '1.0',
    'summary': 'Leon praticas',
    'description': """ Modulo de praticas Leon   """,
    'category': 'Practice',
    'depends': ['website','web', 'base', 'portal'],
    'data': [
        'views/template.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_frontend': [
            'practice/static/src/components/hello-world/root.xml',
            'practice/static/src/components/hello-world/app.js',
        ],
    },
    'license': 'LGPL-3',
}