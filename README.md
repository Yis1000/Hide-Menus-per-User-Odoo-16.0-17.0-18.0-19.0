# Hide Menus per User

Bloqueo de módulos por usuario en Odoo. Eliges menús raíz (Ventas, Compras, Inventario…) en la ficha del usuario y ese usuario verá esos módulos con **listas vacías**, **sin botones de acción** (Nuevo / Editar / Eliminar / Duplicar / Importar / Exportar) y la creación bloqueada **a nivel ORM** — incluso vía API.

A diferencia de los grupos de seguridad, la configuración es **por usuario individual**: dos usuarios con el mismo perfil de seguridad pueden tener distintos módulos bloqueados.

## Ramas

Este repositorio publica una rama por versión soportada de Odoo. Cada rama contiene el módulo en la raíz, listo para soltar en tu directorio de `addons`.

| Rama | Versión de Odoo |
|--------|--------------|
| [`16.0`](../../tree/16.0) | Odoo 16.0 |
| [`17.0`](../../tree/17.0) | Odoo 17.0 |
| [`18.0`](../../tree/18.0) | Odoo 18.0 |
| [`19.0`](../../tree/19.0) | Odoo 19.0 |

## Instalación rápida

```bash
git clone -b 18.0 https://github.com/Yis1000/Hide-Menus-per-User-Odoo-16.0-17.0-18.0-19.0.git
cp -r Hide-Menus-per-User-Odoo-16.0-17.0-18.0-19.0/hide_menus_per_user /ruta/a/tu/odoo/addons/
```

Después reinicia Odoo, actualiza la lista de aplicaciones e instala **Hide Menus per User** (categoría *Herramientas*).

## Uso

1. Abre *Ajustes → Usuarios y compañías → Usuarios* y elige el usuario.
2. Ve a la pestaña **Blocked Modules** (Módulos bloqueados).
3. Pulsa *Añadir una línea* y selecciona uno o varios menús raíz.
4. Guarda. El cambio se aplica al recargar la página del usuario — no hace falta cerrar sesión.

## Licencia

LGPL-3

## Autor

Desarrollado por [HIGA](https://higa.group/).
