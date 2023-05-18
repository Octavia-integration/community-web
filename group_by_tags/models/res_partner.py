# © 2021-2023 Alexandre Dutry, Albin Gilles, Nico Darnis
# © 2021-2023 Niboo SRL (<https://www.niboo.com/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    category_ids_concatenated = fields.Char(
        "Concatenated Tags",
        store=True,
        compute="_compute_category_ids_concatenated",
    )

    @api.depends("category_id")
    def _compute_category_ids_concatenated(self):
        for partner in self:
            category_ids_names = partner.category_id.mapped("name")
            category_ids_names.sort(key=lambda y: y.lower())
            partner.category_ids_concatenated = ", ".join(category_ids_names)
