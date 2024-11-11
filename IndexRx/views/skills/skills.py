import reflex as rx
from PIL import Image
import requests

shadow = "0 3px 6px #00000029, 0 3px 6px #0000003b"

def skills() -> rx.Component:
    return rx.vstack(
                
                rx.heading("Skills",
                           size="8",
                           font_weight="500"),
                
                
                rx.grid(
                    rx.box(
                            rx.avatar(src="https://img.icons8.com/?size=256&id=20909&format=png",
                                      height = "100%",
                                      width = "100%",
                                      padding = "5px"),
                            bg_color = "#f7f7f7",
                            height="100px",
                            width="100px",
                            box_shadow = shadow,
                            border_radius = "20px"
                            
                        ),
                    rx.box(
                            rx.avatar(src="https://img.icons8.com/?size=256&id=7gdY5qNXaKC0&format=png",
                                      height = "100%",
                                      width = "100%",
                                      padding = "5px"),
                            bg_color = "#f7f7f7",
                            height="100px",
                            width="100px",
                            box_shadow = shadow,
                            border_radius = "20px"
                        ),
                    rx.box(
                            rx.avatar(src="https://img.icons8.com/?size=256&id=108784&format=png",
                                      height = "100%",
                                      width = "100%",
                                      padding = "5px"),
                            bg_color = "#f7f7f7",
                            height="100px",
                            width="100px",
                            box_shadow = shadow,
                            border_radius = "20px"
                        ),
                    rx.box(
                            rx.avatar(src="https://img.icons8.com/?size=256&id=PndQWK6M1Hjo&format=png",
                                      height = "100%",
                                      width = "100%",
                                      padding = "5px"),
                            height="100px",
                            width="100px",
                            bg_color = "#f7f7f7",
                            box_shadow = shadow,
                            border_radius = "20px"
                        ),
                    rx.box(
                            rx.avatar(src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_python_icon_130221.png",
                                      height = "100%",
                                      width = "100%",
                                      padding = "5px"),
                            bg_color = "#f7f7f7",
                            height="100px",
                            width="100px",
                            box_shadow = shadow,
                            border_radius = "20px"
                        ),
                    rx.box(
                            rx.avatar(src="https://img.icons8.com/?size=256&id=hCWb1IvpcBZ0&format=png",
                                      height = "100%",
                                      width = "100%",
                                      padding = "5px"),
                            height="100px",
                            width="100px",
                            bg_color = "#f7f7f7",
                            box_shadow = shadow,
                            border_radius = "20px"
                        ),
                    
                    rx.box(
                            rx.avatar(src="https://raw.githubusercontent.com/reflex-dev/reflex-web/refs/heads/main/assets/favicon.ico",
                                      height = "100%",
                                      width = "100%",
                                      padding = "10px"),
                            height="100px",
                            width="100px",
                            bg_color = "#f7f7f7",
                            box_shadow = shadow,
                            border_radius = "20px"
                        ),
                    rx.box(
                            rx.avatar(src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_git_icon_130581.png",
                                      height = "100%",
                                      width = "100%",
                                      padding = "5px"),
                            height="100px",
                            width="100px",
                            bg_color = "#f7f7f7",
                            box_shadow = shadow,
                            border_radius = "20px"
                        ),
                    
                    
                    columns=rx.breakpoints(initial="2", sm="4", lg="8"),
                    spacing="8",
                    
        ),
        
        width = "100%",
        justify="center",
        align="center",
        margin_top = "5%",
        id = "Skills"
    )