from odoo import api, models, fields


class CarRequest(models.Model):
    _name = 'car.request' # This will create a Table in DB => as a name --->> 'car_request' 
    _description = 'Car Request'
    
    name = fields.Char(string='Request', required=True, )
    date_from = fields.Datetime(string='Start Date', required=False, default= fields.Datetime.now(),)
    date_to = fields.Datetime(string='End Date', required=False, default = fields.Datetime.today(),)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee' ,required=True, )
    car_id = fields.Many2one(comodel_name='fleet.vehicle',string='Car' , required=True,) 
    
