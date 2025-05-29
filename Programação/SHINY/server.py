import random
from shiny import render, reactive
from pathlib import Path

personagens = ["Shrek", "Burro", "Fiona", "Dragão"]

pontuacoes = {
    "lugar": {
        "Pântano": {"Shrek": 2, "Burro": 1, "Fiona": 0, "Dragão": 0},
        "Castelo": {"Shrek": 0, "Burro": 0, "Fiona": 1, "Dragão": 2},
        "Floresta": {"Shrek": 0, "Burro": 1, "Fiona": 2, "Dragão": 1},
    },
    "problema": {
        "Fico calmo": {"Shrek": 2, "Burro": 0, "Fiona": 1, "Dragão": 0},
        "Falo muito": {"Shrek": 0, "Burro": 3, "Fiona": 0, "Dragão": 0},
        "Luto": {"Shrek": 1, "Burro": 0, "Fiona": 2, "Dragão": 2},
    },
    "hobby": {
        "Cantar": {"Shrek": 0, "Burro": 3, "Fiona": 1, "Dragão": 0},
        "Lutar": {"Shrek": 1, "Burro": 0, "Fiona": 2, "Dragão": 3},
        "Dormir": {"Shrek": 2, "Burro": 0, "Fiona": 0, "Dragão": 0},
    }
}

def server(input, output, session):
    @output
    @render.text
    def resultado_quiz():
        if not input.mostrar_resultado():
            return ""
        lugar = input.lugar()
        problema = input.problema()
        hobby = input.hobby()
        if not lugar or not problema or not hobby:
            return "Por favor, responda todas as perguntas."
        pontos = {p: 0 for p in personagens}
        for p in personagens:
            pontos[p] += pontuacoes["lugar"][lugar].get(p, 0)
            pontos[p] += pontuacoes["problema"][problema].get(p, 0)
            pontos[p] += pontuacoes["hobby"][hobby].get(p, 0)
        personagem = max(pontos, key=pontos.get)
        mensagens = {
            "Shrek": "Você é o Shrek! Camadas, coragem e um coração gigante.",
            "Burro": "Você é o Burro! Falante, leal e impossível de ignorar.",
            "Fiona": "Você é a Fiona! Forte, determinada e cheia de surpresas.",
            "Dragão": "Você é a Dragão! Feroz por fora, apaixonada por dentro."
        }
        return mensagens.get(personagem, "Personagem não identificado")

    @output
    @render.image
    def image():        
        lugar = input.lugar()
        problema = input.problema()
        hobby = input.hobby()
        pontos = {p: 0 for p in personagens}
        for p in personagens:
            pontos[p] += pontuacoes["lugar"][lugar].get(p, 0)
            pontos[p] += pontuacoes["problema"][problema].get(p, 0)
            pontos[p] += pontuacoes["hobby"][hobby].get(p, 0)
        personagem = max(pontos, key=pontos.get)
        imagens = {
            "Shrek": "Shrek.png",
            "Burro": "Burro.png", 
            "Fiona": "Fiona.png",
            "Dragão": "Dragão.png"
        }
        img_path = Path(__file__).parent / "www" / imagens[personagem]
        if img_path.exists():
            return {"src": str(img_path), "width": "300px", "alt": personagem}
        else:
            return None

    @output
    @render.text
    def efeito_pocao():
        ingredientes = input.ingredientes_pocao()
        if not ingredientes:
            return "🧪 O caldeirão está vazio! Escolha ao menos um ingrediente para começar a mistura."

        # Ajusta nomes caso inclua emoji nos ingredientes (limpeza)
        ingredientes_puros = [i.split(" ", 1)[-1] if " " in i else i for i in ingredientes]
        ingredientes_set = set(ingredientes_puros)

        texto_base = "✨ mexendo... ✨\n\n"

        if {"Pelos de ogro", "Essência de cebola"} <= ingredientes_set:
            return texto_base + "💪 Você criou uma *Poção de Força Bruta* com um aroma de fazer ogros desmaiarem!"
        elif {"Lágrimas de dragão", "Olhos de morcego"} <= ingredientes_set:
            return texto_base + "🔥 Você criou uma *Poção de Fogo Noturno*! Ela arde tanto quanto ilumina!"
        elif {"Pó de fada", "Lágrimas de dragão"} <= ingredientes_set:
            return texto_base + "🪄 Você criou uma *Poção de Voo*! Segure firme para não voar até a lua!"
        elif {"Unha de troll", "Essência de cebola"} <= ingredientes_set:
            return texto_base + "🤢 Você criou uma *Poção de Fedor Imortal*! Vai espantar até as baratas do castelo."
        elif "Olhos de sapo" in ingredientes_set:
            return texto_base + "🌙 Você criou uma *Poção de Visão Noturna*! Seus olhos brilham como faróis no breu!"
        elif "Pó de fada" in ingredientes_set:
            return texto_base + "🌟 Você criou uma *Poção de Encantamento*! Suas palavras agora hipnotizam qualquer um."
        else:
            efeitos_misteriosos = [
                "🌀 Você criou uma *Poção do Caos*! Coisas estranhas estão prestes a acontecer...",
                "🔮 Você criou uma *Poção da Transformação*! Se prepare para se tornar algo... inesperado.",
                "🌈 Você criou uma *Poção Arco-Íris*! Cuidado: ela traz felicidade (e confusão) em doses iguais.",
                "🎭 Você criou uma *Poção das Máscaras*! Cada gole revela uma nova personalidade.",
                "⚡ Você criou uma *Poção da Tempestade*! Raios e trovões vão seguir seus passos!"
            ]
            return texto_base + random.choice(efeitos_misteriosos)

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
        frase = random.choice(frases)
        return frase

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
        banner_path = Path(__file__).parent / "www" / "Banner.png"
        if banner_path.exists():
            return {"src": str(banner_path), "width": "100%", "height": "500px"}
        return None
