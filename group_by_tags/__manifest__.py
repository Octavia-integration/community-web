# © 2021-2023 Alexandre Dutry, Albin Gilles, Nico Darnis
# © 2021-2023 Niboo SRL (<https://www.niboo.com/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Group by Tags",
    "category": "Hidden",
    "summary": "Module to group by Tags in CRM, Sales, and CRM and contacts",
    "website": "https://www.niboo.com/",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "description": """

    """,
    "author": "Niboo",
    "depends": ["base", "crm", "sale"],
    "data": [
        "views/crm_search_views.xml",
        "views/res_partner_views.xml",
        "views/crm_views.xml",
        "views/sale_search_views.xml",
        "views/sale_views.xml",
        "report/sale_report_view.xml",
    ],
    "installable": True,
    "application": False,
}
