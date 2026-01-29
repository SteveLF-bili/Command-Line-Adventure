import os
import sys
import time
import subprocess
import platform
from colorama import Fore, Style
import json

Language = 'EN'

# 确保在CMD窗口中运行
def ensure_cmd_window():
    if sys.platform == 'win32' and not os.environ.get('PROCESS_IN_CMD'):
        # 设置环境变量标志
        os.environ['PROCESS_IN_CMD'] = '1'
        
        # 启动一个新的CMD窗口并传递环境变量
        script_path = os.path.abspath(sys.argv[0])
        env = os.environ.copy()
        env['PROCESS_IN_CMD'] = '1'
        subprocess.Popen(f'cmd /c start cmd /k python "{script_path}"', shell=True, env=env)
        sys.exit(0)

# 调用确保CMD窗口的函数
ensure_cmd_window()

#清屏
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

print('Loading Console version <CLACMB13>')
time.sleep(3)
print('Checking resource integrity...')
time.sleep(2)
print('2 resources not downloaded/awaiting update have been found')
time.sleep(1)
clear_screen()
print('Downloading missing resources...')
time.sleep(0.5)
print('\033[31m' + 'ERROR: Could not find a version that satisfies the requirement Runtime File V13.6.3 (from versions: none)\nERROR: No matching distribution found for Runtime File V13.6.3' + '\033[0m')
print('Looking for alternative resources...')
time.sleep(0.5)
print('Search successful! The HELPME.runtime file will be used shortly.')
time.sleep(0.2)
clear_screen()
print('\033[32m ' + 'Console version <CLACMB13> downloaded successfully!' + '\033[0m')
time.sleep(0.5)
print('Initializing the configuration......')
time.sleep(1)
print('\033[32m ' + 'Console version <CLACMB13> is ready' + '\033[0m')
time.sleep(1)
clear_screen()
print('Welcome to CLACMB13!')
print('Enter \'help\' to get help')
print('Enter \'Change CN\' to change language to Chinese')

while True:
    input1 = input('>')
    if input1 == 'Change CN':
        if Language == 'EN':
         Language = 'CN'
         input1 = '0'
         clear_screen()
         print('欢迎使用CLACMB13!')
         print('输入\'help\'来获取帮助')
         print('输入\'Change EN\'来切换为英文')
         print('已切换为中文')
        if Language == 'CN':
         print('已经切换为中文模式了')
    elif input1 == 'Change EN':
        if Language == 'CN':
         Language = 'EN'
         input1 = '0'
         print('Welcome to CLACMB13!')
         print('Enter \'help\' to get help')
         print('Enter \'Change CN\' to change language to Chinese')
         print('Switched to English')
        if Language == 'EN':
         print('Already in English mode')
    elif input1 == 'help':
        if Language == 'EN':
         print('The console is fully connected to all control commands of the SERIES-7')
         print('For other instructions, please refer to the instruction manual')
        elif Language == 'CN':
         print('控制台已完全支持SERIES-7的所有控制命令')
         print('其他指令请参考说明书')
    elif input1 == 'USE SERPENT_TERMINAL':
        if Language == 'EN':
         print('Hardware detected: SERIES-7 PORTABLE - 73% \battery remaining')
        if Language == 'CN':
         print('检测到硬件：SERIES-7 PORTABLE - 电池剩余73%')
    elif input1 == 'EXIT':
        if Language == 'EN':
         print('Exiting CLACMB13...\nGoodbye!')
        elif Language == 'CN':
         print('正在退出CLACMB13...\n再见！')
        time.sleep(2)
        break
    else :
        if Language == 'EN':
         print(input1,'\033[91m is not a supported instruction, please check before entering\033[0m')
        elif Language == 'CN':
         print(input1,'\033[91m不是一个受支持的指令，请检查后再输入\033[0m')
