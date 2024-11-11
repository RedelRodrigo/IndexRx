import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        
        rx.heading("Rodrigo",
                   size="8",
                   font_weight="700",
                   color="white",
                   opacity = 0.8,
                   margin_top = "40px"),
        
        rx.text("Full Stack developer",
                color = "white",
                opacity = 0.8,),
        
        rx.text("© Rodrigo All right reserved",
                color = "white",
                size="1",
                opacity = 0.8,),
        
        rx.image(src="logo.png",
                 height = "200px",
                 opacity = 0.3,
                 position = "absolute"
                 
                 ),
        
        
        width = "100%",
        height = "200px",
        bg_color = "#7c2f9d",
        margin_y = "2%",
        align="center",
        
    )