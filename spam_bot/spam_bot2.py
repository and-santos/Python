# -*- coding: utf-8 -*-

import pyautogui, time, pyperclip
time.sleep(5)

f = open("spam_texto_axt.txt",'r', encoding="utf-8")

for word in f:
   pyperclip.copy(word)
   pyautogui.hotkey("ctrl","v") 
   pyautogui.press("enter")