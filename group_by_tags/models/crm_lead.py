# © 2021-2023 Alexandre Dutry, Albin Gilles, Nico Darnis
# © 2021-2023 Niboo SRL (<https://www.niboo.com/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    tags_ids_concatenated = fields.Char(
        "Concatenated Tags",
        store=True,
        compute="_compute_tags_ids_concatenated",
    )

    @api.depends("tag_ids")
    def _compute_tags_ids_concatenated(self):
        for lead in self:
            tag_ids_names = lead.tag_ids.mapped("name")
            tag_ids_names.sort(key=lambda y: y.lower())
            lead.tags_ids_concatenated = ", ".join(tag_ids_names)

    partner_tags_ids = fields.Many2many(
        related="partner_id.category_id",
        string="Partner Tags",
        readonly=True,
    )

    partner_tags_ids_concatenated = fields.Char(
        "Concatenated Partner Tags",
        store=True,
        compute="_compute_partner_tags_ids_concatenated",
    )

    @api.depends("partner_tags_ids")
    def _compute_partner_tags_ids_concatenated(self):
        for order in self:
            partner_tags_ids_names = order.partner_tags_ids.mapped("name")
            partner_tags_ids_names.sort(key=lambda y: y.lower())
            order.partner_tags_ids_concatenated = ", ".join(partner_tags_ids_names)
