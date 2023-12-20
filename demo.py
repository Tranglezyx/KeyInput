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
    win32api.PostMessage(window, win32con.WM_KEYDOWN, win32con.VK_F12, 0)
    win32api.PostMessage(window, win32con.WM_KEYUP, win32con.VK_F12, 0)

def click(title):
    window = win32gui.FindWindow(None, title)
    print("找到的窗口:",window)
    while True:
        pressNumber0(window)
        time.sleep(1)

def main():
    # showActiveWindow()
    click("阿里云控制台-日志服务 - Google Chrome")
        

if __name__ == "__main__":
    main()
