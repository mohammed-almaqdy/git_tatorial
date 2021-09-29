from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    # agenda_status = fields.Many2one(
    #     'agenda.status',
    #     'Agenda status'
    # )
     # hex_value = fields.Char(
    #     string="Hex Value",
    #     related="agenda_status",
    #     store=False,
    #     size=7
    # )