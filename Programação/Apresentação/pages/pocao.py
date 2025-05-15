from shiny import ui

def get_page_pocao():
    return (
        ui.h3("Crie sua Poção Mágica!"),
        ui.input_checkbox_group(
            "ingredientes_pocao",
            "Escolha os ingredientes:",
            choices=["Olhos de sapo", "Pelos de ogro", "Essência de cebola", "Lágrimas de dragão"]
        ),
        ui.output_text("efeito_pocao")
    )
