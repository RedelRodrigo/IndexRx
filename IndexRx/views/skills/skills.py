import reflex as rx
from PIL import Image
import requests

shadow = "0 3px 6px #00000029, 0 3px 6px #0000003b"


def skills() -> rx.Component:
    return rx.vstack(
        rx.heading("Skills", size="8", font_weight="500"),
        rx.grid(
            rx.box(
                rx.avatar(
                    src="https://img.icons8.com/?size=256&id=20909&format=png",
                    height="100%",
                    width="100%",
                    padding="5px",
                    class_name="Skill_HTML",
                ),
                bg_color="#f7f7f7",
                height="100px",
                width="100px",
                box_shadow=shadow,
                border_radius="20px",
            ),
            rx.box(
                rx.avatar(
                    src="https://img.icons8.com/?size=256&id=7gdY5qNXaKC0&format=png",
                    height="100%",
                    width="100%",
                    padding="5px",
                    class_name="Skill_Css",
                ),
                bg_color="#f7f7f7",
                height="100px",
                width="100px",
                box_shadow=shadow,
                border_radius="20px",
            ),
            rx.box(
                rx.avatar(
                    src="https://img.icons8.com/?size=256&id=108784&format=png",
                    height="100%",
                    width="100%",
                    padding="5px",
                    class_name="Skill_JS",
                ),
                bg_color="#f7f7f7",
                height="100px",
                width="100px",
                box_shadow=shadow,
                border_radius="20px",
            ),
            rx.box(
                rx.avatar(
                    src="https://img.icons8.com/?size=256&id=PndQWK6M1Hjo&format=png",
                    height="100%",
                    width="100%",
                    padding="5px",
                    class_name="Skill_Boostrap",
                ),
                height="100px",
                width="100px",
                bg_color="#f7f7f7",
                box_shadow=shadow,
                border_radius="20px",
            ),
            rx.box(
                rx.avatar(
                    src="/piton.png",
                    height="100%",
                    width="100%",
                    padding="5px",
                    class_name="Skill_Python",
                ),
                bg_color="#f7f7f7",
                height="100px",
                width="100px",
                box_shadow=shadow,
                border_radius="20px",
            ),
            rx.box(
                rx.avatar(
                    src="https://seeklogo.com/images/F/fastapi-logo-541BAA112F-seeklogo.com.png",
                    height="100%",
                    width="100%",
                    padding="5px",
                    class_name="Skill_FastAPI",
                ),
                height="100px",
                width="100px",
                bg_color="#f7f7f7",
                box_shadow=shadow,
                border_radius="20px",
            ),
            rx.box(
                rx.avatar(
                    src="https://raw.githubusercontent.com/reflex-dev/reflex-web/refs/heads/main/assets/favicon.ico",
                    height="100%",
                    width="100%",
                    padding="10px",
                ),
                height="100px",
                width="100px",
                bg_color="#f7f7f7",
                box_shadow=shadow,
                border_radius="20px",
            ),
            rx.box(
                rx.avatar(
                    src="https://git-scm.com/images/logos/logomark-orange@2x.png",
                    height="100%",
                    width="100%",
                    padding="5px",
                    class_name="Skill_Git",
                ),
                height="100px",
                width="100px",
                bg_color="#f7f7f7",
                box_shadow=shadow,
                border_radius="20px",
            ),
            columns=rx.breakpoints(initial="2", sm="4", lg="8"),
            spacing="8",
        ),
        width="100%",
        justify="center",
        align="center",
        margin_top="5%",
        id="Skills",
    )
