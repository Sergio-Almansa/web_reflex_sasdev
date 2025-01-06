import reflex as rx
import datetime
from web_reflex_sasdev.components.link_icon import link_icon
from web_reflex_sasdev.components.info_text import info_text
from web_reflex_sasdev.components.title import title
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size
from web_reflex_sasdev.styles.colors import TextColor as TextColor
from web_reflex_sasdev.styles.colors import Color as Color
from web_reflex_sasdev.styles.colors import TextColor as TextColor
import web_reflex_sasdev.constants as const
from web_reflex_sasdev.styles.fonts import Font as Font
from web_reflex_sasdev.styles.fonts import FontWeight as FontWeight

def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Sergio Almansa",
                size="6",
                src="/avatarSergio.jpg",
                color=TextColor.BODY.value,
                bg=Color.PRIMARY.value,
                padding="3px",
                radius="full"
             ),
            rx.vstack(
                rx.heading(
                    "Sergio Almansa Saura",
                    size="4"
                ),
                rx.text(
                    "@sasdev",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "Github"
                    ),
                    link_icon(
                        "/icons/setup.svg",
                        const.MIWEB_URL,
                        "SASDev WEB"
                    ),
                    spacing="4"
                ),
                align_items="start"
            ),
            rx.spacer(),
            rx.image(
                src="/logo_sasdev_300_sin_fondo.png",
                width="7em",
                height="7em"
            ),
            spacing="2",
            width="100%",
            align_items="center"
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience_teleco()}+",
                        "años sector teleco"
                    ),
                    rx.spacer(),
                    info_text(
                        "20+", "certificaciones"
                    ),
                    rx.spacer(),
                    info_text(
                        f"{experience_developer()}+",
                        "años programador"
                    ),
                    width="100%",
                    font_family=Font.DEFAULT.value,
                    font_weight= FontWeight.LIGHT.value,
                    #font_weight=FontWeight.MEDIUM.value
                ),
                rx.text(
                    f"""Soy un profesional con más de 25 años de experiencia en el sector
                    de las telecomunicaciones, habiendo trabajado en roles diversos dentro
                    de multinacionales. Mi formación como Técnico Superior en Desarrollo de
                    Aplicaciones, respalda mi sólido conocimiento como programador. En los
                    últimos años, he desempeñado roles clave como PMO, analista de datos y
                    BI. Mi enfoque proactivo para resolver problemas y mi capacidad para
                    trabajar de manera colaborativa, me han permitido contribuir significativamente
                    al éxito de los proyectos en los que he trabajado. En paralelo, y a nivel
                    personal, he abordado pequeños desarrollos de aplicaciones web, scripting,
                    web scraping y ciencia de datos. Aquí podrás encontrar mi portfolio, así como
                    todos mis enlaces de interés. Esta WEB, la he desarrollado por completo y desde
                    cero con Python. ¡Bienvenid@!""",
                    
                    font_size=Size.MEDIUM.value,
                    color=TextColor.BODY.value
                ),
                width="100%",
                spacing="4",
                align_items="start"
            )
        ),
        width="100%",
        spacing="4",
        align_items="start"
    )


def experience_teleco() -> int:
    return datetime.date.today().year - 1999

def experience_developer() -> int:
    return datetime.date.today().year - 2019