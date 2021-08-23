# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
       Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            -training Courses
            -training sessions 
            -attendees registration
    """,

    'author': "Abdo Mostafa",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        #'views/session_board.xml',   #error in file  C:\custome_module\Openacademy\open_academy\views\session_board.xml
        'reports/session_report.xml',
        'views/partner.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
