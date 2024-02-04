import time
import keyboard

mainKey = 'q'
mainKeyInterval = 1
otherInterval = 0.2
keyList = ['a', 'd', 'v'] 

start = 0

def f1Strategy():
    print("F1开始")
    start = 1
    while start == 1:
        nowTime = time.time()
        while time.time() < nowTime + 10:
            keyboard.press(mainKey)
            time.sleep(mainKeyInterval)
        for index, element in enumerate(keyList):  
            keyboard.press(element)
            time.sleep(otherInterval)

def escStrategy():
    start = 0
    print("暂停")

def pressListener(event):
    key = event.name
    print("按键被按压 :" + key)
    if key == 'f1':
        f1Strategy()

    if key == 'esc':
        escStrategy()

def main():
    keyboard.on_press(pressListener)
    keyboard.wait()

if __name__ == "__main__":
    main()

