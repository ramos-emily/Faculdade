from shiny import App, ui, render

def server(input, output, session):
    @output
    @render.text
    def texto():
        return "Teste reload! Mude esse texto e salve para ver se atualiza."

app_ui = ui.page_fluid(
    ui.output_text("texto")
)

app = App(app_ui, server)
