# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class WeightbridgeRawMaterial(models.Model):
    _name = "weightbridge.raw.material"
    _description = "Raw Material purchase from weightbridge"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    
    name = fields.Char('Ticket Reference', required=True, index='trigram', copy=False, default='New', unique=True)
    start_date = fields.Datetime(string='Start Date', default=fields.Datetime.now, required=True)
    end_date = fields.Datetime(string='End Date', default=fields.Datetime.now, required=True)
    provenance = fields.Char(string='Provenance', required=True)
    car_name = fields.Char(string='Car Name', required=True)
    driver_name = fields.Char(string='Driver Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Farmer', required=True, change_default=True, tracking=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", help="You can find a vendor by its Name, TIN, Email or Internal Reference.")
    entry_weight = fields.Float(string='Entry Weight', required=True)
    output_weight = fields.Float(string='Output Weight', required=True)
    net_weight = fields.Float(string='Net Weight', required=True)
    created_by = fields.Char(string='Created By', required=True)
    authorized_by = fields.Many2one('res.users', string='Authorized By', states={'to_paid': [('required', True)], 'confirmed': [('required', False)]})
    date_authorized = fields.Datetime(string='Date Authorized', states={'to_paid': [('readonly', True)], 'confirmed': [('readonly', True)]})
    paid_by = fields.Many2one('res.users', string='Paid By', states={'to_paid': [('required', False)], 'paid': [('required', True)], 'confirmed': [('required', False)]})
    date_paid = fields.Datetime(string='Date Paid', states={'to_paid': [('readonly', True)], 'paid': [('readonly', True)], 'confirmed': [('readonly', False)]})
    state = fields.Selection([('confirmed', 'Confirmed'),  ('to_paid', 'Paid request'), ('paid', 'Paid'), ('cancel', 'Cancel'),], string='Status', required=True, default='confirmed')
    channel_ids = fields.Many2many('raw.material.channel', 'himaf_raw_material_channel_rel', 'raw_material_id', 'channel_id', string='Channels')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company.id)
    
    
    def action_confirm(self):
        """ Confirm the given quotation(s) and set their confirmation date.

        If the corresponding setting is enabled, also locks the Sale Order.

        :return: True
        :rtype: bool
        :raise: UserError if trying to confirm locked or cancelled SO's
        """
        date_authorized = fields.Datetime.now()
        user = self.env.user
        self.write({'state': 'to_paid',
                    'date_authorized': date_authorized,
                    'authorized_by': user.id
                    })
        
    def action_unconfirm(self):
        self.write({'state': 'confirmed',
                    'date_authorized': None,
                    'authorized_by': None
                    })
        
        
    def action_paid(self):
        
        #TODO: ajouter le mode de paiement
        date_paid = fields.Datetime.now()
        user = self.env.user
        
        self.write({'state': 'paid',
                    'date_paid': date_paid,
                    'paid_by': user.id
                    })
                    

        