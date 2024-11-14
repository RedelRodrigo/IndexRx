import reflex as rx

def exp() -> rx.Component:
    return rx.vstack(
        
        rx.heading("Mi Experiencia",
                   size="8",
                   font_weight = "500"),
        
        rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger(rx.icon("graduation-cap"),
                                    "Education",
                                    value="Edu",
                                    margin_right= "13vw",
                                    margin_left = "7vw",
                                    font_size = "20px",
                                    color_scheme="purple"
                                    ),
                    rx.tabs.trigger(rx.icon("briefcase-business"),
                                    "Work",
                                    value="Work",
                                    margin_left = "13vw",
                                    margin_right= "7vw",
                                    font_size = "20px",
                                    color_scheme="purple"
                                    ),     
            ),
                rx.tabs.content(
                        rx.vstack(
                            
                            rx.heading("Técnico electrónico",
                                       size="4"),
                            rx.text("Escuela Nacional de Educación Técnica N°1",
                                    font_weight = "400"),
                            rx.text("2013 - 2020",
                                    font_weight = "200"),
                            
                            align="center"
                           
                    ),
                        rx.vstack(
                            
                            rx.heading("Desarrollo web Full Stack: Python",
                                       size="4"),
                            rx.text("Codo a Codo",
                                    font_weight = "400"),
                            rx.text("Febrero 2024 - Julio 2024",
                                    font_weight = "200"),
                           margin_top = "3%",
                           align="center"
                    ),
                        rx.vstack(
                            
                            rx.heading("Tecnicatura Universitaria en Programación",
                                       size="4"),
                            rx.text("Universidad Provincial del SudOeste",
                                    font_weight = "400"),
                            rx.text(" Marzo 2024 - Diciembre 2025",
                                    font_weight = "200"),
                           margin_top = "3%",
                           align="center"
                    ),
                         margin_top = "2%",
                        value="Edu"
                    ),
                
                rx.tabs.content(
                            
                            
                        rx.vstack(
                            
                            rx.heading("FreeLance",
                                       size="4"),
                            rx.text("Outlier.ai",
                                    font_weight = "400"),
                            rx.text("En actividad",
                                    font_weight = "200"),
                            
                            align="center"
                           
                    ),
                        rx.vstack(
                            
                            rx.heading("Diseñador Web",
                                       size="4"),
                            rx.text("FreeLance",
                                    font_weight = "400"),
                            rx.text("En actividad",
                                    font_weight = "200"),
                           
                           margin_top = "3%",
                           align="center"
                    ),
                        rx.vstack(
                            
                            rx.heading("Creador y encargado de actualizar catalogo",
                                       size="4"),
                            rx.text("Distribuidora Avanzar",
                                    font_weight = "400"),
                            rx.text("En actividad",
                                    font_weight = "200"),
                           
                           margin_top = "3%",
                           align="center"
                    ),
                            
                            margin_top = "2%",
                            value="Work",
                            
                    ),
                
                default_value="Edu",
                margin_top = "5%",
                justify="center",
            
        ),
        
        
        
        width = "100%",
        align="center",
        margin_top = "5%",
        id = "XP"
    )