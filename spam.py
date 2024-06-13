import pyautogui, pyperclip, random, time
print("Tool spam by Toàn")
msg = input("nhập nội dung cần spam: ").split(" // ")
n= int(input("nhập số lần spam: "))
m= float(input("nhập thời gian delay: "))

print("Relay...")
for i in range(5,0,-1):
    print(i,end="...",flush='True')
    time.sleep(1)
print("start")

for i in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(m)
