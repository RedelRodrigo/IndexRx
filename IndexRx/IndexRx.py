import reflex as rx
import rxconfig

#styles:
from IndexRx.styles.general import style

#components:
from IndexRx.components.navbar import navbar
from IndexRx.views.header.headers import headers
from IndexRx.views.about.about import about
from IndexRx.views.skills.skills import skills
from IndexRx.views.XP.xp import exp
from IndexRx.views.portfolio.portfolio import portfolio
from IndexRx.views.contacto.contacto import contacto
from IndexRx.views.footer.footer import footer



class State(rx.State):
    pass


@rx.page(route="/", title="Redel Rodrigo - Reflex")
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        headers(),
        about(),
        skills(),
        exp(),
        portfolio(),
        contacto(),
        footer(),
        
        
        bg_color=rx.color_mode_cond(light="#f9f9f9",
                                            dark="#221f25"),
    )



app = rx.App(style=style,
             
            
            
            stylesheets=["https://fonts.googleapis.com/css2?family=Sacramento&display=swap",
                         "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"]
            )
app.add_page(index)