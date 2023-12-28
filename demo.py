import win32gui
import win32api
import win32con
import time
import pygetwindow as gw
import pyautogui
import ctypes

def showAllWindows():
    for window in gw.getAllWindows():
        print(window)

def showActiveWindow():
    while True:
        window = win32gui.GetForegroundWindow()
        print(window)
        time.sleep(2.5)

def pressNumber0(window):
    win32api.PostMessage(window, win32con.WM_KEYDOWN, win32con.VK_F12, 0)
    win32api.PostMessage(window, win32con.WM_KEYUP, win32con.VK_F12, 0)

def clickWithTitle(title):
    window = win32gui.FindWindow(None, title)
    print("找到的窗口:",window)
    while True:
        pressNumber0(window)
        time.sleep(1)

def clickWithId(id):
    while True:
        pressNumber0(id)
        time.sleep(1)

def clickA(inteval):
    while True:
        # pyautogui.press("A")
        pyautogui.hotkey("alt","a")
        time.sleep(inteval)
        pyautogui.press("esc")
        time.sleep(inteval)

user32 = ctypes.WinDLL('user32')
VK_A = 0x41
# 定义键盘按键标志常量
KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002

def clickA1(inteval):
    while True:
        # 加载user32.dll库
        # 调用keybd_event函数模拟按键按下
        user32.keybd_event(65, 0, KEYEVENTF_KEYDOWN, 0)
        
        # 调用keybd_event函数模拟按键释放
        user32.keybd_event(65, 0, KEYEVENTF_KEYUP, 0)
        time.sleep(1)

def main():
    # showAllWindows()
    # clickWithTitle("阿里云控制台-日志服务 - GAoogle Chrome")AAA
    # showActiveWindow()
    # clickWithId(198096)
    clickA1(1)

if __name__ == "__main__":
    main()
