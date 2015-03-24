# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2015 TrustCode - www.trustcode.com.br                         #
#                                                                             #
#This program is free software: you can redistribute it and/or modify         #
#it under the terms of the GNU Affero General Public License as published by  #
#the Free Software Foundation, either version 3 of the License, or            #
#(at your option) any later version.                                          #
#                                                                             #
#This program is distributed in the hope that it will be useful,              #
#but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#GNU General Public License for more details.                                 #
#                                                                             #
#You should have received a copy of the GNU General Public License            #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
###############################################################################

from openerp import models, api, fields
import decimal_precision as dp

class Product(models.Model):
    _inherit = 'product.product'
    
    standard_price = fields.Float(digits=dp.get_precision('Product Price'), 
                              help="Cost price of the product template used for standard stock valuation in accounting and used as a base price on purchase orders. "
                                   "Expressed in the default unit of measure of the product.",
                              groups="base.group_user", string="Cost Price",
                              inverse='_set_standard_price')

    
    @api.one
    @api.depends('standard_price')
    def _set_standard_price(self):
        ''' Store the standard price change in order to be able to retrieve the cost of a product template for a given date'''        
        price_history_obj = self.pool['product.price.history']
        user_company = self.pool.get('res.users').browse(cr, uid, uid, context=context).company_id.id
        company_id = context.get('force_company', user_company)
        price_history_obj.create(cr, uid, {
            'product_template_id': product_tmpl_id,
            'cost': value,
            'company_id': company_id,
        }, context=context)

    
    
    
    