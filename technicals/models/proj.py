from odoo import models, fields, api

class Proj(models.Model):
    _name = 'proj'

    agenda_status = fields.Many2one(
        'agenda.status',
        'Agenda status'
    )
    
    # def default_get(self, fields):
    #     res = super(Proj,self).default_get(fields)
    #     res['agenda_status']=1

    #     return res