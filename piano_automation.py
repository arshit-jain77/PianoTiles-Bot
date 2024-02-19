import pyautogui
from PIL import ImageGrab
import time

print("This is a jenkins try")
def piano(data):
    a=100
    for i in range(750, 751):
        for j in range(600, 601):
            if data[i, j] < a:
                pyautogui.click(i,j)
                return

    for i in range(900, 901):
        for j in range(600, 601):
            if data[i, j] < a:
                pyautogui.click(i,j)
                return

    for i in range(1000, 1001):
        for j in range(600, 601):
            if data[i, j] < a:
                pyautogui.click(i,j)
                return

    for i in range(1200, 1201):
        for j in range(600, 601):
            if data[i, j] < a:
                pyautogui.click(i,j)
                return

    return


if __name__ == "__main__":
    print("Play the game")
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        piano(data)
