# Made By Guanran928 & nongbaobao(herry-gitee)
# fuck u
from pynput.keyboard import Key, Controller
import linecache  # read txt file
import random  # for random line in txt file & random delay
import time  # for delay
import easygui  # bcz i dont know how to use tkinter

keyboard = Controller()
initmode = ['PREFIX + TEXT', 'TEXT', 'IN GAME PREFIX + TEXT (AUTO PRESS CHAT BUTTON)', 'IN GAME TEXT', 'SPAMMER', 'IN GAME SPAMMER', 'EXIT']

mode = easygui.buttonbox('PenShen in Python', 'PenShen Mode Selection', initmode)
if mode == 'EXIT' or mode is None:
    easygui.msgbox('dont even try to click exit u motherfucker')  # L M A O
    quit()
if mode == 'PREFIX + TEXT' or mode == 'IN GAME PREFIX + TEXT (AUTO PRESS CHAT BUTTON)': # does this work even
    prefix = easygui.enterbox('输入你想发送的前缀')
if mode == 'SPAMMER' or mode == 'IN GAME SPAMMER':
    spam = easygui.enterbox('输入TEXT')
    
inGameChatButton = 't'

while True:
    repeatTime = easygui.enterbox('Repeat time')
    try:
        if repeatTime is None:
            easygui.msgbox('dont even try to click cancel u motherfucker')
            quit()
        else:
            repeatTime = int(repeatTime)  # 转换非'None'的值
            break
    except ValueError:
        easygui.msgbox('can u even enter a fucking number')  # :D yes swearing is good

while True:  # yes copy & paste
    delay = easygui.enterbox('Delay (sec)')
    try:
        if repeatTime is None:
            easygui.msgbox('dont even try to click cancel u motherfucker')
            quit()
        else:
            delay = float(delay)
            break
    except ValueError:
        easygui.msgbox('can u even enter a fucking number')

# also you can use: delay = random.uniform(0.5, 1) to prevent BOT Detection

# waiting for user to enter the fucking wechat
# todo: auto open wechat / other software
time.sleep(2)

# spammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# e thats alot of elif :/
if mode == 'PREFIX + TEXT':
    for i in range(1, repeatTime):
        keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(delay)        
elif mode == 'TEXT':
    for i in range(1, repeatTime):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(delay)
elif mode == 'IN GAME PREFIX + TEXT (AUTO PRESS CHAT BUTTON)':
    for i in range(1, repeatTime):
        keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(delay)  # 给minecraft弄的delay，不知道为什么，我在上下行之间不加delay就不管用
        keyboard.press(Key.enter)
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
elif mode == 'IN GAME TEXT':
    for i in range(1, repeatTime):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(delay)
        keyboard.press(Key.enter)
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
elif mode == 'SPAMMER':
    for i in range(1, repeatTime):
        keyboard.type(spam)
        keyboard.press(Key.enter)
        time.sleep(delay)
elif mode == 'IN GAME SPAMMER':
    for i in range(1, repeatTime):
        keyboard.type(spam)
        time.sleep(delay)
        keyboard.press(Key.enter) 
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
