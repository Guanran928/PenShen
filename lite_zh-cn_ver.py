# coding=utf-8
# Made By Guanran928 & nongbaobao(herry-gitee)
# :D
import linecache  # read txt file
import random  # for random line in txt file & random delay
import time  # for delay

from pynput.keyboard import Key, Controller

# init
keyboard = Controller()
initmode = ['前缀 + 句子', '句子', '游戏内前缀 + 句子 (自动按说话按钮)', '游戏内句子', '刷屏', '游戏内刷屏']


# settings
def fuck_user(question, fuck1, fuck2, reform_str, ifInit = False, initValue = ''):
    while True:
        fuck_var = input(question)
        try:
            if fuck_var == '':
                exec(fuck1)
                if ifInit == True:
                    return initValue
            else:
                print(fuck_var)
                return eval(reform_str)
        except ValueError:
            exec(fuck2)  # :D yes shitcode

mode = input(initmode)
if mode not in initmode:
    print('nothing inputted, too lazy to make a loop to make u enter again')
    exit()

if mode == initmode[0] or mode == initmode[2]:  # does this work even
    prefix = input('输入你想发送的前缀 默认为[FoodByte]: ')
    if prefix == '':
        prefix = '[FoodByte]'
        print (prefix)

if mode == initmode[4] or mode == initmode[5]:
    while True:
        spam = input('输入你想发送的句子: ')
        print(spam)
        if spam != '':
            break
        else:
            print('please enter smth')

inGameChatButton = 't'

repeatTime = fuck_user('输入你想发送的重复次数: ', 'print(\'大傻逼请宁输一个数\')', 'print(\'大傻逼请宁输一个整数\')', 'int(fuck_var)')
delay = fuck_user('延迟(秒, Buggy, 默认0.5s): ', 'print(\'0.5\')', 'print(\'大傻逼请宁输一个整数\')', 'float(fuck_var)', True, 0.5)
# also you can use: delay = random.uniform(0.5, 1) to prevent BOT Detection

repeatTime+=1

# waiting for user to enter the fucking wechat
time.sleep(2)


# start spamming
# SIMPLIFIED YES YES YES
def spam_loop(spam_type, if_ingame):
    print('spamming started')
    if if_ingame is False:
        for i in range(repeatTime):
            eval(spam_type)
            keyboard.press(Key.enter)
            time.sleep(delay)
    else:
        for i in range(repeatTime):
            eval(spam_type)
            time.sleep(delay)
            keyboard.press(Key.enter)
            time.sleep(delay)
            keyboard.type(inGameChatButton)
            time.sleep(delay)
    print('spamming ended')


if mode == initmode[0]:
    spam_loop('keyboard.type(prefix + \' \' + linecache.getline(r\'800.txt\', random.randrange(1, 800)))', False)

elif mode == initmode[1]:
    spam_loop('keyboard.type(linecache.getline(r\'800.txt\', random.randrange(1, 800)))', False)

elif mode == initmode[2]:
    spam_loop('keyboard.type(prefix + \' \' + linecache.getline(r\'800.txt\', random.randrange(1, 800)))', True)

elif mode == initmode[3]:
    spam_loop('keyboard.type(linecache.getline(r\'800.txt\', random.randrange(1, 800)))', True)

elif mode == initmode[4]:
    spam_loop('keyboard.type(spam)', False)

elif mode == initmode[5]:
    spam_loop('keyboard.type(spam)', True)
