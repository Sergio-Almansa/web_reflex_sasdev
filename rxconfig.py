import reflex as rx

config = rx.Config(
    app_name="sasdev_web_new",
    api_url="https://api.sergioalmansa.dev",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
