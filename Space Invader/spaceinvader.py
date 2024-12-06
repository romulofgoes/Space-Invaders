from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.mouse import Mouse
from PPlay.keyboard import Keyboard
from game_loop import *
from dificuldade import *
from ranking import *

# Configurações iniciais
janela = Window(800, 600)  # Tamanho da janela
janela.set_title("Menu Gráfico")
background = GameImage("black_screen.jpg")
mouse = Mouse()
teclado = Keyboard()

# Definição das áreas clicáveis (x, y, largura, altura)
area_jogar = (300, 150, 200, 50)
area_dificuldade = (300, 250, 200, 50)
area_ranking = (300, 350, 200, 50)
area_sair = (300, 450, 200, 50)

# Loop principal
while True:
    janela.update()
    background.draw()
    # Desenhar as áreas como caixas
    janela.draw_text(
        "JOGAR", area_jogar[0] + 50, area_jogar[1] + 10, size=20, color=(255, 255, 255))
    janela.draw_text(
        "DIFICULDADE", area_dificuldade[0] + 20, area_dificuldade[1] + 10, size=20, color=(255, 255, 255))
    janela.draw_text(
        "RANKING", area_ranking[0] + 50, area_ranking[1] + 10, size=20, color=(255, 255, 255))
    janela.draw_text(
        "SAIR", area_sair[0] + 80, area_sair[1] + 10, size=20, color=(255, 255, 255))

    # Verificar cliques do mouse dentro das áreas
    if mouse.is_button_pressed(1):
        if area_jogar[0] <= mouse.get_position()[0] <= area_jogar[0] + area_jogar[2] and \
           area_jogar[1] <= mouse.get_position()[1] <= area_jogar[1] + area_jogar[3]:
            game_loop()
        elif area_dificuldade[0] <= mouse.get_position()[0] <= area_dificuldade[0] + area_dificuldade[2] and \
                area_dificuldade[1] <= mouse.get_position()[1] <= area_dificuldade[1] + area_dificuldade[3]:
            dificuldade()
        elif area_ranking[0] <= mouse.get_position()[0] <= area_ranking[0] + area_ranking[2] and \
                area_ranking[1] <= mouse.get_position()[1] <= area_ranking[1] + area_ranking[3]:
            ranking()
        elif area_sair[0] <= mouse.get_position()[0] <= area_sair[0] + area_sair[2] and \
                area_sair[1] <= mouse.get_position()[1] <= area_sair[1] + area_sair[3]:
            janela.close()
