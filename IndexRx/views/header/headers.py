import reflex as rx

def headers() -> rx.Component:
    return rx.vstack(
            rx.heading("Hola mundo, soy",
                       size="6",
                       font_size = "calc(1vw + 1.5em)"
                       ),
            
            
            rx.heading("Rodrigo",
                       font_family = "Sacramento",
                       size="9",
                       font_size = "calc(6vw + 2.5em)",
                       margin_top = "4%"
                       ),
            
            rx.heading("Full Stack developer",
                    margin_top = "3%",
                    size="4"),
            
            rx.text("Experiencia en desarrollo web y diseño, produciendo proyectos de calidad",
                    font_weight = "300",
                    width = "70%",
                    align="center"),
            
            rx.link(rx.button(
                "Contacto",
                rx.icon("arrow-big-right-dash",
                        size=20
                        ),
                size="9",
                height = "58px",
                width = "125px",
                font_size = "15px",
                color_scheme="purple",
                border_radius = "15px"
            ),
                margin_top = "1%",
                href="#Contacto"),
            
        
        width = "100%",
        align="center",
        margin_top = "5%"
    )