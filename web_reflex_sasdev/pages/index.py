import reflex as rx
#from web_reflex_sasdev.routes import Route
import web_reflex_sasdev.utils as utils
from web_reflex_sasdev.components.navbar import navbar
from web_reflex_sasdev.components.footer import footer
from web_reflex_sasdev.views.header import header
from web_reflex_sasdev.views.index_links import links
import web_reflex_sasdev.styles.styles as styles
from web_reflex_sasdev.styles.styles import Size as Size
import web_reflex_sasdev.constants as const



@rx.page(
    title=utils.index_title,
    description=utils.index_description,        
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                align="center"
            ),        
        ),
        footer(),
    )
