from odoo import _, api, models
from odoo.exceptions import AccessError
from odoo.osv import expression


_NEVER_HIDE = frozenset({
    "res.users", "res.groups", "res.company", "res.lang",
    "res.country", "res.country.state", "res.partner.title",
})


class Base(models.AbstractModel):
    _inherit = "base"

    def _hide_for_current_user(self):
        if self.env.context.get("_skip_hide_menus"):
            return False
        name = self._name
        if name.startswith("ir.") or name.startswith("base.") or name in _NEVER_HIDE:
            return False
        user = self.env.user
        if not user or user._is_superuser():
            return False
        if not user.with_context(_skip_hide_menus=True).hidden_menu_ids:
            return False
        return name in user.with_context(_skip_hide_menus=True)._hidden_model_names()

    @api.model
    def _search(self, domain, *args, **kwargs):
        if self._hide_for_current_user():
            return super()._search(expression.FALSE_DOMAIN, *args, **kwargs)
        return super()._search(domain, *args, **kwargs)

    @api.model_create_multi
    def create(self, vals_list):
        if self._hide_for_current_user():
            raise AccessError(
                _("You are not allowed to create %s records.",
                  self._description or self._name)
            )
        return super().create(vals_list)

    @api.model
    def _get_view(self, view_id=None, view_type="form", **options):
        arch, view = super()._get_view(view_id=view_id, view_type=view_type, **options)
        if view_type in ("list", "tree", "kanban", "form") and self._hide_for_current_user():
            arch.set("create", "0")
            arch.set("delete", "0")
            arch.set("edit", "0")
            arch.set("import", "0")
            arch.set("export_xlsx", "0")
            arch.set("duplicate", "0")
        return arch, view
