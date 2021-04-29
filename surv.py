from PIL import Image, ImageGrab
import pyautogui
from time import sleep
import time
sleep(15)
tty = True
rtt = True
while rtt:
    pyautogui.PAUSE = 0.2
    pyautogui.press("s")#---------------------if sleep
    sleep(1)
    pyautogui.moveTo(289, 785) #--------------survival mode
    pyautogui.click()
    pyautogui.moveTo(225, 891) #--------------neww
    pyautogui.click()
    pyautogui.moveTo(245, 788) #--------------piligrim
    pyautogui.click(clicks=2, interval=0.2)
    pyautogui.moveTo(659, 159) #--------------region
    pyautogui.click()
    pyautogui.moveTo(2173, 1352)
    pyautogui.click(clicks=3, interval=0.2)
    pyautogui.moveTo(1136, 847) #-------------accept
    pyautogui.click()
    sleep(6) #--------------------------------waiting time before start
    pyautogui.press("s")
    sleep(6)
    pyautogui.press("Esc")#

    while tty:
        img = ImageGrab.grab( (1426, 330, 1427, 331) )
        img.save("D:/HTML/aim/screens2/dead.png", "BMP")

        #walk
        pyautogui.keyDown("w")
        sleep(1)
        pyautogui.keyUp("w")
        pyautogui.keyDown("s")
        sleep(1)
        pyautogui.keyUp("s")

        dead = Image.open('D:/HTML/aim/screens2/dead.png', 'r')
        colorD = list(dead.getdata())
        #print(colorD)
        if colorD == [(110, 130, 123)]:
            pyautogui.moveTo(2333, 1374)
            pyautogui.click()
            pyautogui.moveTo(1139, 846)
            pyautogui.click()
            sleep(10)
            pyautogui.moveRel(10, 10, 1)
            break
        else:
            continue

        #walk2
        pyautogui.keyDown("w")
        sleep(1)
        pyautogui.keyUp("w")

        pyautogui.keyDown("s")
        sleep(1)
        pyautogui.keyUp("s")