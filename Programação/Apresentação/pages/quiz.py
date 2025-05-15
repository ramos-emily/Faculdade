from shiny import ui

def get_page_quiz():
    return (
        ui.h3("Quem é você no Shrek?"),
        ui.input_radio_buttons(
            "quiz_resposta",
            "Escolha seu personagem favorito:",
            choices=["Shrek", "Burro", "Fiona", "Dragão"]
        ),
        ui.output_text("resultado_quiz"),   #nome do personagem
        ui.output_image("image") 
    )