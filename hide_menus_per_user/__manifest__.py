{
    "name": "Hide Menus per User",
    "version": "17.0.1.2.0",
    "summary": "Block selected modules per user: empty lists, no buttons, no creation",
    "description": """
Per-user module blocking. Pick root menus (Sales, Purchase, Inventory...) from the
user form and the user will see those modules with empty lists and no action buttons:
no New, Edit, Delete, Duplicate, Import or Export. Creation is also blocked at the
ORM level for those models, even via API.
    """,
    'author': 'Higa Solutions',
    "website": "https://higa.group/",
    "license": "LGPL-3",
    "category": "Tools",
    "depends": ["base"],
    "images": ["static/description/banner.png"],
    "data": [
        "views/res_users_views.xml",
    ],
    "installable": True,
    "application": False,
}

