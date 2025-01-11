import reflex as rx
from web_reflex_sasdev.routes import Route
import web_reflex_sasdev.constants as const
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size
from web_reflex_sasdev.styles.colors import Color as Color
from web_reflex_sasdev.styles.colors import TextColor as TextColor


def navbar() -> rx.Component:
        return rx.hstack(
            rx.link(
              rx.box(
              rx.el.span("sas", color=Color.PRIMARY.value),
              rx.el.span("dev", color=Color.SECONDARY.value),
              style=styles.navbar_title_style
            ),      
            href=Route.INDEX.value,
            ),
            position="sticky",
            bg=Color.CONTENT.value,
            padding_x=Size.BIG.value,
            padding_y=Size.DEFAULT.value,
            z_index="999",
            top="0",
            align="center"            
    )