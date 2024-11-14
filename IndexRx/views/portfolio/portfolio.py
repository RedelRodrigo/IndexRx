import reflex as rx



def portfolio() -> rx.Component:
    return rx.vstack(
        
        rx.heading("Portfolio",
                   font_weight = "500",
                   size="8"),
        
        rx.text("Repositorios en GitHub de algunos de mis trabajos",
                font_weight = "200",
                margin_top = "3%",
                font_size = "1.5rem",
                align="center"),
        
        rx.link(rx.image(src="/github.png",
                        width = 210,
                        height = "auto",
                        border_radius = "100%",
                        
                        ),
                
                href="https://github.com/RedelRodrigo?tab=repositories",
                margin_top = "3%",
                is_external=True
                
                
                ),
        
        width = "100%",
        align="center",
        margin_top = "5%",
        id="Portfolio"
    )