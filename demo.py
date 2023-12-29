import time
import keyboard
import threading

pause_event = threading.Event()

def pressListener(event):
    key = event.name
    if key == ',':
        print("开始")
        pause_event.set()
        threadA.start()
        threadB.start()
    if key == '.':
        print("停止")
        pause_event.clear()

def newThreadPressA():
    while True:
        pause_event.wait()
        keyboard.press('a')
        time.sleep(2)

def newThreadPressB():
    while True:
        pause_event.wait()
        keyboard.press('b')
        time.sleep(600)

threadA = threading.Thread(target=newThreadPressA) 
threadB = threading.Thread(target=newThreadPressB) 

def main():
    keyboard.on_press(pressListener)
    keyboard.wait()

if __name__ == "__main__":
    main()
