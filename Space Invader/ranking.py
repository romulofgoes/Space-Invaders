from PPlay.window import Window
from PPlay.keyboard import Keyboard

# SUBPROGRAMA
def ranking():
    while True:
        janela.update()
        janela.set_background_color((70, 70, 70))
        janela.draw_text("Pressione ESC para voltar", 250, 300, size=30, color=(255, 255, 255))
        if teclado.key_pressed("ESC"):
            break


# PROGRAMA PRINCIPAL
janela = Window(800, 600)  # Tamanho da janela
teclado = Keyboard()
