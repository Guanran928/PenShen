import linecache  # read txt file
import random  # for random line in txt file & random delay
import time  # for delay

import easygui  # mode selection
from pynput.keyboard import Key, Controller

# todo: replace easygui w/ tk & put goal and mode selection button in a single gui

keyboard = Controller()
pressGoal = easygui.enterbox("Repeat Time")

try:
    if pressGoal is None:
        quit()
    else:
        pressGoal = int(pressGoal)  # 转换非'None'的值
except ValueError:
    easygui.msgbox("Please fucking enter a number u idiot")  # :D yes swearing is good
mode = easygui.buttonbox('AutoL v2',
                         'AutoL v2 mode selection',
                         ['L + text', 'L', 'text', 'in game L + text', 'in game text', 'exit'])
if mode == 'exit':
    quit()

inGameChatButton = 't'
delay = 0.5
prefix = 'L'
# also you can use: delay = random.uniform(0.5, 1) to prevent BOT Detection


# waiting for user to enter the fucking wechat
# todo: auto open wechat / other software
time.sleep(5)

# spammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
if mode == 'L + text':
    for i in range(1, pressGoal):
        keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(delay)
elif mode == 'L':
    for i in range(1, pressGoal):
        keyboard.type(prefix)
        keyboard.press(Key.enter)
        time.sleep(delay)
elif mode == 'text':
    for i in range(1, pressGoal):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(delay)
elif mode == 'in game L + text':
    for i in range(1, pressGoal):
        keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(delay)  # 给minecraft弄的delay，不知道为什么，我在52，54行之间不加delay就不管用
        keyboard.press(Key.enter)
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
elif mode == 'in game text':
    for i in range(1, pressGoal):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(delay)
        keyboard.press(Key.enter)
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
