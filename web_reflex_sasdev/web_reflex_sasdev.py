import reflex as rx
from web_reflex_sasdev.components.navbar import navbar
from web_reflex_sasdev.components.footer import footer
from web_reflex_sasdev.views.header import header
from web_reflex_sasdev.views.links import links
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size
import web_reflex_sasdev.constants as const

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
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{const.G_TAG}');
"""     ),
    ],

)

title = "Sergio Almansa | Desarrollo de aplicaciones"
description= "Hola, mi nombre es Sergio Almansa. Soy programador de software."
preview = "https://sergioalmansa.dev/preview.jpg"

app.add_page(
    index,
    title=title,
    description=description,
    image="avatarSergio.jpg",
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@sasdev"}
    ]
)
