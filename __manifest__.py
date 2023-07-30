# Copyright 2010-2014 Savoir-faire Linux (<http://www.savoirfairelinux.com>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "WeightBridge",
    "version": "16.0.1.0.1",
    "author": "2DAY GROUP",
    "maintainer": "2DAY GROUP",
    "website": "2daygroup.net",
    "license": "AGPL-3",
    "category": "Inventory/Purchase",
    "summary": "Receive and deliver products from the weight bridge",
    "depends": ["purchase", "stock"],
    "data": [
        'views/weightbridge_views.xml',
        # 'views/farmer_views.xml',
        'security/ir.model.access.csv'
        ],
    "installable": True,
    
}
