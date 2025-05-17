# app.py
from shiny import App
from pages.home import get_page_home
from server import server

app_ui = get_page_home()

app = App(app_ui, server)
