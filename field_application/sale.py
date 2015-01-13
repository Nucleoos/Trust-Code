# -*- coding: utf-8 -*-
import time
from openerp.osv import fields,osv
from openerp.tools.translate import _

# Overloaded sale_order to manage carriers :
class sale_order(osv.osv):
    _inherit = 'sale.order'
    
    _columns = {
            'application': fields.selection([
                                      ('final_customer','final_customer'),
                                      ('resale','Resale'),
                                      ],'Application', readonly=False, select=True, required=True),
                }

    def onchange_partner_id(self, cr, uid, ids, part, context=None):
        
        result = super(sale_order, self).onchange_partner_id(cr, uid, ids, part, context=context)
        
        if not context:
            context = {}

        if not part:
            result['value']['application'] = 'final_customer'
            return result
        
        partner_obj = self.pool.get('res.partner')
        partner_data  = partner_obj.browse(cr, uid, part, context=context).application

        result['value']['application'] = partner_data
        
        return result

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
