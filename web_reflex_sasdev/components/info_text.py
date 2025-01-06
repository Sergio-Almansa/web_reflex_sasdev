import reflex as rx
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size
from web_reflex_sasdev.styles.colors import Color as Color
from web_reflex_sasdev.styles.colors import TextColor as TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text.strong(
            title,
            font_weight="bold",
            color =Color.PRIMARY.value
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value
    )