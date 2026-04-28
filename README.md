# Hide Menus per User — Odoo 19.0

Bloqueo de módulos por usuario para **Odoo 19.0**. Eliges menús raíz en la ficha del usuario y ese usuario verá esos módulos con listas vacías, sin botones de acción (Nuevo / Editar / Eliminar / Duplicar / Importar / Exportar) y con la creación bloqueada a nivel ORM.

Esta rama es solo para **Odoo 19.0**. Para otras versiones consulta la rama correspondiente (`16.0`, `17.0`, `18.0`).

## Instalación

1. Copia `hide_menus_per_user/` a tu directorio de `addons` de Odoo (p. ej. `/mnt/extra-addons/`).
2. Reinicia Odoo.
3. *Aplicaciones → Actualizar lista de aplicaciones*, busca **Hide Menus per User** (categoría *Herramientas*) e instala.

## Uso

1. *Ajustes → Usuarios y compañías → Usuarios* → elige un usuario.
2. Abre la pestaña **Blocked Modules** (Módulos bloqueados).
3. *Añadir una línea* y selecciona uno o varios menús raíz (p. ej. Ventas, Compras, Inventario).
4. Guarda. El cambio se aplica al recargar la página del usuario.

## Licencia

LGPL-3 — Desarrollado por [HIGA](https://higa.group/).
