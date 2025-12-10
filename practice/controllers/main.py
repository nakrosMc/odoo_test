from odoo import http
from odoo.http import request

class PracticeController(http.Controller):
    @http.route('/practice/hello', type='http', auth='public', website=True)
    def hello(self, **kwargs):
        return request.render('practice.hello_root_page')