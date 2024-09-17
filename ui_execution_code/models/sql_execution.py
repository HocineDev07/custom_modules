# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from lxml import etree
import psycopg2


class SqlExecution(models.Model):
    _name = "sql.execution"
    _description = "SQL Execution"


    sql_expression = fields.Text(string='SQL Code', default='', help='Enter your SQL code here.')
    model_id = fields.Many2one('ir.model', string='Model')
    technical_name = fields.Char(string='Technical name', readonly='1', compute='get_technical_name')
    result = fields.Html(string='Result', readonly=True)

    def execute_sql_query(self):
        if self.sql_expression:
            try:
                self.env.cr.execute(self.sql_expression)
                query_result = self.env.cr.fetchall()
                if query_result:
                    # Create an HTML table to display the query result
                    table = etree.Element('table')
                    table.set('class', 'table table-bordered custom_table')

                    # Extract headers from the cursor description
                    headers = [col[0] for col in self.env.cr.description]

                    # Create table headers
                    thead = etree.SubElement(table, 'thead')
                    tr = etree.SubElement(thead, 'tr')
                    for header in headers:
                        th = etree.SubElement(tr, 'th')
                        th.set('style',
                               'background-color: #f5c4c4; font-weight: bold;')  # Set background color and font weight
                        th.text = str(header)  # Ensure header is converted to string

                    # Create table rows
                    tbody = etree.SubElement(table, 'tbody')
                    for i, row in enumerate(query_result):
                        tr = etree.SubElement(tbody, 'tr')
                        # Alternate row colors
                        if i % 2 == 0:
                            tr.set('style', 'background-color: #f2f2f2;')  # Set background color for even rows
                        for cell in row:
                            td = etree.SubElement(tr, 'td')
                            td.text = str(cell)  # Ensure cell value is converted to string

                    # Convert HTML table to string and assign to result field
                    result_html = etree.tostring(table, pretty_print=True, encoding='unicode')
                    self.result = result_html
                else:
                    self.result = 'No result'
            except psycopg2.Error as e:
                # Handle psycopg2 errors
                self.result = "<p>Error executing SQL expression: {}</p>".format(str(e))
                self.env.cr.rollback()  # Rollback the transaction
            except Exception as e:
                self.result = "<p>Error: {}</p>".format(str(e))
        else:
            self.result = 'No SQL expression provided'

    def clear_result(self):
        self.result = False

    def compute_result(self):
        self.execute_sql_query()

    @api.depends('model_id')
    def get_technical_name(self):
        tec_name = self.model_id.model
        if tec_name:
            tec_name2 = str(tec_name).replace('.', '_')
            self.technical_name = tec_name2

    # @api.depends('model_id')
    # def get_technical_name(self):
    #     return