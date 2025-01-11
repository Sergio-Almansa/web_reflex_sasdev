import reflex as rx
from web_reflex_sasdev.pages.index import index
from web_reflex_sasdev.pages.portfolio import portfolio
from web_reflex_sasdev.pages.career_path import career_path
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size
import web_reflex_sasdev.constants as const



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

