from PPlay.window import *
from PPlay.keyboard import Keyboard
from PPlay.gameimage import *
from PPlay.sprite import *


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


def colisao(tiros_list, monster_list):
    sinal_i = 0
    sinal_j = 0
    x = int()
    sinal = 0
    for i in range(len(tiros_list)):
        if sinal_i:
            break
        for j in range(len(monster_list)):
            if sinal_j:
                break
            for k in range(len(monster_list[j])):
                if (monster_list[j][k].x+monster_list[j][k].width > tiros_list[i].x > monster_list[j][k].x-monster_list[j][k].width) and\
                        (monster_list[j][k].y+monster_list[j][k].height > tiros_list[i].y > monster_list[j][k].y-monster_list[j][k].height):
                    monster_list[j].pop(k)
                    sinal = 1
                    x = i
                    sinal_i = 1
                    sinal_j = 1
                    if not monster_list[j]:
                        monster_list.pop(j)
                    break
    if sinal:
        tiros_list.pop(x)
