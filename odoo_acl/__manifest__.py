# -*- coding: utf-8 -*-
{
    'name': "Odoo ACL",

    'summary': """
        Demo module to show odoo access controls""",

    'description': """
        This module will cover following.
            > Access Rights on models per group
            > Field level access per group
            > Records level per group
    """,

    'author': "Ajay Chauhan <ajay.chauhan@fictiv.com>",
    'website': "http://www.fictiv.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # UPDATEME remove dependancy of fictiv_digital_model
    'depends': [],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/machine_views.xml',
    ]

}
