import pygetwindow, pyautogui
from time import sleep

hwnd_lol = pygetwindow.getWindowsWithTitle('League of Legends')[0] # pega o codigo da janela do lol
while True:
    left, top, width, height = hwnd_lol.left, hwnd_lol.top, hwnd_lol.width, hwnd_lol.height
# x1, y1, x2, y2 = 475, 436, 551, 453
# while True:
#     try:
#         region = (left + x1, top +y1, x2 - x1, y2 - y1)
#         break
#     except:
#         input("[ERRO] Pressione enter e tente novamente!")
#         sleep(1)
# sleep(2)
# screenshot = pyautogui.screenshot(region=(region))
# screenshot.save('image.png')
# print(screenshot)
