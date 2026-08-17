import reflex as rx

config = rx.Config(
    app_name="web_reflex_sasdev",
    api_url="https://api.sergioalmansa.dev",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
