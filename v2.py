import pyautogui 

def main():
    path = 'D:\\workspace\\python\\KeyInput\\image\\1111.png'
    try:
        location = pyautogui.locateOnScreen(path)
        if location is not None:
            x, y, width, height = location
            center_x = x + width / 2
            center_y = y + height / 2
            print(center_x)
            print(center_y)
            pyautogui.click(center_x,center_y)
        else:
            print("Image not found on the screen.")
    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen.")

if __name__ == "__main__":
    main()