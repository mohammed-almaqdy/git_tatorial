from odoo import models, fields, api
# first
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
    @api.onchange('status')
    def onchange_status(self):
        if  self.status == 'new':
            self.color=4
        elif self.status == 'approved':
            self.color =3
        elif self.status== 'rejected':
            self.color=10

        # fil = self.env['agenda.status'].search([]).filtered(lambda r:r.name=='f5')
        # print(fil)
        # this is trying
        # fil = self.env['agenda.status'].search([]).sorted(key='age',reverse=True).mapped('age')
        # print(fil)
        # fil1 = self.env['helpdesk.ticket'].search([]).mapped('name')
        # fil = self.env['helpdesk.ticket'].with_context(lang=)
        # print(fil1)
        # print(fil)
        # f
        # ch = self.e
        # ch = self.env['agenda.status'].browse(25)
        # print('hhhhhhhhh',ch)
        # if ch.exists():
        #     print('Exist')
        # else:
        #     print('Not Exist')


        # va = {
        #     'name':'sodu',
        #     'age':44

        # }
        # self.env['agenda.status'].create(va)


        # vals = {'name':'record','age':332}
        # erc_to_update = self.env['agenda.status'].search([('id','=','27')])
        # erc_to_update.write(vals)


        # erc_to_update = self.env['agenda.status'].search([('id','=','37')])
        # erc_to_update.unlink()
   
    def neme_get(self):
        res = []
        for re in self:

            res.append((re.id,'%s-%s'%(re.name,re.age)))

        return res
    
