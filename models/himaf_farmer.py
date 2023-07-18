# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class HimafFarmer(models.Model):
    _name = "himaf.farmer"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Name', required=True)
    ref = fields.Char(string='Reference', index=True)
    mobile = fields.Char(unaccent=False)
    channel_ids = fields.Many2many('himaf.farmer.channel', 'himaf_farmer_channel_rel', 'farmer_id', 'channel_id', string='Channels')
    
    