import time
import keyboard
import threading
import sys

zeroKeyInterval = 0.01
ctrlKeyInterval = 0.01


def f1Strategy():
    print("F1开始")
    pauseEvent.set()
    threadZero.start()

def f2Strategy():
    print("F2开始")
    pauseEvent.set()
    threadCtrl.start()

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

    if key == 'esc':
        escStrategy()

def pressZero():
    while True:
        pauseEvent.wait()
        keyboard.press('0')
        time.sleep(zeroKeyInterval)

def pressCtrl():
    while True:
        pauseEvent.wait()
        keyboard.press('b')
        time.sleep(ctrlKeyInterval)

    
threadZero = threading.Thread(target=pressZero) 
threadCtrl = threading.Thread(target=pressCtrl) 
pauseEvent = threading.Event()

def main():
    keyboard.on_press(pressListener)
    keyboard.wait()

if __name__ == "__main__":
    main()
