import reflex as rx

config = rx.Config(
    app_name="web_reflex_sasdev",
    cors_allowed_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "https://sergioalmansa.dev"
    ]
)