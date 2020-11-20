from openerp.osv import orm, fields

class student_mark_main(orm.TransientModel):
    _name = "student.mark.main"
    _inherit = "student.info.student"
    def _square(self, cr, uid, ids, field_name, arg, context=None):
        res={}
        for record in self.browse(cr,uid,ids,context=context):
            b=record.num
            res[record.id] =  b ** 2
            print res
        return res
    
    def _square_root(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr,uid,[id],{'num': value and value ** 0.5},context=context)
    _columns = {
        'aavgg':fields.char("Average Marks", size=15),
        'num':fields.float("Number 1"),
        'smp':fields.function(_square,fnct_inv=_square_root, string="Simple")
    }
        
