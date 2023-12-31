import time
import keyboard
import threading
import sys

buffKey = ['2','4']
aKeyInterval = 1.8
bKeyInterval = 300
buffInterval = 250
pressCount = 1000
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

def f4Strategy():
    print("F4开始")
    pauseEvent.set()
    threadGoWG.start()
    time.sleep(6)
    threadA.start()
    threadB.start()

def goWG():
    print("F4开始")
    while True:
        pauseEvent.wait()
        time.sleep(1)
        keyboard.press('space')
        time.sleep(1)
        keyboard.press('right')
        time.sleep(0.5)
        keyboard.release('right')
        time.sleep(0.5)
        keyboard.press('space')
        time.sleep(1220) 

def escStrategy():
    print("暂停")
    pauseEvent.clear()
    keyboard.release('right')
    keyboard.release('left')

def pressListener(event):
    key = event.name
    print("按键被按压 :" + key)
    if key == 'f1':
        f1Strategy()

    if key == 'f2':
        f2Strategy()

    if key == 'f3':
        f3Strategy()

    if key == 'f4':
        f4Strategy()

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

def pressBuff():
    while True:
        pauseEvent.wait()
        for key in buffKey:
            keyboard.press(key)
            time.sleep(0.5)
        time.sleep(buffInterval)

def pressRight():
    while True:
        pauseEvent.wait()
        keyboard.press('right')
        time.sleep(pressInterval)

def pressLeft():
    while True:
        pauseEvent.wait()
        keyboard.press('left')
        time.sleep(pressInterval)
    
threadA = threading.Thread(target=pressA) 
threadB = threading.Thread(target=pressB) 
threadBuff = threading.Thread(target=pressBuff)
threadRight = threading.Thread(target=pressRight) 
threadLeft = threading.Thread(target=pressLeft)
threadGoWG = threading.Thread(target=goWG) 
pauseEvent = threading.Event()

def main():
    keyboard.on_press(pressListener)
    keyboard.wait()

if __name__ == "__main__":
    main()
