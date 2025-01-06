import reflex as rx
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size
from web_reflex_sasdev.styles.colors import Color as Color
from web_reflex_sasdev.styles.colors import TextColor as TextColor

def link_button(text: str, body: str, image: str, url: str, is_external= True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=text
                ),
                rx.vstack(
                    rx.text(text, style = styles.button_title_style),
                    rx.text(body, style = styles.button_body_style),
                    spacing="1",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                    #margin=Size.ZERO.value,
                    
                ),
                width="100%",
                align="center"
            ),
        ),
        href= url,
        is_external= is_external,
        width="100%"
    )