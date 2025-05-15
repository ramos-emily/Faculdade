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
        


    @output
    @render.text
    def efeito_pocao():
        ingredientes = input.ingredientes_pocao()

        if not ingredientes:
            return "Escolha ao menos um ingrediente."

        if "Pelos de ogro" in ingredientes and "Essência de cebola" in ingredientes:
            return "🧅💪 Você criou uma Poção de Força Bruta com cheiro duvidoso!"
        elif "Lágrimas de dragão" in ingredientes:
            return "🔥 Você criou uma Poção de Fogo!"
        elif "Olhos de sapo" in ingredientes:
            return "👁️ Você criou uma Poção de Visão Noturna!"
        else:
            return "✨ Você criou uma poção mágica misteriosa!"
        


    @output
    @render.text
    def mensagem_cebola():
        camada = input.camadas()
        mensagens = {
            1: "Você arranhou a superfície... ogros são mais profundos que isso.",
            2: "Hmm, já tá ficando pessoal.",
            3: "Começou a chorar? Ogros são complexos!",
            4: "Camada após camada... ainda não chegou no coração.",
            5: "Parabéns! Você entendeu o Shrek: ogros têm sentimentos também."
        }
        return mensagens.get(camada, "Descasque mais para entender.")



    