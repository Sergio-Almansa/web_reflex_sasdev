import reflex as rx
from web_reflex_sasdev.routes import Route
import web_reflex_sasdev.constants as const
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.components.link_button import link_button
from web_reflex_sasdev.components.title import title
from web_reflex_sasdev.styles.styles import Size as Size
from web_reflex_sasdev.styles.colors import Color, TextColor

def portfolio_links() -> rx.Component:
    return rx.vstack(
        title("Desarrollo WEB"),
        rx.center(
            rx.vstack(
                rx.box(
                    rx.link(
                        rx.image(
                        src="/preview.png",
                        ),
                        href="https://sergioalmansa.dev",
                        is_external=True
                    ),
                    border_radius="15px",
                    border_width="thick",
                    border_color= Color.PRIMARY.value ,
                    width="100%"
                    
                ),
                rx.box(
                    rx.link(
                        rx.image(
                        src="/web_retos.jpg",
                        ), 
                        href="https://sasdev.reflex.run",
                        is_external=True
                    ),
                    border_radius="15px",
                    border_width="thick",
                    border_color= Color.PRIMARY.value ,
                    width="100%"
                                     
                ),

            ),
            

        ),
        title("Aplicaciones móviles Android"),
        rx.center(
            rx.flex(
                rx.box(
                    rx.image(
                        src="/asistmed/Asistmed_1.jpg"
                    ),
                    style=styles.image_miniatura_style
                    ),
                rx.box(
                    rx.image(
                        src="/asistmed/Asistmed_2.jpg"
                    ),
                    style=styles.image_miniatura_style
                ),
                rx.box(
                    rx.image(
                        src="/asistmed/Asistmed_3.jpg"
                    ),
                    style=styles.image_miniatura_style
                ),
                rx.box(
                    rx.image(
                        src="/asistmed/Asistmed_4.jpg"
                    ),
                    style=styles.image_miniatura_style
                ),
                rx.box(
                    rx.image(
                        src="/asistmed/Asistmed_5.jpg"
                    ),
                    style=styles.image_miniatura_style
                ),
                rx.box(
                    rx.image(
                        src="/asistmed/Asistmed_6.jpg"
                    ),
                    style=styles.image_miniatura_style
                ),
                rx.box(
                    rx.image(
                        src="/asistmed/Asistmed_7.jpg"
                    ),
                    style=styles.image_miniatura_style
                ),
                rx.box(
                    rx.image(
                        src="/asistmed/Asistmed_8.jpg"
                    ),
                    style=styles.image_miniatura_style
                ),
                rx.box(
                    rx.image(
                        src="/asistmed/Asistmed_9.jpg"
                    ),
                    style=styles.image_miniatura_style
                ),
                #"auto_colums",
                #"auto_rows",
                #"auto_flow",
                columns=[3],
                spacing="4",
                width="100%"
            ),
            

        ),
        title("Scripting Python"),
        link_button(
            "Automatización de tareas con Python",
            "Pequeños proyectos realizados Python",
            "/icons/setup.svg",
            const.MIWEB_URL
        ),
        title("WEB Scraping"),
        link_button(
            "WEB Scraping",
            "Scraping de páginas WEB",
            "/icons/setup.svg",
            const.MIWEB_URL
        ),
        title("Ciencia de datos"),
        link_button(
            "Ciencia de datos",
            "Proyectos de análsis de datos realizados con Python",
            "/icons/setup.svg",
            const.MIWEB_URL
        ),
        width="100%",
        spacing="2",
        align_items="center"
    )