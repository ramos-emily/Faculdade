from shiny import App, ui
from pages.quiz import get_page_quiz
from pages.pocao import get_page_pocao
from pages.aventura import get_page_aventura
from pages.cebola import get_page_cebola
from server import server 

app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav_panel("Quiz", get_page_quiz()),
        ui.nav_panel("Poção Mágica", get_page_pocao()),
        ui.nav_panel("cebola", get_page_cebola()),
        ui.nav_panel("Aventura", get_page_aventura()),
    )
)

app = App(app_ui, server)
