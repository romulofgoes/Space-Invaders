from PPlay.window import *
from PPlay.keyboard import Keyboard
from PPlay.gameimage import *
from PPlay.sprite import *
from tiros import *
from monstros import mat
from monstros import *
from random import randint

def game_loop():
    janela = Window(800, 600)  # Tamanho da janela
    background = GameImage("black_screen.jpg")
    nave = GameImage("nave.png")
    tiro = GameImage("tiro.png")  # imagem do tiro
    teclado = Keyboard()
    tempo_monstros = 0
    tempo = 0
    taxa_monstros = 300  # taxa de tempo mínimo para disparar novo tiro dos monstros
    taxa = 150  # taxa de tempo mínimo para disparar novo tiro do player
    tiros_list = list()  # lista para armazenar os tiros
    tiros_monstros_list = list()
    nave.x = janela.width/2-nave.width/2
    nave.y = 450
    cont = 0
    vidas = 3
    matriz_monstros(L, C, mat)
    while vidas:
        while True:
            janela.update()
            background.draw()
            nave.draw()
            vel = 400
            soma_tiros(tiros_list, vel, 1, janela)
            soma_tiros(tiros_monstros_list, vel, -1, janela)
            if tempo_monstros > taxa_monstros:
                tempo_monstros = 0
                i = randint(0, len(mat)-1)
                j = randint(0, len(mat[i])-1)
                tiros_monstros_list = lista_de_tiros_monstros(tiro, mat[i][j], tiros_monstros_list)

            if teclado.key_pressed("right") and nave.x < (janela.width - nave.width):
                nave.x += (vel*janela.delta_time())
            if teclado.key_pressed("left") and nave.x > 0:
                nave.x -= (vel*janela.delta_time())
            if teclado.key_pressed("space") and tempo > taxa:
                tempo = 0
                tiros_list = lista_de_tiros(tiro, nave.x, tiros_list)
                # tiros_list = lista_de_tiros(nave.x)
            # E depois o Sprite
            if tiros_list:
                if tiros_list[0].y > mat[0][0].y-mat[0][0].height:
                    colisao_monstro(tiros_list, mat)
            if tiros_monstros_list:
                if colisao_player(tiros_monstros_list, nave):
                    vidas -=1
                    tempo_regeneracao = 0 # tempo de regeneração do player depois de ataque, enquanto tiver vida
                    x = 1
                    break
                
            monstros_draw(mat, cont)
            cont += 1
            move_matriz(mat, janela)
            tempo += 1
            tempo_monstros+=1
            if mat:
                i = len(mat)
                if (mat[i-1][0].y > nave.y):
                    break

            if teclado.key_pressed("ESC"):
                break

            fps = 1/janela.delta_time()
            janela.draw_text(
                f"FPS {fps}", 2, 2, size=20, color=(255, 255, 255))
        while tempo_regeneracao<300:
            if x*1<tempo_regeneracao<30*x:
                background.draw()
                nave.draw()
                x+=2
            janela.update()
            tempo_regeneracao+=1

# PRINCIPAL
