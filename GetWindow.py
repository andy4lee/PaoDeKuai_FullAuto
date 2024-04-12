# -*- coding: utf-8 -*-
import win32gui
import pyautogui

def enum_windows_proc(hwnd, output_list):
    # 获取窗口的类名
    class_name = win32gui.GetClassName(hwnd)
    # 获取窗口的标题
    window_title = win32gui.GetWindowText(hwnd)
    # 将句柄、类名和标题添加到列表中
    output_list.append((hwnd, class_name, window_title))
    return True

# 创建一个空列表来存储窗口信息
window_info_list = []

# 枚举所有顶级窗口
win32gui.EnumWindows(enum_windows_proc, window_info_list)

# 打印所有窗口信息
for hwnd, class_name, window_title in window_info_list:
    if window_title == "微乐跑得快":
     print(f"句柄: {hwnd}, 类名: {class_name}, 标题: {window_title}")

     Handle = win32gui.FindWindow(None, "微乐跑得快")
     win32gui.SetActiveWindow(Handle)
     left, top, right, bot = win32gui.GetWindowRect(Handle)
     # 调整窗口大小
     win32gui.MoveWindow(hwnd, 0, 0, 1440, 810, True)