# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public')
    def index(self,**kw):
        return "Hello, World"

class Templatefirst(http.Controller):
    @http.route('/academy/temp/', auth='public')
    def index(self,**kw):
        return http.request.render('my_first_test_module.index')

# class MyFirstTestModule(http.Controller):
#     @http.route('/my_first_test_module/my_first_test_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_first_test_module/my_first_test_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_first_test_module.listing', {
#             'root': '/my_first_test_module/my_first_test_module',
#             'objects': http.request.env['my_first_test_module.my_first_test_module'].search([]),
#         })

@http.route('/my_first_test_module/my_first_test_module/objects/<model("my_first_test_module.my_first_test_module"):obj>/', auth='public')
def object(self, obj, **kw):
    return http.request.render('my_first_test_module.object', {
        'object': obj
    })
