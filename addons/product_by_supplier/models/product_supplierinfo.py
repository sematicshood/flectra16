# Copyright 2010-2013 Elico Corp. <lin.yu@elico-corp.com>
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from flectra import models, fields


class ProductSupplierinfo(models.Model):
    _inherit = 'product.supplierinfo'

    delay = fields.Integer(group_operator='avg')
