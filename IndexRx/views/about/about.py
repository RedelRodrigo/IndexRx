import reflex as rx
from PIL import Image
import requests


class ImageState(rx.State):
    url = f"https://avatars.githubusercontent.com/u/170350965?v=4"
    image = Image.open(requests.get(url, stream=True).raw)


def about() -> rx.Component:
    return rx.vstack(
        rx.heading("Sobre mí", size="8", font_weight="500"),
        rx.image(
            src=ImageState.image,
            width=250,
            height="auto",
            border_radius="100%",
        ),
        rx.vstack(
            rx.text(
                "Desde los 15 años que sé que quiero dedicarme a la Programación, a lo largo de mi vida he tomado los caminos que me lleven a realizar ese objetivo. Hoy curso la carrera universitaria en programación y, a su vez, estudio en línea para mejorar mis habilidades, y siempre al tanto de nuevos cursos de mi interés, y así poder ser un desarrollador full stack de calidad.",
                align="center",
                font_weight="300",
                margin_top="10px",
            ),
            rx.text(
                "Tengo proyectos personales y colaborativos que he desarrollado con tecnologías como HTML, CSS, JavaScript, Python , entre otras. Me apasiona la programación y me gusta aprender nuevas tecnologías.",
                align="center",
                font_weight="300",
            ),
            rx.text(
                "Estoy en búsqueda de una posición full time donde pueda seguir adquiriendo nuevos conocimientos y mejorar mis habilidades como desarrollador en un equipo de trabajo.",
                align="center",
                font_weight="300",
            ),
            width="80%",
        ),
        rx.button(
            "Download CV",
            rx.icon("download"),
            on_click=rx.download(
                url="/Redel_Rodrigo_FullStack_Developer.pdf",
                filename="Redel_Rodrigo_FullStack_Developer.pdf",
            ),
            color_scheme="purple",
            height="58px",
            border_radius="15px",
            margin_top="2%",
        ),
        width="100%",
        align="center",
        margin_top="4%",
        id="Sobre_mi",
    )
