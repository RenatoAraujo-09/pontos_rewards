"""
Script para automatizar tarefas no navegador usando o pyautogui, para resgate de pontos xbox rewards.
"""
import time
import pyautogui

# Configuração inicial
pyautogui.PAUSE = 3
rewards_url = "https://rewards.bing.com/"

# Abrir o navegador Edge
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")

# Navegar para a URL dos prêmios do Bing
pyautogui.click(x=659, y=50)
pyautogui.write(rewards_url)
pyautogui.press("enter")
time.sleep(7)

# Esperar até que a página carregue
pyautogui.click(x=710, y=486)
for i in range(36):
    pyautogui.press('tab')
# range 36 vai variar de quantas tab precisa ate chegar no campo PC Search
for i in range(2):
    pyautogui.press("enter")
time.sleep(5)

# Realizar 30 pesquisas com as cores de cabelo para completar os pontos
colors = ["vermelho", "amarelo", "verde", "azul", "roxo", "rosa", "violeta",
    "lilas", "preto", "loiro", "ruivo", "amarelo e preto", "verde e azul",
    "verde e vermelho", "verde e preto", "cinza", "amarelo e azul",
    "vermelho cereja", "marçala", "vermelho e preto", "vermelho escuro",
    "azul piscina", "verde agua", "amarelo sol", "curto", "moecano",
    "masculino", "de bebe", "em ve", "chanel", "longo", "colorido"]

for color in colors:
    pyautogui.click(x=512, y=112)
    pyautogui.write(f"Cabelo {color}")
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=717, y=111)
    
