import pyautogui
import win32gui
import win32api
import win32con
import time
import pygetwindow as gw

def showActiveWindow():
    for window in gw.getAllWindows():
        print(window)

def pressNumber0(window):
    win32api.PostMessage(window, win32con.WM_KEYDOWN, win32con.VK_NUMPAD0, 0)
    win32api.PostMessage(window, win32con.WM_KEYUP, win32con.VK_NUMPAD0, 0)

def main():
    # showActiveWindow()
    # windowHandle = pyautogui.getWindowsWithTitle("页面接入短信发送.sql - txt - Visual Studio Code")
    window = win32gui.FindWindow(None, "页面接入短信发送.sql - txt - Visual Studio Code")
    while True:
        pressNumber0(window)
        time.sleep(1)
        

if __name__ == "__main__":
    main()
