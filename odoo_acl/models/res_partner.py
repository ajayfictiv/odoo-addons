# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    machine_ids = fields.One2many('machine', 'vendor_id')