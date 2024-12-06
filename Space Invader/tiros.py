from PPlay.window import *
from PPlay.keyboard import Keyboard
from PPlay.gameimage import *


def lista_de_tiros(tiro, nave_pos, tiros_list):  # atualiza lista de tiros
    nova_lista = tiros_list
    tiro_novo = GameImage("tiro.png")
    tiro_novo.x = nave_pos+35
    tiro_novo.y = 415
    nova_lista.append(tiro_novo)
    return nova_lista

# atualiza a posição dos tiros e apaga os tiros fora da janela


def soma_tiros(tiros_list, vel, janela):
    if len(tiros_list) > 0 and tiros_list[0].y > janela.height:
        tiros_list.pop(0)
    for i in range(len(tiros_list)):
        tiros_list[i].y -= (0.5)
        tiros_list[i].draw()
