import pyautogui
from time import sleep
from pyautogui import press, write, moveTo, mouseUp, mouseDown, alert

pyautogui.PAUSE = 1

press('winright')
write('chrome')
press('enter')
write("https://natansales221.wixsite.com/home")
press('enter')
sleep(2)

# clicar no sobre
moveTo(x=1049, y=642)
mouseDown()
mouseUp()

# descer a tela
for c in range(0, 7):
    press('down')

# clicar no curriculo
moveTo(x=707, y=629)
mouseDown()
mouseUp()

alert('Muito obrigado pela atenção!!')
