from odoo import models, fields, api

class AgendaStatus(models.Model):
    _name = 'agenda.status'

    name = fields.Char(
        String='Description'
    )
    age = fields.Integer()
    status =  fields.Selection( string='Status', selection=[
        ('new', 'New'),
        ('approved','Approved'),
        ('rejected', 'Rejected')
    ])
    partner_name = fields.Many2one('res.partner',string='Customer')
    country_id = fields.Many2one('res.country',related='partner_name.country_id', store=True)
    state_id =fields.Many2one('res.country.state',related='partner_name.state_id', store=True)
    color = fields.Integer(
        string="Color",
        help="Choose your color",
        
    )
    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    # pri = fields.Integer(string='priyorty',default=2)
    sign = fields.Binary('signiture')
    priority = fields.Selection([('0','Low'), ('1','Normal'), ('2','High'),('3','very hight')], 'Priority',default=0)
    # hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    @api.onchange('status')
    def onchange_status(self):
        if  self.status == 'new':
            self.color=4
        elif self.status == 'approved':
            self.color =3
        elif self.status== 'rejected':
            self.color=10
       