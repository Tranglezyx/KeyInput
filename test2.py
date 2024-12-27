import psutil
import pygetwindow as gw
import pyautogui
import time
from pywinauto import Application

# === 1. 找到进程并激活窗口 ===
def find_and_activate_window(process_name):
    # 遍历所有进程，找到匹配的进程
    for proc in psutil.process_iter(['pid', 'name']):
        # print(f"进程名称:{proc.info['name']},pid:{proc.pid}")
        if proc.info['name'].find(process_name) != -1:
            try:
                app = Application().connect(process=proc.info['pid'])
                window = app.top_window()
                window.set_focus()
                print(f"已激活窗口: {window.window_text()}")
                return window
            except Exception as e:
                print(f"激活窗口失败: {e}")
                return None
    print("未找到指定的进程。")
    return None

# === 2. 在相对坐标点击 ===
def click_relative(window, x, y):
    try:
        # 获取窗口的位置和大小
        rect = window.rectangle()
        window_left = rect.left
        window_top = rect.top

        # 计算绝对坐标
        abs_x = window_left + x
        abs_y = window_top + y

        # 将鼠标移动到目标位置并点击
        pyautogui.moveTo(abs_x, abs_y)
        pyautogui.click()
        print(f"已在窗口内的 ({x}, {y}) 坐标点击。")
    except Exception as e:
        print(f"点击失败: {e}")

# === 3. 主程序 ===
if __name__ == "__main__":
    process_name = "Taskmgr"  # 修改为你的进程名称
    window = find_and_activate_window(process_name)
    if window:
        time.sleep(1)  # 等待窗口激活
        click_relative(window, 100, 200)  # 窗口内的相对坐标
