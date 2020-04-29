# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    machine_ids = fields.One2many('machine', 'vendor_id')
    total_machine_value = fields.Float(
        compute='calculate_machine_value', store=True)

    @api.depends('machine_ids', 'machine_ids.cost')
    def calculate_machine_value(self):
        for partner in self:
            partner.total_machine_value = sum(
                partner.machine_ids.mapped('cost'))
