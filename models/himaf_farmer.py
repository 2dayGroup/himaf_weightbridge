# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class HimafFarmer(models.Model):
    _name = "himaf.farmer"
    _inherit = 'res.partner'
    
    channel_ids = fields.Many2many('farmer.channel', 'himaf_farmer_channel_rel', 'farmer_id', 'channel_id', string='Channels')
    