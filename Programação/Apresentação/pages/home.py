from shiny import ui
from pathlib import Path

def card(titulo, descricao, botao_id):
    return ui.tags.div(
        ui.h3(titulo),
        ui.p(descricao),
        ui.tags.button(
            f"Ir para {titulo}",
            id=botao_id,
            style=(
                "background:#6b8e23; color:white; border:none; padding:10px 15px; "
                "border-radius:5px; cursor:pointer;"
            )
        ),
        style=(
            "background:#f0f0f0; border-radius:10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.15); "
            "width:220px; padding:20px; text-align:center;"
        )
    )

def get_page_home():
    return ui.page_fluid(
        ui.div(
            ui.tags.div(
                ui.img(
                    src=str(Path(__file__).parent / ".." / "www" / "Shrek.png"),
                    style="width:100%; max-height:300px; object-fit:cover; border-radius: 8px;"
                ),
                ui.h1(
                    "Bem-vindo ao Mundo do Shrek!",
                    style=(
                        "text-align:center; margin-top:10px; color: #2E8B57; "
                        "font-family: 'Comic Sans MS', cursive;"
                    )
                ),
            ),
            ui.tags.div(
                "Explore as aventuras, quizzes e mistérios do pântano com Shrek e seus amigos!",
                style=(
                    "background-color:#9acd32; color:white; padding:10px; text-align:center; "
                    "font-weight:bold; font-size:1.1em; border-radius: 5px; margin-top:15px;"
                )
            ),
            ui.tags.div(
                card("Quiz", "Descubra qual personagem do Shrek combina com você.", "btn_quiz"),
                card("Poção", "Experimente poções mágicas e veja o resultado.", "btn_pocao"),
                card("Cebola", "Descubra as camadas misteriosas do Shrek.", "btn_cebola"),
                card("Aventura", "Escolha seu caminho e receba sabedoria do Shrek.", "btn_aventura"),
                style="display:flex; justify-content:center; gap:20px; margin-top:30px; flex-wrap: wrap;"
            )
        )
    )
