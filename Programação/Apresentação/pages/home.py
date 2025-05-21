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
                
                ui.div(
                    ui.div(
                        id="progress-bar",
                        style=(
                            "height: 6px; background-color: #2E8B57; "
                            "width: 33%; border-radius: 3px;"
                        )
                    ),
                    style=(
                        "background-color: #f0f0f0; border-radius: 3px; "
                        "margin-bottom: 20px;"
                    )
                ),
                
                ui.div(
                    ui.div(
                        ui.div(
                            ui.input_radio_buttons(
                                "lugar",
                                "1. Qual lugar você prefere?",
                                choices=["Pântano", "Castelo", "Floresta"],
                            ),
                            style="font-size: 1.1em;",
                            id="pergunta1",
                        ),
                        ui.div(
                            ui.input_radio_buttons(
                                "problema",
                                "2. Como você lida com problemas?",
                                choices=["Fico calmo", "Falo muito", "Luto"],
                            ),
                            style="font-size: 1.1em; display: none;",
                            id="pergunta2",
                        ),
                        ui.div(
                            ui.input_radio_buttons(
                                "hobby",
                                "3. Qual seu hobby favorito?",
                                choices=["Cantar", "Lutar", "Dormir"],
                            ),
                            style="font-size: 1.1em; display: none;",
                            id="pergunta3",
                        ),
                        ui.div(
                            ui.tags.button(
                                ui.tags.i(class_="fas fa-arrow-left"),
                                " Anterior",
                                id="btn_anterior",
                                class_="btn btn-default",
                                style="margin-right: 10px; display: none;",
                            ),
                            ui.tags.button(
                                "Próximo ",
                                ui.tags.i(class_="fas fa-arrow-right"),
                                id="btn_proximo",
                                class_="btn btn-primary",
                            ),
                            style="text-align: center; margin-top: 20px;",
                        ),
                        id="quiz_container",
                    ),
                    
                    ui.div(
                        ui.output_text("resultado_quiz"),
                        ui.div(
                            ui.output_image("image"),
                            style=(
                                "margin: 20px auto; text-align: center; min-height: 300px; "
                                "width: 300px; height: 300px; display: flex; align-items: center; "
                                "justify-content: center; overflow: hidden;"
                            )
                        ),
                        id="quiz_resultado",
                        style="display: none;",
                    ),
                ),
            ),
            class_="section",
        ),

        ui.tags.section(
            ui.tags.div(
                ui.h2("🧪 Poção Mágica", id="sec_pocao", class_="section-title"),
                ui.input_checkbox_group(
                    "ingredientes_pocao",
                    "Escolha os ingredientes para sua poção:",
                    choices=[
                        "Pelos de ogro",
                        "Essência de cebola",
                        "Lágrimas de dragão",
                        "Olhos de sapo",
                        "Unha de troll",
                        "Pó de fada",
                        "Olhos de morcego",
                    ],
                ),
                ui.div(
                    ui.output_text("efeito_pocao"),
                    class_="efeito-pocao-texto",
                ),
            ),
            class_="section",
        ),

        ui.tags.section(
            ui.tags.div(
                ui.h2("Descubra as Camadas do Shrek", id="sec_cebola", class_="section-title"),
                ui.input_slider(
                    "camadas",
                    "Quantas camadas você quer descascar?",
                    min=1,
                    max=5,
                    value=1,
                ),
                ui.output_text("mensagem_cebola"),
            ),
            class_="section",
        ),

        ui.tags.section(
            ui.tags.div(
                ui.h2("Aventura no Pântano", id="sec_aventura", class_="section-title"),
                ui.input_radio_buttons(
                    "caminho_escolha",
                    "Escolha seu caminho:",
                    choices=["Entrar no castelo", "Fugir para o pântano", "Pedir ajuda ao Burro"],
                ),
                ui.output_text("resultado_caminho"),
            ),
            class_="section",
        ),

        ui.tags.style("""
            #quiz_resultado img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                object-position: center;
            }
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

            /* Estilos para o quiz */
            .btn {
                padding: 8px 16px;
                border-radius: 20px;
                cursor: pointer;
                font-weight: bold;
                transition: all 0.3s;
                font-family: 'Comic Sans MS', cursive;
            }
            
            .btn-default {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
            }
            
            .btn-primary {
                background-color: #2E8B57;
                color: white;
                border: 1px solid #1E6B47;
            }
            
            .btn:hover {
                opacity: 0.9;
                transform: translateY(-2px);
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            }

            img[src$=".png"] {
                min-height: 300px;
                background-color: #f0f0f0;
                border-radius: 10px;
            }
           
            /* Ícones Font Awesome */
            .fa-arrow-left, .fa-arrow-right {
                margin: 0 5px;
            }
        """),

        # JavaScript para controlar o quiz
        ui.tags.script("""
            $(document).ready(function() {
                let currentQuestion = 1;
                const totalQuestions = 3;
                
                // Atualizar barra de progresso
                function updateProgress() {
                    const progress = (currentQuestion / totalQuestions) * 100;
                    $("#progress-bar").css("width", progress + "%");
                }
                
                // Mostrar próxima pergunta
                $("#btn_proximo").click(function() {
                    if (currentQuestion < totalQuestions) {
                        $("#pergunta" + currentQuestion).hide();
                        currentQuestion++;
                        $("#pergunta" + currentQuestion).show();
                        
                        // Atualizar navegação
                        $("#btn_anterior").show();
                        updateProgress();
                        
                        if (currentQuestion === totalQuestions) {
                            $("#btn_proximo").html("Ver Resultado <i class='fas fa-check'></i>");
                        }
                    } else {
                        $("#quiz_container").hide();
                        $("#quiz_resultado").show();
                        
                        // Força a atualização dos outputs
                        Shiny.setInputValue("mostrar_resultado", true, {priority: "event"});
                        setTimeout(function() {
                            Shiny.bindAll("#quiz_resultado");
                        }, 100);
                    }
                });
                
                // Mostrar pergunta anterior
                $("#btn_anterior").click(function() {
                    if (currentQuestion > 1) {
                        $("#pergunta" + currentQuestion).hide();
                        currentQuestion--;
                        $("#pergunta" + currentQuestion).show();
                        
                        // Atualizar navegação
                        $("#btn_proximo").html("Próximo <i class='fas fa-arrow-right'></i>");
                        updateProgress();
                        
                        if (currentQuestion === 1) {
                            $("#btn_anterior").hide();
                        }
                    }
                });
            });
        """),
        ui.tags.link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
        ),
    )
