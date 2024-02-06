import time
import keyboard

mainKey = 'ctrl'
mainKeyInterval = 0.01
otherInterval = 0.5
keyList = ['a','d','v','b'] 

def f1Strategy():
    time.sleep(5)
    pressKey('9')
    pressKey('9')
    pressKey('9')
    print("F1开始")
    lastTime =  time.time() + 3600
    while time.time() < lastTime:
        time.sleep(2)
        nowTime = time.time()
        endTime = nowTime + 10
        print("开始,now : {} ,end : {}".format(nowTime,endTime))
        print("按键被按压 : " + mainKey)
        keyboard.press(mainKey)
        while time.time() < endTime:
            time.sleep(mainKeyInterval)
        keyboard.release(mainKey)
        time.sleep(0.5)
        for index, element in enumerate(keyList):
            print("按键被按压 : " + element)  
            pressKey(element)
    time.sleep(5)
    comback()
    time.sleep(5)
    comback()
    time.sleep(5)
    comback()

def escStrategy():
    start = 0
    print("暂停")

def pressListener(event):
    key = event.name
    print("按键被按压 :" + key)
    if key == 'f1':
        f1Strategy()
    if key == 'f2':
        comback()

    if key == 'esc':
        escStrategy()

def leftAndRightWalk():
    pressKey('left')
    pressKey('left')
    pressKey('left')
    pressKey('left')
    pressKey('left')
    pressKey('right')
    pressKey('right')
    pressKey('right')
    pressKey('right')
    pressKey('right')

def comback():
    pressKey('j')
    pressKey('down')
    pressKey('down')
    pressKey('down')
    pressKey('enter')
    pressKey('down')
    pressKey('enter')

def main():
    keyboard.on_press(pressListener)
    keyboard.wait()

def pressKey(key):
    keySleep = 0.3
    keyboard.press(key)
    time.sleep(keySleep)
    keyboard.release(key)
    time.sleep(keySleep)

if __name__ == "__main__":
    main()

