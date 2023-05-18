# © 2021-2023 Alexandre Dutry, Albin Gilles, Nico Darnis
# © 2021-2023 Niboo SRL (<https://www.niboo.com/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    order_create_date = fields.Datetime("Creation Date", readonly=True)

    tag_ids = fields.Many2many("Tags", related="order_id.tag_ids", readonly=True)
    tag_ids_concatenated = fields.Char("Concatenated Tags", readonly=True)

    partner_tags_ids = fields.Many2many(
        related="order_id.partner_id.category_id",
        string="Partner Tags",
        readonly=True,
    )
    partner_tags_ids_concatenated = fields.Char(
        "Concatenated Partner Tags",
        readonly=True,
    )

    def _query(self, with_clause="", fields=None, groupby="", from_clause=""):
        if fields is None:
            fields = {}

        fields.update(
            {
                "order_create_date": ", s.create_date as order_create_date",
                "tag_ids_concatenated": ", s.tag_ids_concatenated as tag_ids_concatenated",
                "partner_tags_ids_concatenated": ", s.partner_tags_ids_concatenated as partner_tags_ids_concatenated",
            }
        )
        groupby += ", s.create_date, s.tag_ids_concatenated"
        return super()._query(with_clause, fields, groupby, from_clause)
