import reflex as rx
from web_reflex_sasdev.routes import Route
import web_reflex_sasdev.utils as utils
from web_reflex_sasdev.components.navbar import navbar
from web_reflex_sasdev.views.header import header
from web_reflex_sasdev.views.portfolio_links import portfolio_links
from web_reflex_sasdev.components.footer import footer
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size

@rx.page(
    route=Route.CAREER_PATH.value,
    title=utils.trayectoria_title,
    description=utils.trayectoria_description,
    image=utils.preview,
    meta=utils.trayectoria_meta  
)
def career_path() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                rx.spacer(),
                rx.spacer(),                
                rx.image(
                    src="/under_construction.png",
                    width="15em",
                    height="15em",
                ),align="center",
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                
            ),
        ),
        footer(),
        
    )