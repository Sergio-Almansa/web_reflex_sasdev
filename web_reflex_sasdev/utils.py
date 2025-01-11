import reflex as rx

# Común

def lang() -> rx.Component:
   return rx.script("document.documentElement.lang='es'")

preview = "https://sergioalmansa.dev/preview.jpg"

_meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@sasdev"}
]

# Index
index_title = "Sergio Almansa | Desarrollo de aplicaciones"
index_description= "Hola, mi nombre es Sergio Almansa. Soy programador de software."

index_meta = [
        {"name": "og:title", "content": index_title},
        {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)


# Porfolio

portfolio_title = "Sergio Almansa | Mi portfolio personal"
portfolio_description= "Estos son mis proyectos como programador."

portfolio_meta = [
        {"name": "og:title", "content": portfolio_title},
        {"name": "og:description", "content": portfolio_description},
]
portfolio_meta.extend(_meta)


# Trayectoria

trayectoria_title = "SASDev | Trayectoria profesional"
trayectoria_description = "Te cuento mi trayectoria profesional."

trayectoria_meta = [
    {"name": "og.title", "content": trayectoria_title},
    {"name": "og.description", "content": trayectoria_description},
]

trayectoria_meta.extend(_meta)