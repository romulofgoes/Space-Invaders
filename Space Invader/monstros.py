from PPlay.sprite import *
from PPlay.window import *

direcion = 1
mat = list()
cont = 0
vel_x = 1 # velocidade horizontal
vel_y = 15 # velocidade vertical
def matriz_monstros(linhas, colunas, matriz): # Cria nova matriz
    for i in range(linhas):
        lista_aux = list()
        for j in range(colunas):
            monstro = Sprite("monster.png")
            lista_aux.append(monstro)
        matriz.append(lista_aux)


def monstros_draw(linhas, colunas, matriz, controle=1):  # mostra os monstros na tela
    y = 0
    for i in range(linhas):
        x = 0
        for j in range(colunas):
            if controle == 0:
                matriz[i][j].set_position(x, y)
            x += matriz[i][j].width + matriz[i][j].width/2
            matriz[i][j].draw()
        y += matriz[i][j].height + matriz[i][j].height/2    



def move_matriz(linhas, colunas, matriz, janela):
    x = int()
    global direcion, vel_y, vel_x
    if matriz[0][C-1].x > (janela.width - matriz[0][C-1].width) or matriz[0][0].x < 0:
        direcion*=-1
        x = 1
    for i in range(linhas):
        for j in range(colunas):
            # move a monstro 1 pixels por frame sobre X
            matriz[i][j].x += vel_x*direcion
            if x:
                matriz[i][j].y+=vel_y


L = 4
C = 6

if L<=3 or C<=5: # Erro pois L não pode ser menor que 3 e C não pode ser menor que 5
    raise Exception("L deve ser maior que 3 e C deve ser maior que 5.")

