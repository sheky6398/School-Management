from typing import DefaultDict
from odoo.exceptions import ValidationError
from odoo import models
from odoo import fields
from odoo import api
from datetime import date, datetime
import logging

_logger = logging.getLogger(__name__)


class Student(models.Model):
    _name="school.student"
    _description="school student"
    # _rec_name="student_name"

    name=fields.Char(string="Student Name",required=True)
    roll_no=fields.Char(string="Roll no",required=True, size=6)
    registration_no=fields.Char( string="Registration No", size=6)
    course_ids=fields.Many2many('school.course', string="Courses",
                                help="Courses in which student to be enrolled")
    batch=fields.Char(string="Batch")
    phone_no=fields.Char(string="Phone number",size=10, readonly=True)
    father_name=fields.Char()
    age=fields.Integer(string="Age",compute="compute_age", store= True)
    date_dob=fields.Date(string="Date of Birth",required=True)
    state=fields.Selection([('draft','Draft'), ('pending','Pending'), 
                            ('enrolled','Enrolled'), ('rejected','Rejected')],
                            default='draft',string="Status")
    gender=fields.Selection([('male','Male'), ('female','Female')],
                            string="Gender",default="male")
    image=fields.Binary(string="Student Image")
    teacher_ids=fields.One2many('school.teacher','student_id',string="Teacher's id")
    email_address = fields.Char(string="Email Address")
    fee = fields.Float(string='Fee')
    amount_paid = fields.Float(string='Amount Paid',compute="compute_amount_paid")
    due_fee = fields.Integer(compute="compute_due_fee")
    total_fee = fields.Integer()
    date_joining = fields.Datetime(string="Admission Time")
    choose_state = fields.Many2one('res.country.state',string="State")

    teeacher_id=fields.Many2one('school.teacher', string = "Teacher's Name")
    
    
    


    @api.depends('date_dob') 
    def compute_age(self):
        _logger.info("\n Age is being calculated")
        today_date=date.today()
        for student_ in self:
            if student_.date_dob:
                date_dob=fields.Datetime.to_datetime(student_.date_dob).date()
                total_age=str(int((today_date-date_dob).days/365))
                student_.age=total_age

    
    
    @api.depends('fee')
    def compute_due_fee(self):
        self.due_fee=self.total_fee-self.amount_paid

    @api.depends('fee')
    def compute_amount_paid(self):
        self.amount_paid=self.fee


    


    @api.onchange('name')   #student_name
    def _onchange_name(self):#student_name
        if self.name:
            self.email_address=self.name.replace(" ",'')+"@gmail.com"   
   

    @api.constrains('name','father_name')    #stduent_name
    def _check_name(self):
        _logger.info("\n I am informing Student Name and Father Name")
        _logger.warning("\n I am Warning Student Name and Father Name")
        _logger.critical("\n I am Critical Student Name and Father Name")
        _logger.error("\n I am Error Student Name and Father Name")
        _logger.debug("\n I am Debugging Student Name and Father Name")
        for record in self:
            if record.name==record.father_name:    #stduent_name
                raise ValidationError("It is Not possible to have Father's name and Son name  are same")


    @api.constrains('phone_no')
    def _check_phone_no(self):
        for record in self:
            if len(record.phone_no)<10:
                raise ValidationError("Phone Numer Must be 10 digits")  
                _logger.info("\n Phone number must be 10")   

    @api.constrains('date_dob')  
    def _check_date_dob(self):
        for record in self:
            if record.date_dob > date.today():
                raise ValidationError("It is not possible ") 

    def check_method(self):
        _logger.info(f"\n self = {self} \n ") 
        _logger.info(f"\n name = {self.name} \n ")
        _logger.info(f"\n age = {self.age} \n ")
        _logger.info(f"\n self.gender = {self.gender} \n ")
        self.state='draft'
        
        

    def father(self):
        _logger.info(f' \n context = {self.env.context} \n ')
        if self.env.context.get("developer",'') == "Bharat":
            _logger.info(f' \n  "Welcome Bharat" \n ')
        else:
            _logger.info(f' \n  "We Have No developer" \n ')
        
    




    def enroll_method(self):
        _logger.info(f'\n self = {self} \n')
        _logger.info(f'\n name = {self.name} \n')
        self.state='enrolled'

    def rejected_method(self):
        self.state='rejected'

    # def just_method(self)
        # _logger.info(f"\n env = {self.env} \n")
        # _logger.info(f"\n context = {self.env.context} \n")
        #create = create
        #read = read
        #update = write
        #delete = unlink
        # values = self.read()
        # _logger.info(f' \n values={values} \n')
        # rec1 = self.env['school.student'].create([{'name':"Tarun Saran","roll_no":"1245212","phone_no":"1485265842","date_dob":"2021-05-11"}])
        # _logger.info(f' \n rec1 = {rec1} \n')
        # result = self.write({'batch':'2000','registration_no':'145785215'})
        # _logger.info(f' \n result = {result} \n')
        # self.unlink()
        # courses=self.env['school.course'].search(['|',('course_fee','>',10000),('name','=','Python')])
        # # _logger.info(f' \n courses = {courses.sorted(key = lambda o:o.duration)} \n ')
        # _logger.info(f' \n courses = {courses.mapped("name")} \n ')
        # # _logger.info(f' \n courses = {courses.mapped("joining_date")} \n ')
        # courses=self.env['school.course'].search_count([('course_fee','<',10000)])
        # _logger.info(f' \n courses = {courses} \n ')

        #odoo browse method
        # browsed= self.env['school.teacher'].browse([14,1])
        # exists method
        # if browsed.exists():
        #     _logger.info(f' \n browsed = {browsed} \n ')
        # else:
        #     _logger.info(f' \n browsed = {browsed} not found  \n ')

        #copy method
        # browsed= self.env['school.teacher'].browse(1)
        # browsed.copy()


    # filtered Method
    # def just_method(self):
    #     filter=self.env['school.student'].search([]).filtered(lambda s:s.batch > '2015')
    #     _logger.info(f' \n filter = {filter.mapped("name")} \n ')


    # Sorted Method
    # def just_method(self):
    #      filter=self.env['school.student'].search([]).sorted(key="age")
    #      _logger.info(f' \n filter = {filter.mapped("name")} \n ')

    # # With_context
    def just_method(self):
        self.father()
        self.with_context(developer = "Bharat").father()

        

        #   filter=self.env['school.student'].with_context(lang='ar_SY').search([]).mapped("name")
        #   _logger.info(f' \n filter = {filter} \n ')








    
 











        


        
      



        






        

    
    
    
    
    
    





