# Copyright 2016 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)

from flectra import api, fields, models


class DateRange(models.Model):
    _inherit = "date.range"

    days = fields.Integer(
        string="Days between dates",
        compute='_compute_days',
        readonly=True,
    )

    @api.multi
    @api.depends('date_start', 'date_end')
    def _compute_days(self):
        for rec in self.filtered(lambda x: x.date_start and x.date_end):
            rec.days = abs((
                fields.Date.from_string(rec.date_end) -
                fields.Date.from_string(rec.date_start)
            ).days) + 1
