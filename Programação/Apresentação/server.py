import random
from shiny import render, reactive
from pathlib import Path

personagens = ["Shrek", "Burro", "Fiona", "Dragão"]

# Pontuação para cada resposta por pergunta
pontuacoes = {
    "lugar": {
        "Pântano": {"Shrek": 2, "Burro": 1, "Fiona": 0, "Dragão": 0},
        "Castelo": {"Shrek": 0, "Burro": 0, "Fiona": 1, "Dragão": 2},
        "Floresta": {"Shrek": 0, "Burro": 1, "Fiona": 2, "Dragão": 1},
    },
    "problema": {
        "Fico calmo": {"Shrek": 2, "Burro": 0, "Fiona": 1, "Dragão": 0},
        "Falo muito": {"Shrek": 0, "Burro": 3, "Fiona": 0, "Dragão": 0},
        "Luto": {"Shrek": 1, "Burro": 0, "Fiona": 3, "Dragão": 1},
    },
    "hobby": {
        "Cantar": {"Shrek": 0, "Burro": 3, "Fiona": 1, "Dragão": 0},
        "Lutar": {"Shrek": 1, "Burro": 0, "Fiona": 2, "Dragão": 1},
        "Dormir": {"Shrek": 2, "Burro": 0, "Fiona": 0, "Dragão": 0},
    }
}

def server(input, output, session):

    @output
    @render.text
    def resultado_quiz():
        lugar = input.lugar()
        problema = input.problema()
        hobby = input.hobby()

        # Se alguma pergunta não respondida
        if not lugar or not problema or not hobby:
            return "Responda todas as perguntas para descobrir seu personagem."

        # Calcula pontos por personagem
        pontos = {p: 0 for p in personagens}

        for p in personagens:
            pontos[p] += pontuacoes["lugar"][lugar].get(p, 0)
            pontos[p] += pontuacoes["problema"][problema].get(p, 0)
            pontos[p] += pontuacoes["hobby"][hobby].get(p, 0)

        # Personagem com maior pontuação
        personagem = max(pontos, key=pontos.get)

        mensagens = {
            "Shrek": "Você é o Shrek! Camadas, coragem e um coração gigante.",
            "Burro": "Você é o Burro! Falante, leal e impossível de ignorar.",
            "Fiona": "Você é a Fiona! Forte, determinada e cheia de surpresas.",
            "Dragão": "Você é a Dragão! Feroz por fora, apaixonada por dentro."
        }

        return f"{mensagens[personagem]}"

    @output
    @render.image
    def image():
        personagem = None
        lugar = input.lugar()
        problema = input.problema()
        hobby = input.hobby()
        if lugar and problema and hobby:
            pontos = {p: 0 for p in personagens}
            for p in personagens:
                pontos[p] += pontuacoes["lugar"][lugar].get(p, 0)
                pontos[p] += pontuacoes["problema"][problema].get(p, 0)
                pontos[p] += pontuacoes["hobby"][hobby].get(p, 0)
            personagem = max(pontos, key=pontos.get)

        base = Path(__file__).parent / "www"
        imagens = {
            "Shrek": "Shrek.png",
            "Burro": "Burro.png",
            "Fiona": "Fiona.png",
            "Dragão": "Dragao.png"
        }
        if personagem in imagens:
            return {"src": str(base / imagens[personagem]), "width": "300px"}
        return {}

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
    def image_banner():
        base = Path(__file__).parent / "www"
        return {"src": str(base / "Banner.png"),"width": "100%", "height": "500px"}
