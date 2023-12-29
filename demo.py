import time
import keyboard
import threading
import sys

aKeyInterval = 1.8
bKeyInterval = 600
pressCount = 10000
pressInterval = 0.1

def pressListener(event):
    key = event.name
    print("按键被按压 :" + key)
    if key == 'f1':
        print("F1开始")
        pause_event.set()
        threadA.start()
        threadB.start()

    if key == 'f2':
        print("F2开始")
        pause_event.set()
        threadA.start()
        threadB.start()
        threadRight.start()

    if key == 'f3':
        print("F3开始")
        pause_event.set()
        threadA.start()
        threadB.start()
        threadLeft.start()

    if key == 'esc':
        print("暂停")
        pause_event.clear()

    if key == 'f12':
        print("退出程序")
        sys.exit()

def pressA():
    while True:
        pause_event.wait()
        keyboard.press('a')
        keyboard.release('a')
        time.sleep(aKeyInterval)

def pressB():
    while True:
        pause_event.wait()
        keyboard.press('b')
        keyboard.release('b')
        time.sleep(bKeyInterval)

def pressRight():
    while True:
        pause_event.wait()
        pressKey('right',pressCount)
        time.sleep(pressInterval)

def pressLeft():
    while True:
        pause_event.wait()
        pressKey('left',pressCount)
        time.sleep(pressInterval)

def pressKey(key,count):
    for i in range(count):
        keyboard.press(key)

threadA = threading.Thread(target=pressA) 
threadB = threading.Thread(target=pressB) 
threadRight = threading.Thread(target=pressRight) 
threadLeft = threading.Thread(target=pressLeft) 
pause_event = threading.Event()

def main():
    keyboard.on_press(pressListener)
    keyboard.wait()

if __name__ == "__main__":
    main()
