import reflex as rx

def contacto() -> rx.Component:
    return rx.vstack(
         
        rx.heading("Contacto",
                   size="8",
                   font_weight="500"),
         
        rx.desktop_only(
            
            rx.hstack(
                rx.hstack(
                    rx.icon("phone",
                        size=30,
                        margin_top = "15px"),
                    rx.vstack(
                        rx.text("Teléfono"),
                        rx.text("+54 2932-530877 ", font_weight = "300")
                    ),
                    ),
                
                rx.hstack(
                    rx.icon("mail",
                        size=30,
                        margin_top = "15px"),
                    rx.vstack(
                        rx.text("Email"),
                        rx.text("RedelRodrigoA@gmail.com", font_weight = "300")
                    ),
                    ),
                
                rx.hstack(
                    rx.icon("map-pinned",
                        size=30,
                        margin_top = "15px"),
                    rx.vstack(
                        rx.text("Ubicación"),
                        rx.text("Punta Alta, Bs As, Arg", font_weight = "300")
                    ),
                    ),
             
                width = "70vw",
                wrap="wrap",
                justify="between",
                margin_top = "3%"
                
            )),
        
        
        rx.mobile_and_tablet(
            rx.vstack(
                
                rx.hstack(
                    rx.icon("phone",
                        size=30,
                        margin_top = "15px"),
                    rx.vstack(
                        rx.text("Teléfono"),
                        rx.text("+54 2932-530877 ", font_weight = "300")
                    )),
                
                rx.hstack(
                    rx.icon("mail",
                        size=30,
                        margin_top = "15px"),
                    rx.vstack(
                        rx.text("Email"),
                        rx.text("RedelRodrigoA@gmail.com", font_weight = "300")
                    )),
                
                 rx.hstack(
                    rx.icon("map-pinned",
                        size=30,
                        margin_top = "15px"),
                    rx.vstack(
                        rx.text("Ubicación"),
                        rx.text("Punta Alta, Bs As, Arg", font_weight = "300")
                    )))),
        
         width = "100%",
         align="center",
         margin_top = "5%",
         id = "Contacto"
    )