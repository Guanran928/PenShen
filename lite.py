import linecache  # 读取 800.txt
import random  # 选择 800.txt 内的随机行
import time  # 发送延迟

import easygui  # 次数 + 模式选择
from pynput.keyboard import Key, Controller  # 控制键盘

keyboard = Controller()

pressGoal = easygui.enterbox('Repeat Time')

try:
    if pressGoal is None:
        quit()
    else:
        pressGoal = int(pressGoal)  # 转换非'None'的值
except ValueError:
    easygui.msgbox('Please fucking enter a number u idiot')  # :D yes swearing is good

mode = easygui.buttonbox('PenShen in Python', 'PenShen mode selection',
                         ['With Watermark', 'Without Watermark', 'QQ With Watermark', 'QQ Without Watermark', 'exit'])
if mode == 'exit':
    quit()

inGameChatButton = 't'

if mode == 'With Watermark':
    for i in range(1, pressGoal):
        keyboard.type('[Foodbyte] ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(0.5)
        keyboard.press(Key.enter)
        time.sleep(0.5)
        keyboard.type(inGameChatButton)
        time.sleep(0.5)
elif mode == 'Without Watermark':
    for i in range(1, pressGoal):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(0.5)
        keyboard.press(Key.enter)
        time.sleep(0.5)
        keyboard.type(inGameChatButton)
        time.sleep(0.5)
elif mode == 'QQ With Watermark':
    for i in range(1, pressGoal):
        keyboard.type('[Foodbyte] ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(0.5)
elif mode == 'QQ Without Watermark':
    for i in range(1, pressGoal):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(0.5)
