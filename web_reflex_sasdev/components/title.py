import reflex as rx
import web_reflex_sasdev.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="6",
        style=styles.title_style
    )