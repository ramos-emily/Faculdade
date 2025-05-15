from shiny import ui

def get_page_cebola():
    return (
        ui.h3("🧅 Camadas do Ogro"),
        ui.input_slider(
            "camadas", 
            "Quantas camadas você quer descascar?", 
            min=1, max=5, value=1
        ),
        ui.output_text("mensagem_cebola")
    )
