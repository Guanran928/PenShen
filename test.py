from pynput.keyboard import Key, Controller
import time  # for delay
spam = '1'
repeatTime = 2
delay = 0.5

keyboard = Controller()

for i in range(repeatTime):
   keyboard.type(spam)
   keyboard.press(Key.enter)
   time.sleep(delay)
