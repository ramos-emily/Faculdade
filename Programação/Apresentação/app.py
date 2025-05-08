from shiny import App, ui
from pages.quiz import get_page_quiz
from server import server 

app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav_panel("Quiz", get_page_quiz()),
    )
)

app = App(app_ui, server)
