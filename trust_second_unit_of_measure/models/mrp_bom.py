'''
Created on May 7, 2015

@author: danimar
'''

from openerp import models, api, fields

class mrp_bom(models.Model):
    _inherit = 'mrp.bom'
    
    def _bom_explode(self, cr, uid, bom, product, factor, properties=None, level=0, routing_id=False, previous_products=None, master_bom=None, context=None):
        
        res = super(mrp_bom, self)._bom_explode(cr, uid, bom, product, factor, properties=properties,
                                    level=level, routing_id=routing_id, previous_products=previous_products, 
                                    master_bom=master_bom, context=context)
        results = res[0] # product_lines
        results2 = res[1] # workcenter_lines
        indice = 0
        
        for bom_line_id in bom.bom_line_ids:
            line = results[indice]
            line['largura'] = bom_line_id.largura
            line['comprimento'] = bom_line_id.comprimento
            line['quantidade'] = bom_line_id.quantidade
            indice += 1
        return results, results2

class mrp_bom_line(models.Model):
    _inherit = 'mrp.bom.line'
    
    largura = fields.Integer(string="Largura")
    comprimento = fields.Integer(string="Comprimento")
    quantidade = fields.Integer(string="Quantidade")
    

class mrp_production_product_line(models.Model):
    _inherit = 'mrp.production.product.line'
    
    largura = fields.Integer(string="Largura")
    comprimento = fields.Integer(string="Comprimento")
    quantidade = fields.Integer(string="Quantidade")
    

class mrp_production(models.Model):
    _inherit = 'mrp.production'
    
    def action_compute(self, cr, uid, ids, properties=None, context=None):
        return super(mrp_production,self).action_compute(cr, uid, ids, properties=properties, context=context)
        
        