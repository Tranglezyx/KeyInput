import time
import keyboard


def pressStartListener(event):
    key = event.name
    if key == ',':
        print("开始")
        while True:
            keyboard.press('a')
            time.sleep(2)

def pressEndListener(event):
    key = event.name
    if key == '.':
        print("停止")
        keyboard.unhook_all()

def main():
    keyboard.on_press(pressStartListener)
    keyboard.on_press(pressEndListener)
    keyboard.wait()

if __name__ == "__main__":
    main()
