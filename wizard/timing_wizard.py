from odoo import models,api,fields
import logging

_logger = logging.Logger(__name__)


class Timing(models.TransientModel):
    _name = "timing.wizard"
    _description = "Check the timing"


    timing = fields.Selection([('morning','Morning'), ('afternoon','Afternoon'), 
                            ('evening','Evening')], string="Timing", default="morning")


    def check_timing(self):
        context=self.env.context
        # _logger.info(f'\n {context} \n ')
        
        model = context["active_model"]
        id = context["active_id"]
        record = self.env[model].browse(id)
        # record.write({'timing':self.timing})
        record.timing=self.timing

        
     
       




  

