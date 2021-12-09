from odoo import models,api,fields
import logging

_logger = logging.getLogger(__name__)

class PayFee(models.TransientModel):
    _name ="pay.fee.wizard"


    fee = fields.Float(string="Fees")


    def pay_fee(self):
        context = self.env.context
        # _logger.info(f' \n {context} \n ')

        model = context["active_model"]
        id = context["active_id"]
        # _logger.info(f'\n {model} \n')
        # _logger.info(f'\n {id} \n')
        record = self.env[model].browse(id)
        # _logger.info(f'\n {record} \n')
        # record.fee=self.fee
        result=record.write({'fee':self.fee})
        # _logger.info(f'\n {self.fee} \n')

    
          






        
        


        
        
        

    


