from odoo import models
from odoo import fields,api

class Teacher(models.Model):
    _name="school.teacher"
    _description="school teacher"
    # _rec_name="teacher_name"

    name=fields.Char(string="Teacher Name",required=True)
    courses_count=fields.Integer(string="Courses Count",compute="compute_count")
    course_ids=fields.Many2many('school.course', string="Courses")
    subject_name=fields.Char(string="Subject Name",required=True)
    designation=fields.Char(string="Designation")
    fee=fields.Integer(string="Salary")
    joining_date=fields.Date(string="Joining Date")
    image=fields.Binary(string="Teacher Image")
    student_id=fields.Many2one('school.student', string="Student's id")
    student_batch = fields.Char(related='student_id.batch', store=True)
    student_line_ids = fields.One2many('school.student','teeacher_id',string="STUDENT")

    @api.depends('course_ids')
    def compute_count(self):
        for rec in self:
            rec.courses_count=len(rec.course_ids)


    def action_create(self):
        self.create([{'name':"Anurag Singh",'subject_name':'Bcom','fee':20000}])
    

    def action_write(self):
        self.update({'name':"Virender sharma",'subject_name':'BSC','fee':10000})

    def action_delete(self):
        self.unlink()
















