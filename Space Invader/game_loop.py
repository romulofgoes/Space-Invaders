from PPlay.window import *
from PPlay.keyboard import Keyboard
from PPlay.gameimage import *
from PPlay.sprite import *
from tiros import lista_de_tiros, soma_tiros
from monstros import mat
from monstros import *



def game_loop():
    janela = Window(800, 600)  # Tamanho da janela
    background = GameImage("black_screen.jpg")
    nave = GameImage("nave.png")
    tiro = GameImage("tiro.png")  # imagem do tiro
    teclado = Keyboard()
    tempo = 0
    taxa = 200  # taxa de tempo mínimo para disparar novo tiro
    tiros_list = list()  # lista para armazenar os tiros
    nave.x = janela.width/2-nave.width/2
    nave.y = 450
    cont = 0
    matriz_monstros(L, C, mat)
    while True:
        janela.update()
        background.draw()
        nave.draw()
        vel = 400
        soma_tiros(tiros_list, vel, janela)
        if teclado.key_pressed("right") and nave.x < (janela.width - nave.width):
            nave.x += (vel*janela.delta_time())
        if teclado.key_pressed("left") and nave.x > 0:
            nave.x -= (vel*janela.delta_time())
        if teclado.key_pressed("space") and tempo > taxa:
            tempo = 0
            tiros_list = lista_de_tiros(tiro, nave.x, tiros_list)
            # tiros_list = lista_de_tiros(nave.x)
        # E depois o Sprite
        monstros_draw(L, C, mat, cont)
        cont+=1
        move_matriz(L, C, mat, janela)
        tempo+=1
        if (mat[L-1][0].y > nave.y):
            break

        if teclado.key_pressed("ESC"):
            break

        fps = 1/janela.delta_time()
        janela.draw_text(
            f"FPS {fps}",2, 2, size=20, color=(255, 255, 255))
        
# PRINCIPAL
