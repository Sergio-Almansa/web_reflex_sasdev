import reflex as rx
from web_reflex_sasdev.routes import Route
from web_reflex_sasdev.components.link_button import link_button
from web_reflex_sasdev.components.title import title
from web_reflex_sasdev.styles.styles import Size, Color
import web_reflex_sasdev.constants as const

def links() -> rx.Component:
    return rx.vstack(
        title("Proyectos y más"),
        link_button("PORTFOLIO",
                     "Proyectos desarrollados por mí",
                     "/icons/setup.svg",
                     Route.PORTFOLIO.value,
                     False
                     ),
        link_button("GitHub",
                    "Repos de mis proyectos",
                    "/icons/github.svg",
                    const.GITHUB_URL
                    ),
        title("Redes Sociales"),
        link_button("LinkedIn",
                     "Mi página personal de LinkedIn",
                     "/icons/linkedin.svg",
                     const.LINKEDIN_URL
                     ),
        title("Trayectoria profesional"),
        link_button("A qué me he dedicado estos años",
                    "Te cuento con detalle",
                    "/icons/book.svg",
                    Route.CAREER_PATH.value,
                    is_external=False
                    ),
        title("Contacto"),
        link_button("Email",
                    "Contacta conmigo mediante correo electrónico",
                    "/icons/email.svg",
                    f"mailto:{const.EMAIL}"
                    ),
        link_button("Whatsapp",
                    "Contacta conmigo mediante Whatsapp",
                    "/icons/whatsapp.svg",
                    f"https://api.whatsapp.com/send?phone={const.TELEPHONE}"
                    ),            
        width="100%",
        spacing="2"
    )
