import reflex as rx
import web_reflex_sasdev.utils as utils
from web_reflex_sasdev.components.navbar import navbar
from web_reflex_sasdev.views.header import header
from web_reflex_sasdev.views.portfolio_links import portfolio_links
from web_reflex_sasdev.components.footer import footer
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.routes import Route
from web_reflex_sasdev.styles.styles import Size as Size

@rx.page(
    route=Route.PORTFOLIO.value,
    title=utils.portfolio_title,
    description=utils.portfolio_description,
    image=utils.preview,
    meta=utils.portfolio_meta  
)
def portfolio() -> rx.Component:
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
                    height="15em"
                ),
                portfolio_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                align="center"
                
            ),
        ),
        footer(),
    )