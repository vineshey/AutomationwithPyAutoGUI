import random
import sys
sys.path.append(r'C:\Users\ACER\AppData\Roaming\Python\Python311\Scripts')
import pyautogui as pg
import time
animal=('monkey','donkey','dog')
time.sleep(8)
for i in range(25):
    a=random.choice(animal)
    pg.write("you are a "+a)
    pg.press('enter')
