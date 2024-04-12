import pyautogui
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import numpy as np
import DetermineColor as DC
import GameHelper as gh
from GameHelper import GameHelper
import win32gui
import win32ui
from ctypes import windll

helper = GameHelper()
# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()
print(f"Screen resolution: {screen_width}x{screen_height}")

img_path = 'pics/ceshi.png'
img = Image.open(img_path)
#img = pyautogui.screenshot(region=(270, 562, 920, 50))
# 获取图像分辨率（宽度和高度）
image_width, image_height = img.size
print(f"Image resolution: {image_width}x{image_height}")

user_hand_cards_real = ""
AllCards = ['2', 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3']
FilterArg = 30

def cards_filter(location, distance):  # 牌检测结果滤波
    if len(location) == 0:
        return 0
    locList = [location[0][0]]
    poslist = [location[0]]
    count = 1
    for e in location:
        flag = 1  # “是新的”标志
        for have in locList:
            # print(abs(e[0] - have))
            if abs(e[0] - have) <= distance:
                flag = 0
                break
        if flag:
            count += 1
            locList.append(e[0])
            poslist.append(e)
    # print(poslist)
    return count, poslist
def find_cards(img, pos, mark="", confidence=0.8):
    cards_real = ""
    D_king = 0
    X_king = 0
    for card in AllCards:
        result = gh.LocateAllOnImage(img, helper.PicsCV[mark + card], region=pos, confidence=confidence)

        if len(result) > 0:
            count, s = cards_filter(list(result), FilterArg)
            if card == "X" or card == "D":
                for a in s:
                    classifier = DC.ColorClassify(debug=True)
                    img1 = img[pos[1]:pos[1] + pos[3], pos[0]:pos[0] + pos[2]]
                    img2 = img1[a[1]:a[1] + a[3] - 50, a[0]:a[0] + 20]  # 注意连着裁切时img不能重名
                    # gh.ShowImg(img2)
                    result = classifier.classify(img2)
                    # print(result)
                    for b in result:
                        if b[0] == "Red":
                            if b[1] > 0.54:
                                D_king = 1
                            else:
                                X_king = 1
            else:
                cards_real += card[0] * count

    if X_king:
        cards_real += "X"
        cards_real = cards_real[-1] + cards_real[:-1]

    if D_king:
        cards_real += "D"
        cards_real = cards_real[-1] + cards_real[:-1]
    return cards_real

if __name__ == '__main__':
    MyHandCardsPos = (82,518,1157,66)
    img, _ = helper.Screenshot()
    plt.imshow(img)
    plt.show()
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    my_cards_real = find_cards(img, MyHandCardsPos, mark="m")
    print(my_cards_real)
