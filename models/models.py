from odoo import api, models, fields


class CarRequest(models.Model):
    _name = 'car.request' # This will create a Table in DB => as a name --->> 'car_request' 
    _inherit = ['mail.thread']
    _description = 'Car Request'
    
    STATE = [
        ('d','Draft'),
        ('c','Confirm'),
        ('v','Validated'),
        ('r','Refuse'),
        ('a','Approved'),
        
    ]
    
    name = fields.Char(string='Request', required=True, )
    date_from = fields.Datetime(string='Start Date', required=False, default= fields.Datetime.now(),)
    date_to = fields.Datetime(string='End Date', required=False, default = fields.Datetime.today(),)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee' ,required=True, )
    car_id = fields.Many2one(comodel_name='fleet.vehicle',string='Car' , required=True,)
    state = fields.Selection(string='Status', selection=STATE, required=True, default='d', track_visibility='onchange', )
    
    
    @api.multi
    def confirm_request(self):
        self.state = 'c'
    
    @api.multi
    def validate_request(self):
        self.state = 'v'
    
    @api.multi
    def refuse_request(self):
        self.state = 'r'
    
    @api.multi
    def approve_request(self):
        self.state = 'a'
        
    
    
