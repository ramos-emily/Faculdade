import random
from shiny import render, ui, reactive
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
            return "Você criou uma Poção de Força Bruta com cheiro duvidoso!"
        elif "Lágrimas de dragão" in ingredientes:
            return "Você criou uma Poção de Fogo!"
        elif "Olhos de sapo" in ingredientes:
            return "Você criou uma Poção de Visão Noturna!"
        else:
            return "Você criou uma poção mágica misteriosa!"
        


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
    
    @output
    @render.text
    def resultado_caminho():
        escolha = input.caminho_escolha()
        if escolha == "Entrar no castelo":
            return "Você entrou e... encontrou o Lord Farquaad!"
        elif escolha == "Fugir para o pântano":
            return "Você está seguro... mas coberto de lama!"
        elif escolha == "Pedir ajuda ao Burro":
            return "Burro chegou... e começou a cantar!"
        return "Faça sua escolha acima."

    frases = [
        "Cebolas têm camadas!",
        "É melhor pra todo mundo se você for embora!",
        "Isso não é um conto de fadas!",
        "O que tá fazendo no meu pântano?!",
        "Burro... CAAAAALA a boca!"
    ]

    @output
    @render.text
    @reactive.event(input.botao_frase)
    def sabedoria_shrek():
        return random.choice(frases)    
    
    @reactive.Effect
    def _():
        if input.btn_quiz():
            session.set_input("navset_tab", "Quiz")
        elif input.btn_pocao():
            session.set_input("navset_tab", "Poção")
        elif input.btn_cebola():
            session.set_input("navset_tab", "Cebola")
        elif input.btn_aventura():
            session.set_input("navset_tab", "Aventura")

    
    @output
    @render.image
    def banner_img():
        return {
            "src": str(Path(__file__).parent / "www" / "shrek.png"),
            "width": "100%",
            "style": "max-height:300px; object-fit:cover; border-radius:8px;"
        }



    