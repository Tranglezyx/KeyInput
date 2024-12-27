import cv2
import numpy as np
import pyautogui
from PIL import Image

def findLocaltion():
    tmpScreenShotName = 'tmp/desktop_screenshot.png'
    # 截取当前桌面屏幕截图
    screenshot = pyautogui.screenshot()
    screenshot.save(tmpScreenShotName)

    # 读取桌面截图和目标图标
    desktop_image = cv2.imread(tmpScreenShotName)
    # 你保存的图标截图
    icon_image = cv2.imread('image/caidan.png')  

    # 转换为灰度图
    desktop_gray = cv2.cvtColor(desktop_image, cv2.COLOR_BGR2GRAY)
    icon_gray = cv2.cvtColor(icon_image, cv2.COLOR_BGR2GRAY)

    # 模板匹配
    result = cv2.matchTemplate(desktop_gray, icon_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 设置匹配的阈值（0.8 表示匹配度 80% 以上）
    threshold = 0.8

    if max_val >= threshold:
        print(f"匹配成功！图标坐标: {max_loc}")
        top_left = max_loc
        icon_w, icon_h = icon_image.shape[1], icon_image.shape[0]
        bottom_right = (top_left[0] + icon_w, top_left[1] + icon_h)
        
        # 在截图上绘制矩形标记图标位置
        cv2.rectangle(desktop_image, top_left, bottom_right, (0, 255, 0), 2)
        # cv2.imwrite('tmp/result.png', desktop_image)
        if max_val >= threshold:
            icon_center = (top_left[0] + icon_w // 2, top_left[1] + icon_h // 2)
            # pyautogui.moveTo(icon_center[0], icon_center[1])
            # pyautogui.click()
    else:
        print("未能在桌面上找到匹配的图标。")

def main():
    findLocaltion()

if __name__ == "__main__":
    main()
