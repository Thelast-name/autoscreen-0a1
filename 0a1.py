import pyautogui as pg
import time

i = 0

while True :
    print('Please select')
    s = int(input("Enter 1.screenshot 2.stop: "))
    if s == 1:
        pg.screenshot(str(i)+".png")
        i+=1
        time.sleep(5)
    if s == 2:
        break
    print('--------------------------')