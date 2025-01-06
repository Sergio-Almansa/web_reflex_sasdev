import reflex as rx
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src= image,
            width= Size.DEFAULT.value,
            alt= alt
        ),
        href= url,
        is_external= True,
    )