import pyautogui
import time
print("Enter the string and number of times ")

ip = input().split(' ')

print("Place the cursor within 10 secs")
time.sleep(10)

for i in range(0,int(ip[1])):
    pyautogui.typewrite(ip[0])
    pyautogui.press('return')