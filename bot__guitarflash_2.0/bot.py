import pyautogui
from pynput.keyboard import Controller
import time

# Inicializa o controlador do teclado
keyboard = Controller()

# Função que compara a cor do pixel com a cor requerida
def detectar_pixel(x, y, cor_rgb_requerida):
    # Captura a cor do pixel na posição (x, y)
    cor_pixel = pyautogui.pixel(x, y)
    
    # Compara as cores (verifica se o RGB bate)
    if cor_pixel == cor_rgb_requerida:
        print(f"Cor encontrada em {x}, {y}! Pressionando a tecla.")
        # Pressiona a tecla "space" se as cores coincidirem
        pyautogui.keyDown('l')
        pyautogui.keyUp('l')
        #keyboard.press('l')
    else:
        print(f"Cor não encontrada em {x}, {y}. Cor atual: {cor_pixel}")

# Parâmetros
x = 1273  # Posição X
y = 630  # Posição Y
cor_rgb_requerida = (255, 255, 255)  # Cor requerida em RGB (exemplo: vermelho)

# Loop para verificar a cor a cada 1 segundo
while True:
    detectar_pixel(x, y, cor_rgb_requerida)
    #time.sleep(0.01)  # Espera 1 segundo antes de verificar novamente
