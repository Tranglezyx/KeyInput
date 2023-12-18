import pyautogui
import win32gui
import time
import pygetwindow as gw

def showActiveWindow():
    for window in gw.getAllWindows():
        print(window)

def main():
    # showActiveWindow()
    windowHandle = pyautogui.getWindowsWithTitle("● 页面接入短信发送.sql - txt - Visual Studio Code")
    print(windowHandle)
    if(windowHandle):
        window = windowHandle[0]
        print(window)
        pyautogui.press(window, "A")
        # 模拟释放 "Enter" 键
        pyautogui.release(window, "A")

if __name__ == "__main__":
    main()
