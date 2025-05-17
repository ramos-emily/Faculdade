from shiny import ui
from pathlib import Path

def get_page_home():
    return ui.page_fluid(
        ui.h1(
            "Bem-vindos ao Mundo do Shrek!",
            style=(
                "text-align:center; margin-top:20px; color: #2E8B57; "
                "font-family: 'Comic Sans MS', cursive; font-size: 2.8em;"
            )
        ),

        ui.div(
            ui.output_image("image_banner"),
            style=(
                "width: 100%; max-width: 900px; margin: 20px auto 30px auto; "
                "height: 500px; overflow: hidden; border-radius: 12px; "
                "box-shadow: 0 4px 15px rgba(0,0,0,0.25);"
            )
        ),

ui.tags.section(
    ui.tags.div(
        ui.h2("Quem é você no Shrek?", id="sec_quiz", class_="section-title"),
        
        ui.input_radio_buttons(
            "lugar",
            "Qual lugar você prefere?",
            choices=["Pântano", "Castelo", "Floresta"]
        ),
        ui.input_radio_buttons(
            "problema",
            "Como você lida com problemas?",
            choices=["Fico calmo", "Falo muito", "Luto"]
        ),
        ui.input_radio_buttons(
            "hobby",
            "Qual seu hobby favorito?",
            choices=["Cantar", "Lutar", "Dormir"]
        ),

        ui.output_text("resultado_quiz"),
        ui.output_image("image")
    ),
    class_="section"
),


        ui.tags.section(
            ui.tags.div(
                ui.h2("Poção Mágica", id="sec_pocao", class_="section-title"),
                ui.input_checkbox_group(
                    "ingredientes_pocao",
                    "Escolha os ingredientes:",
                    choices=["Pelos de ogro", "Essência de cebola", "Lágrimas de dragão", "Olhos de sapo"]
                ),
                ui.output_text("efeito_pocao")
            ),
            class_="section"
        ),

        ui.tags.section(
            ui.tags.div(
                ui.h2("Descubra as Camadas do Shrek", id="sec_cebola", class_="section-title"),
                ui.input_slider(
                    "camadas",
                    "Quantas camadas você quer descascar?",
                    min=1,
                    max=5,
                    value=1
                ),
                ui.output_text("mensagem_cebola")
            ),
            class_="section"
        ),

        ui.tags.section(
            ui.tags.div(
                ui.h2("Aventura no Pântano", id="sec_aventura", class_="section-title"),
                ui.input_radio_buttons(
                    "caminho_escolha",
                    "Escolha seu caminho:",
                    choices=["Entrar no castelo", "Fugir para o pântano", "Pedir ajuda ao Burro"]
                ),
                ui.output_text("resultado_caminho")
            ),
            class_="section"
        ),

        # CSS embutido no final
        ui.tags.style("""
            body {
                background-color: #f0fff0;
                font-family: 'Comic Sans MS', cursive;
            }

            .section {
                background-color: #ffffff;
                border: 2px solid #2E8B57;
                border-radius: 12px;
                padding: 25px;
                margin: 20px auto;
                max-width: 850px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
            }

            .section-title {
                color: #2E8B57;
                font-size: 1.8em;
                margin-bottom: 15px;
            }

            label {
                font-weight: bold;
                color: #333;
            }

            input[type="radio"],
            input[type="checkbox"] {
                margin-right: 8px;
            }
        """)
    )
