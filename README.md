# Hide Menus per User — Odoo 17.0

Per-user module blocking for **Odoo 17.0**. Pick root menus on the user form and that user will see those modules with empty lists, no action buttons (New / Edit / Delete / Duplicate / Import / Export), and creation blocked at the ORM level.

This branch targets **Odoo 17.0** only. For other versions check the matching branch (`16.0`, `18.0`, `19.0`).

## Install

1. Copy `hide_menus_per_user/` into your Odoo `addons` path (e.g. `/mnt/extra-addons/`).
2. Restart Odoo.
3. *Apps → Update Apps List*, search **Hide Menus per User** (category *Tools*) and install.

## Usage

1. *Settings → Users & Companies → Users* → pick a user.
2. Open the **Blocked Modules** tab.
3. *Add a line* and select one or more root menus (e.g. Sales, Purchase, Inventory).
4. Save. The change applies on the user's next page reload.

## License

LGPL-3 — Developed by [HIGA](https://higa.group/).
