# Hide Menus per User

Per-user module blocking for Odoo. Pick root menus (Sales, Purchase, Inventory…) on the user form and that user will see those modules with **empty lists**, **no action buttons** (New / Edit / Delete / Duplicate / Import / Export), and creation blocked **at the ORM level** — even via API.

Unlike security groups, the configuration is **per individual user**: two users with the same security profile can have different sets of blocked modules.

## Branches

This repository ships one branch per supported Odoo version. Each branch contains the module at the root, ready to drop into your `addons` path.

| Branch | Odoo Version |
|--------|--------------|
| [`16.0`](../../tree/16.0) | Odoo 16.0 |
| [`17.0`](../../tree/17.0) | Odoo 17.0 |
| [`18.0`](../../tree/18.0) | Odoo 18.0 |
| [`19.0`](../../tree/19.0) | Odoo 19.0 |

## Quick install

```bash
git clone -b 18.0 https://github.com/Yis1000/Hide-Menus-per-User-Odoo-16.0-17.0-18.0-19.0.git
cp -r Hide-Menus-per-User-Odoo-16.0-17.0-18.0-19.0/hide_menus_per_user /path/to/your/odoo/addons/
```

Then restart Odoo, update the apps list and install **Hide Menus per User** (category *Tools*).

## Usage

1. Open *Settings → Users & Companies → Users* and pick the user.
2. Switch to the **Blocked Modules** tab.
3. Click *Add a line* and pick one or more root menus.
4. Save. The change applies on the user's next page reload — no logout required.

## License

LGPL-3

## Author

Developed by [HIGA](https://higa.group/).
