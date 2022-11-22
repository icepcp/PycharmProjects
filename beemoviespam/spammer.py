import pyautogui, time
time.sleep(5)
# Change game to bee if you want the bee movie script
f = open("game",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
