from shiny import ui, render
from pathlib import Path

def get_page_quiz():
    return ui.page_fluid(
        ui.h3("Quem é você no Shrek?"),
        ui.input_radio_buttons(
            "quiz_resposta",
            "Escolha seu personagem favorito:",
            choices=["Shrek", "Burro", "Fiona", "Dragão"]
        ),
        ui.output_text("resultado_quiz"),
        ui.output_image("image"),
        ui.tags.button("Voltar para Home", id="btn_home_quiz", style="margin-top:20px;")
    )

def server_quiz(input, output, session):
    @output
    @render.text
    def resultado_quiz():
        resposta = input.quiz_resposta()
        if resposta:
            return f"Você escolheu: {resposta}!"
        return "Escolha uma opção acima."

    @output
    @render.image
    def image():
        resposta = input.quiz_resposta()
        base_path = Path(__file__).parent / ".." / "www"
        imagens = {
            "Shrek": base_path / "Shrek.png",
            "Burro": base_path / "Burro.png",
            "Fiona": base_path / "Fiona.png",
            "Dragão": base_path / "Dragao.png"
        }
        if resposta in imagens:
            return {"src": str(imagens[resposta]), "width": "300px"}
        return None
