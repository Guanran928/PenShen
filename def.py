# Made By Guanran928 & nongbaobao(herry-gitee)
# :D
from pynput.keyboard import Key, Controller
import linecache  # read txt file
import random  # for random line in txt file & random delay
import time  # for delay
import easygui  # bcz i dont know how to use tkinter

keyboard = Controller()
initmode = ['前缀和句子', '游戏内前缀和句子', '句子', '游戏内句子', '刷屏', '游戏内刷屏', 'exit']


def cancel():
    easygui.msgbox('大傻逼宁怎么可以点cancel')  # L M A O
    quit()

mode = easygui.buttonbox('模式选择', 'PenShen 模式选择, 游戏内为自动开启聊天栏', initmode)
if mode == 'exit' or mode == 'None':
    cancel
if mode == '前缀和句子' or mode == '游戏内前缀和句子 (自动按说话按钮)': # does this work even
    prefix = easygui.enterbox('输入你想发送的前缀')
if mode == '刷屏' or mode == '游戏内刷屏':
    spam = easygui.enterbox('输入句子')

inGameChatButton = 't'

while True:
    repeatTime = easygui.enterbox('输入的重复次数')
    try:
        if repeatTime is None:
            cancel()
        else:
            repeatTime = int(repeatTime)  # 转换非'None'的值
            break
    except ValueError:
        easygui.msgbox('大傻逼请宁输一个整数')  # :D yes swearing is good

while True:  # yes copy & paste
    delay = easygui.enterbox('延迟(秒)')
    try:
        if repeatTime is None:
            cancel()
        else:
            delay = float(delay)
            break
    except ValueError:
        easygui.msgbox('大傻逼请宁输个数')

# also you can use: delay = random.uniform(0.5, 1) to prevent BOT Detection

# waiting for user to enter the fucking wechat
# todo: auto open wechat / other software?
time.sleep(2)

# changed those "elif" to "def"
def 前缀和句子():
    for i in range(1, repeatTime):
        keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(delay)
def 游戏内前缀和句子():
    for i in range(repeatTime):
        keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(delay)  # 给minecraft弄的delay，不知道为什么，我在上下行之间不加delay就不管用
        keyboard.press(Key.enter)
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)   
def 句子():
    for i in range(repeatTime):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(delay)
def 游戏内句子():
    for i in range(repeatTime):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(delay)
        keyboard.press(Key.enter)
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
def 刷屏():
    for i in range(repeatTime):
        keyboard.type(spam)
        keyboard.press(Key.enter)
        time.sleep(delay)
def 游戏内刷屏():
    for i in range(repeatTime):
        keyboard.type(spam)
        time.sleep(delay)
        keyboard.press(Key.enter) 
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)

exec(mode)
