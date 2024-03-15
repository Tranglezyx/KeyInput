import time
import keyboard

mainKey = 'ctrl'
mainKeyInterval = 0.01
otherInterval = 0.5
keyList = ['1','2','4','3','f']
moveFlag = True
moveInterval = 180
endDirection = 'right'
runTime = 3600
# 技能使用间隔时间
clickTime = 6

def f1Strategy():
    time.sleep(5)
    pressKey('0')
    pressKey('0')
    pressKey('0')
    print("F1开始")
    lastTime =  time.time() + runTime
    lastMoveTime = time.time()
    while time.time() < lastTime:
        time.sleep(2)
        nowTime = time.time()
        endTime = nowTime + clickTime
        print("开始,now : {} ,end : {}".format(nowTime,endTime))
        keyboard.press(mainKey)
        while time.time() < endTime:
            time.sleep(mainKeyInterval)
        keyboard.release(mainKey)
        time.sleep(0.5)
        for index, element in enumerate(keyList):
            pressKey(element)
        if time.time() > lastMoveTime + moveInterval and moveFlag:
            print('左右走一次,now:{},lastMoveTime:{}'.format(time.time(),lastMoveTime))
            leftAndRightMove()
            fastPressKey(endDirection)
            lastMoveTime = time.time()
    time.sleep(5)
    comback()
    time.sleep(5)
    comback()
    time.sleep(5)
    comback()

def f3Strategy():
    print("F3开始")
    time.sleep(3)
    pressKey('0')
    pressKey('0')
    pressKey('0')
    count = 4
    lastTime =  time.time() + runTime
    lastMoveTime = time.time()
    while time.time() < lastTime:
        jumpAndHit('left',count)
        jumpAndHit('right',count)
        if time.time() > lastMoveTime + 10:
            lastMoveTime = time.time()
            for index, element in enumerate(keyList):
                pressKey(element)
            

    time.sleep(5)
    comback()
    time.sleep(5)
    comback()
    time.sleep(5)
    comback()

def jumpAndHit(direction,count):
    time.sleep(0.5)
    pressKey(direction)
    jumpKey = 'alt'
    hitKey = 'a'
    for i in range(count):
        pressKeyWithTime(jumpKey,0.1)
        pressKeyWithTime(jumpKey,0.03)
        pressKeyWithTime(hitKey,0.1)
        time.sleep(0.5)

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
    if key == 'f3':
        f3Strategy()

def fastPressKey(key):
    keySleep = 0.05
    keyboard.press(key)
    time.sleep(keySleep)
    keyboard.release(key)
    time.sleep(keySleep)

def pressKey(key):
    keySleep = 0.3
    pressKeyWithTime(key,keySleep)

def pressKeyWithTime(key,keySleep):
    print("按键被按压 : " + key)  
    keyboard.press(key)
    time.sleep(keySleep)
    keyboard.release(key)
    time.sleep(keySleep)

def leftAndRightMove():
    pressKey('left')
    time.sleep(0.5)
    pressKeyWithTime('right',0.25)

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

if __name__ == "__main__":
    main()

