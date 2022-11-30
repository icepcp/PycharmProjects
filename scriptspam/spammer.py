import time
import pyautogui
a = input("Type filename: ")
b = input("Seconds before disaster: ")
b = int(b)
c = open(a)
time.sleep(b)
for word in c:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
