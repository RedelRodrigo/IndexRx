import reflex as rx
    
    

def navbar() -> rx.Component:
    return rx.stack(
        rx.desktop_only(
            rx.stack(
            
            rx.text("Rodrigo"),
            
            rx.spacer(),
            
            rx.link(
                rx.button("Inicio",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",
                          color_scheme="purple"
                          ),
                href="#",
                margin_x = "7px",
                
            ),
            rx.link(
                rx.button("Sobre mi",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",
                          color_scheme="purple"),
                href="#Sobre_mi",
                margin_x = "7px"
            ),
            rx.link(
                rx.button("Skills",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",
                          color_scheme="purple"),
                href="#Skills",
                margin_x = "7px"
            ),
            rx.link(
                rx.button("Experiencia",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",
                          color_scheme="purple"),
                href="#XP",
                margin_x = "7px"
            ),
            rx.link(
                rx.button("Portfolio",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",
                          color_scheme="purple"),
                href="#Portfolio",
                margin_x = "7px"
            ),
            rx.link(
                rx.button("Contacto",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",
                          color_scheme="purple"),
                href="#Contacto",
                margin_x = "7px"
            ),
            
            rx.spacer(),

            rx.color_mode.button(),
            
            width = "100vw",
            height = "50px",
            justify = "center",
            padding_y = "1%",
            padding_x = "2%",
            position = "fixed",
            bg_color=rx.color_mode_cond(light="#f9f9f9",
                                            dark="#221f25"),
            z_index = "999",
            id="Inicio",
        )),
            
        rx.mobile_and_tablet(
            rx.hstack(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu"),),
                rx.menu.content(
                    
                rx.menu.item(
                    
                    rx.link(
                rx.button("Inicio",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",
                          ),
                href="#",
                margin_x = "7px",
                
            ),
                    color_scheme="purple",
                ),
                rx.menu.item(
                    
                    rx.link(
                rx.button("Sobre mi",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",),
                href="#Sobre_mi",
                margin_x = "7px"
            ),
                    
                    color_scheme="purple",
                ),
                rx.menu.item(
                    
                    rx.link(
                rx.button("Skills",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",),
                href="#Skills",
                margin_x = "7px"
            ),
                    color_scheme="purple",
                ),
                rx.menu.item(
                    
                    rx.link(
                rx.button("Experiencia",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",),
                href="#XP",
                margin_x = "7px"
            ),
                    color_scheme="purple",
                ),
                rx.menu.item(
                    
                    rx.link(
                rx.button("Portfolio",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",),
                
                href="#Portfolio",
                margin_x = "7px"
            ),
                    color_scheme="purple",
                ),
                rx.menu.item(
                    
                    rx.link(
                rx.button("Contacto",
                          color=rx.color_mode_cond(light="black", dark="white"),
                          variant="ghost",),
                href="#Contacto",
                margin_x = "7px"
            ),
                    color_scheme="purple"
                    ))),
                      
                rx.spacer(),
                      
                rx.color_mode.button(),
                
                
            width = "100vw",
            justify = "center",
            padding_y = "1%",
            padding_x = "2%",
            position = "fixed",
            z_index = "999",
            id="Inicio",
                      ))
    )