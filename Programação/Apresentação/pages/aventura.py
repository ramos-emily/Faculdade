from shiny import ui

def get_page_aventura():
    return ui.div(
        ui.h3("Escolha seu Caminho na Aventura!"),

        ui.input_radio_buttons(
            "caminho_escolha",
            "Você encontrou um castelo. O que deseja fazer?",
            choices=[
                "Entrar no castelo",
                "Fugir para o pântano",
                "Pedir ajuda ao Burro"
            ]
        ),
        ui.output_text("resultado_caminho"),

        ui.hr(),
        ui.h3("Receba uma Sabedoria do Shrek"),
        ui.input_action_button("botao_frase", "Receber Sabedoria Ogra"),
        ui.output_text("sabedoria_shrek")
    )
