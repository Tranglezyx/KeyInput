import time
import keyboard
import threading
import sys

aKeyInterval = 1.8
bKeyInterval = 60
pressCount = 100
pressInterval = 0.1

def f1Strategy():
    print("F1开始")
    pauseEvent.set()
    threadA.start()
    threadB.start()

def f2Strategy():
    print("F2开始")
    pauseEvent.set()
    threadA.start()
    threadB.start()
    threadRight.start()

def f3Strategy():
    print("F3开始")
    pauseEvent.set()
    threadA.start()
    threadB.start()
    threadLeft.start()

def escStrategy():
    print("暂停")
    pauseEvent.clear()

def pressListener(event):
    key = event.name
    print("按键被按压 :" + key)
    if key == 'f1':
        f1Strategy()

    if key == 'f2':
        f2Strategy()

    if key == 'f3':
        f3Strategy()

    if key == 'esc':
        escStrategy()

def pressA():
    while True:
        pauseEvent.wait()
        keyboard.press('a')
        time.sleep(aKeyInterval)

def pressB():
    while True:
        pauseEvent.wait()
        keyboard.press('b')
        time.sleep(bKeyInterval)

def pressRight():
    while True:
        pauseEvent.wait()
        pressKey('right',pressCount)
        time.sleep(pressInterval)

def pressLeft():
    while True:
        pauseEvent.wait()
        pressKey('left',pressCount)
        time.sleep(pressInterval)

def pressKey(key,count):
    for i in range(count):
        keyboard.press(key)

threadA = threading.Thread(target=pressA) 
threadB = threading.Thread(target=pressB) 
threadRight = threading.Thread(target=pressRight) 
threadLeft = threading.Thread(target=pressLeft) 
pauseEvent = threading.Event()

def main():
    keyboard.on_press(pressListener)
    keyboard.wait()

if __name__ == "__main__":
    main()
