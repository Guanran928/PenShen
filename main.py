from pynput.keyboard import Key, Controller
import random  # for random line in txt file & random delay
import time  # for delay
import linecache  # read txt file
import easygui  # mode selection
# todo: replace easygui w/ tk & put goal and mode selection button in a single gui

keyboard = Controller()
pressGoal = easygui.enterbox('goal')

if pressGoal is None:
    quit()
else:
    pressGoal = int(pressGoal)  # 转换非'None'的值

mode = easygui.buttonbox('AutoL v2',
                         'AutoL v2 mode selection', ['L + text', 'L', 'text', 'in game L + text', 'in game text', 'exit'])
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
if mode == 'L':
    for i in range(1, pressGoal):
        keyboard.type(prefix)
        keyboard.press(Key.enter)
        time.sleep(delay)
if mode == 'text':
    for i in range(1, pressGoal):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        keyboard.press(Key.enter)
        time.sleep(delay)
if mode == 'in game L + text':
    for i in range(1, pressGoal):
        keyboard.type(prefix + ' ' + linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(delay)  # 给minecraft弄的delay，不知道为什么，我在49，51行之间不加delay就不管用
        keyboard.press(Key.enter)
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
if mode == 'in game text':
    for i in range(1, pressGoal):
        keyboard.type(linecache.getline(r'800.txt', random.randrange(1, 800)))
        time.sleep(delay)
        keyboard.press(Key.enter)
        time.sleep(delay)
        keyboard.type(inGameChatButton)
        time.sleep(delay)
