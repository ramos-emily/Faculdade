from shiny import render, ui
from pathlib import Path

def server(input, output, session):
    
    @output
    @render.text
    def resultado_quiz():
        resposta = input.quiz_resposta()
        if resposta:
            return f"Você escolheu: {resposta}!"
        return "Escolha uma opção acima."

    # @output
    # @render.ui
    # def imagem_quiz():
    #     resposta = input.quiz_resposta()
    #     if resposta == "Shrek":
            
    #         return ui.output_image("image")
    #     elif resposta == "Burro":
    #         return ui.img(src="burro.png", width="300px")
    #     elif resposta == "Fiona":
    #         return ui.img(src="fiona.png", width="300px")
    #     elif resposta == "Dragão":
    #         return ui.img(src="dragao.png", width="300px")
    #     else:
    #         return ui.p("Escolha seu personagem para ver a imagem.")

    @output
    @render.image
    def image():
        resposta = input.quiz_resposta()
        if resposta == "Shrek":
            return {"src": str(Path(__file__).parent) + "\www\Shrek.png", "width":"300px"}
        elif resposta == "Burro":
            return {"src": str(Path(__file__).parent) + "\www\Burro.png", "width":"300px"}
        elif resposta == "Fiona":
            return {"src": str(Path(__file__).parent) + "\www\Fiona.png", "width":"300px"}
        elif resposta == "Dragão":
            return {"src": str(Path(__file__).parent) + "\www\Dragao.png", "width":"300px"}
        else:
            return ui.p("Escolha seu personagem para ver a imagem.")

    