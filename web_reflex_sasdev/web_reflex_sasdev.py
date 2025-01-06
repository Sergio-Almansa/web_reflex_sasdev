import reflex as rx
from web_reflex_sasdev.components.navbar import navbar
from web_reflex_sasdev.components.footer import footer
from web_reflex_sasdev.views.header.header import header
from web_reflex_sasdev.views.links.links import links
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                align="center"
            ),        
        ),
        footer(),
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="SASDev | Desarrollo SW y Análisis de datos",
    description="Hola, me llamo Sergio Almansa Saura y soy desarrollador de Software",
    image="/avatarSergio.jpg"
)
