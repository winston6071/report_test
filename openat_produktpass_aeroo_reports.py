# -*- encoding: utf-8 -*-

from openerp.osv import osv,fields
from openerp.tools.translate import _

class ir_actions_report_xml(osv.osv):
    _name = 'ir.actions.report.xml'
    _inherit = 'ir.actions.report.xml'

    def _remake_print_button(self, cr, uid, src_id, dest_id):
        ir_values_obj = self.pool.get('ir.values')
        event_id = ir_values_obj.search(cr, uid, \
                [('value','=',"ir.actions.report.xml,%s" % src_id)])
        if event_id:
            ir_values_obj.write(cr, uid, event_id[0], \
                    {'value':"ir.actions.report.xml,%s" % dest_id})
        
        return True

    _columns = {
    }


class product_product(osv.osv):
    _name = 'product.product'
    _inherit = 'product.product'

    def produktpass_print(self, cr, uid, ids, context=None):
        res = super(product_product, self).produktpass_print(cr, uid, ids, context=context)
        res['report_name'] = 'product.produktpass.openat'
        return res
