# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
from odoo.addons import decimal_precision as dp
from lxml import etree

import logging


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('general_discount')
    def onchange_general_discount(self):
        logging.info("*********modulo***************")
        self.mapped('order_line').update({
            'discount3': self.general_discount,
        })