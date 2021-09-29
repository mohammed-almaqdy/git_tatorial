# -*- coding: utf-8 -*-
# from odoo import http


# class Technicals(http.Controller):
#     @http.route('/technicals/technicals/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/technicals/technicals/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('technicals.listing', {
#             'root': '/technicals/technicals',
#             'objects': http.request.env['technicals.technicals'].search([]),
#         })

#     @http.route('/technicals/technicals/objects/<model("technicals.technicals"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('technicals.object', {
#             'object': obj
#         })

    
    # def checkstutas(self,**kw):
    #     mydic ={'new': 'green','approved':'yellow','rejected':'red'}
