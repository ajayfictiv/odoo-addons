# -*- coding: utf-8 -*-

from odoo import models, fields


class Machine(models.Model):
    _name = 'machine'

    name = fields.Char(required=True)
    vendor_id = fields.Many2one(
        'res.partner', string="Vendor", domain=[('supplier', '=', True)],
        required=True)
    note = fields.Text()
    cost = fields.Float()
