import reflex as rx
import datetime
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size
from web_reflex_sasdev.styles.colors import Color as Color
from web_reflex_sasdev.styles.colors import TextColor as TextColor
import web_reflex_sasdev.constants as const

def footer() -> rx.Component:
        return rx.vstack(
            rx.image(
                src="/logo_sasdev_300_sin_fondo.png",
                width="10em",
                height="10em",
                padding=Size.ZERO.value,
                alt="Logotipo SASDev. Un teclado con mi acrónimo."
            ),
            rx.link(
                f"© 2023-{datetime.date.today().year} SASDev by Sergio Almansa",
                href="https://www.sergioalmansa.dev",
                is_external= True,
                font_size=Size.MEDIUM.value
            ),
            rx.text(
                "BUILDING SOFTWARE WITH ♥ FROM MURCIA.",
                font_size=Size.MEDIUM.value,
                margin_top=Size.ZERO.value
            ),
            align="center",
            margin_bottom=Size.BIG.value,
            pading_bottom=Size.BIG.value,
            padding_x=Size.BIG.value,
            spacing="0",
            color=TextColor.FOOTER.value
        )
