# -*- coding: utf-8 -*-
# © 2011-2015 Sylvain Garancher <sylvain.garancher@syleam.fr>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class StockPickingWave(models.Model):
    _inherit = 'stock.picking.wave'

    @property
    @api.multi
    def move_lines(self):
        return self.mapped('picking_ids.move_lines')

    @property
    @api.multi
    def pack_operation_ids(self):
        return self.mapped('picking_ids.pack_operation_ids')

    @api.multi
    def do_transfer(self):
        return self.picking_ids.do_transfer()
