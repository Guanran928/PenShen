# Made By Guanran928 & nongbaobao(herry-gitee)

from pynput.keyboard import Key, Controller
import linecache  # read txt file
import random  # for random line in txt file & random delay
import time  # for delay
import easygui  # bcz i dont know how to use tkinter

keyboard = Controller()
initmode = ['前缀 + 句子', '句子', '游戏内前缀 + 句子 (自动按说话按钮)', '游戏内句子', '刷屏', '游戏内刷屏', 'exit']

while True:
    pressGoal = easygui.enterbox('输入的重复次数')
    try:
        if pressGoal is None:
            easygui.msgbox('大傻逼宁怎么可以点cancel')  # L M A O
            quit()
        else:
            pressGoal = int(pressGoal)  # 转换非'None'的值
            break
    except ValueError:
        easygui.msgbox('大傻逼请宁输一个整数')  # :D yes swearing is good

delay = float(easygui.enterbox('延迟(秒)'))
# also you can use: delay = random.uniform(0.5, 1) to prevent BOT Detection

mode = easygui.buttonbox('PenShen in Python', 'PenShen 模式选择', initmode)
if mode == 'exit':
    quit()

if mode == '前缀 + 句子' or mode == '游戏内前缀 + 句子 (自动按说话按钮)': # does this work even
    prefix = easygui.enterbox('输入你想发送的前缀')
if mode == '刷屏' or mode == '游戏内刷屏':
    spam = easygui.enterbox('输入句子')
inGameChatButton = 't'

# waiting for user to enter the fucking wechat
# todo: auto open wechat / other software
# why dont i just use time.sleep(2)
t = 2
for i in range(t):
    print(str(t-i) +'\n')
    time.sleep(1)

# spammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# e thats alot of elif :/
if mode == '前缀 + 句子':
    for i in range(1, pressGoal):
        keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(delay)        
elif mode == '句子':
    for i in range(1, pressGoal):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(delay)
elif mode == '游戏内前缀 + 句子 (自动按说话按钮)':
    for i in range(1, pressGoal):
        keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(delay)  # 给minecraft弄的delay，不知道为什么，我在上下行之间不加delay就不管用
        keyboard.press(Key.enter)
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
elif mode == '游戏内句子':
    for i in range(1, pressGoal):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(delay)
        keyboard.press(Key.enter)
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
elif mode == '刷屏':
    for i in range(1, pressGoal):
        keyboard.type(spam)
        keyboard.press(Key.enter)
        time.sleep(delay)
elif mode == '游戏内刷屏':
    for i in range(1, pressGoal):
        keyboard.type(spam)
        time.sleep(delay)
        keyboard.press(Key.enter) 
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
