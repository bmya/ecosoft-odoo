# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv
from openerp import fields as newfields, models, api

# Available commission rule
COMMISSION_RULE = [
    ('percent_fixed', 'Fixed Commission Rate'),
    ('percent_product_category', 'Product Category Commission Rate'),
    ('percent_product', 'Product Commission Rate'),
    ('percent_product_step', 'Product Commission Rate Steps'),
    ('percent_amount', 'Commission Rate By Order Amount')]


class commission_rule(models.Model):

    _name = "commission.rule"
    _description = "Commission Rule"

    name = newfields.Char('Name', size=64, required=True)
    type = newfields.Selection(COMMISSION_RULE, 'Type', required=True)
    fix_percent = newfields.Float('Fix Percentage')
    rule_rates = newfields.One2many(
        'commission.rule.rate', 'commission_rule_id', 'Rates')
    # comentado para ver si cambia el error
    # rule_conditions = newfields.One2many(
    #    'commission.rule.condition', 'commission_rule_id', 'Conditions')
    rule_conditions = newfields.Integer('Conditions')
    active = newfields.Boolean('Active', default=True)
    sale_team_ids = newfields.One2many(
        'sale.team', 'commission_rule_id', 'Teams')
    salesperson_ids = newfields.One2many(
        'res.users', 'commission_rule_id', 'Salesperson')
    


class commission_rule_rate(models.Model):

    _name = "commission.rule.rate"
    _description = "Commission Rule Rate"
    
    commission_rule_id = newfields.Many2one(
        'commission.rule', 'Commission Rule')
    amount_over = newfields.Float('Amount Over', required=True)
    amount_upto = newfields.Float('Amount Up-To', required=True)
    percent_commission = newfields.Float('Commission (%)', required=True)
    
    _order = 'id'

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
