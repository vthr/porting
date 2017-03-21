# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    fal_action_counter = fields.Integer(string='Action', readonly="1")

# end of sale_order()
