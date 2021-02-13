# -*- coding: utf-8 -*-

import pyautogui, time
time.sleep(5)

f = open("spam_texto.txt", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

