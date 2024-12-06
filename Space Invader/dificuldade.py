from PPlay.window import Window
from PPlay.keyboard import Keyboard

# SUBPROGRAMA
def dificuldade():
    while True:
        janela.update()
        janela.set_background_color((50, 50, 50))
        janela.draw_text("Escolha a dificuldade - Pressione ESC para voltar", 150, 100, size=20, color=(255, 255, 255))
        janela.draw_text("Fácil", 350, 200, size=20, color=(255, 255, 255))
        janela.draw_text("Médio", 350, 250, size=20, color=(255, 255, 255))
        janela.draw_text("Difícil", 350, 300, size=20, color=(255, 255, 255))
        if teclado.key_pressed("ESC"):
            break


# PROGRAMA PRINCIPAL
janela = Window(800, 600)  # Tamanho da janela
teclado = Keyboard()
