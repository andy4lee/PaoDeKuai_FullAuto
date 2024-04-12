# -*- coding: utf-8 -*-

# Created by: Raf

# 这个文件用来辅助调整截图区域坐标。运行游戏，全屏截图，放上路径，就可以查看截图区域。

import cv2
import matplotlib.pyplot as plt
import win32gui

# Modify the region parameters and the image path
capture_pos = [(82, 518, 1157, 66),    # 玩家手牌区域
               (499, 70, 364, 128),   # 下家出牌区域
               (700, 400, 147, 55),  # 玩家要不起区域
               (998, 624, 140, 54),   # 玩家下一局
               (855, 400, 108, 55),    # 玩家出牌
               (670, 458, 97, 55),    # 打完一局的提示词准备
               (424, 625, 94, 48),    # 打完九局的准备按钮
               (280, 300, 694, 54)     # 玩家出牌区域
               ]
img_path = 'pics/ceshi6.png'


img = cv2.imread(img_path)
for pos in capture_pos:
      img = cv2.rectangle(img, pos[0:2], (pos[0] + pos[2], pos[1] + pos[3]), (0, 0, 255), 3)
plt.imshow(img)
plt.show()

