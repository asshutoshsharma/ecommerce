# -*- coding: utf-8 -*-
{
    'name': "Ecommerce Order Management",
    'sequence': 2,
    'author': "Ashutosh Sharma",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/order_list.xml',
    ],
}