from odoo import fields, models, tools


_ACTION_MODEL_FIELD = {
    "ir.actions.act_window": "res_model",
    "ir.actions.report": "model",
    "ir.actions.server": "model_name",
}


class ResUsers(models.Model):
    _inherit = "res.users"

    hidden_menu_ids = fields.Many2many(
        comodel_name="ir.ui.menu",
        relation="res_users_hidden_menu_rel",
        column1="user_id",
        column2="menu_id",
        string="Blocked Modules",
        domain=[("parent_id", "=", False)],
        help="Root menus blocked for this user. Models reachable ONLY through "
             "these menus will appear empty (no records, no New / Edit / Delete / "
             "Import / Export) and creation is blocked at the ORM level.",
    )

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ["hidden_menu_ids"]

    @tools.ormcache("self.id")
    def _hidden_model_names(self):
        self.ensure_one()
        if not self.hidden_menu_ids:
            return frozenset()

        Menu = self.env["ir.ui.menu"].sudo().with_context(
            _skip_hide_menus=True, **{"ir.ui.menu.full_list": True}
        )

        def models_of(menus):
            names = set()
            for menu in menus:
                action = menu.action
                if not action:
                    continue
                field = _ACTION_MODEL_FIELD.get(action._name)
                if not field:
                    continue
                value = getattr(action, field, False)
                if value:
                    names.add(value)
            return names

        hidden_menus = Menu.search([("id", "child_of", self.hidden_menu_ids.ids)])
        other_menus = Menu.search([("id", "not in", hidden_menus.ids)])
        return frozenset(models_of(hidden_menus) - models_of(other_menus))

    def write(self, vals):
        res = super().write(vals)
        if "hidden_menu_ids" in vals:
            self.env.registry.clear_caches()
        return res
