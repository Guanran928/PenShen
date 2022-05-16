# Made By Guanran928 & nongbaobao(herry-gitee)
# :D
from timeit import repeat
from pynput.keyboard import Key, Controller
import linecache  # read txt file
import random  # for random line in txt file & random delay
import time  # for delay

keyboard = Controller()
initmode = ['前缀 + 句子', '句子', '游戏内前缀 + 句子 (自动按说话按钮)', '游戏内句子', '刷屏', '游戏内刷屏']

def fuckUser(fvar, question, fuck1, fuck2):
    while True:
        fvar = None
        fvar = input(question)
        try:
            if fvar == '':
                exec(fuck1)
            else:
                break
        except ValueError:
            exec(fuck2)  # :D yes swearing is good
    return fvar

mode = input(initmode)
if mode not in initmode:
    print('nothing inputed, too lazy to make a loop to make u enter again')
    exit()

if mode == initmode[0] or mode == initmode[2]: # does this work even
    prefix = input('输入你想发送的前缀 默认为[FoodByte]: ')
    if prefix == '':
            prefix = '[FoodByte]'
            print (prefix)

if mode == initmode[4] or mode == initmode[5]:
    spam = input('输入你想发送的句子: ')

inGameChatButton = 't'

repeatTime = int(fuckUser('repeatTime', '输入你想发送的重复次数: ', 'print(\'大傻逼请宁输一个数\')', 'print(\'大傻逼请宁输一个整数\')'))
delay = float(fuckUser('delay', '延迟(秒, Buggy): ', 'fvar = 0.5', 'print(\'大傻逼请宁输一个整数\')'))
# also you can use: delay = random.uniform(0.5, 1) to prevent BOT Detection

# waiting for user to enter the fucking wechat
time.sleep(2)

# start spamming
# SIMPLEFIED YES YES YES
def repeatLoop(type, ingame):
    if ingame == False:
        for i in range(repeatTime):
            exec(type)
            keyboard.press(Key.enter)
            time.sleep(delay)
        else:
            for i in range(repeatTime):
                exec(type)
                time.sleep(delay)
                keyboard.press(Key.enter)
                time.sleep(delay)
                keyboard.type(inGameChatButton)
                time.sleep(delay)

if mode == initmode[0]:
    repeatLoop(keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800))), False)

elif mode == initmode[1]:
    repeatLoop(keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800))), False)

elif mode == initmode[2]:
    repeatLoop(keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800))), True)

elif mode == initmode[3]:
    repeatLoop(keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800))), True)

elif mode == initmode[4]:
    repeatLoop(keyboard.type(spam), False)

elif mode == initmode[5]:
    repeatLoop(keyboard.type(spam), True)
