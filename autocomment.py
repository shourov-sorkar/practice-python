import pyautogui
import time
comments = ["Hello", "This  is a bot", "This is cool", "Isn't it cool?", "What do you think?", "A simple python script for autocomment", "Auto Comment", "Hola", "Thank you"]
time.sleep(5)
for i in range(len(comments)):
    pyautogui.typewrite(comments[i])
    pyautogui.typewrite("\n")  # For pressing the Enter button
    time.sleep(5)