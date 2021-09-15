from odoo import models
from odoo import fields

class Course(models.Model):
    _name="school.course"
    _description="school course"
    # _rec_name="course"

    
    name=fields.Char(string="Course Name",required=True)
    tutor_id=fields.Many2one('school.teacher', string="Teacher Name")
    joining_date=fields.Date(string="Joining Date")
    image=fields.Binary(string="Student Image")
    duration=fields.Selection([('3_months',"3 Months"), ('6_months',"6 Months"), 
                               ('12_months',"12 Months"), ('24_months',"24 Months")]
                                 ,string="Course Duration",default="3 months")
    course_fee=fields.Integer(string="Course Fee")
    timing = fields.Selection([('morning','Morning'),('afternoon','Afternoon'),('evening','Evening')], string="Batch Timing", default="morning")
    
    