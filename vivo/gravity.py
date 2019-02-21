#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from adbtools import AdbTools
from adbtools import KeyCode
import time
import os


def get_lock_screen_state(self):
        '''判断手机屏幕解锁状态
        False为已解锁
        True为未解锁
        '''
        l = self.shell('dumpsys window policy|findstr isStatusBarKeyguard').readlines()
        for i in l:
            if 'isStatusBarKeyguard=true' in i:
                return True
            else:
                return False

device_name = '78340964'
device = AdbTools(device_name)
# result = get_lock_screen_state(device)

def cut_resources1():
    device.shell('am start com.example.vivotest/.StartActivity bnds')
    time.sleep(2)
    device.shell('input tap 550 600')
    time.sleep(2)
    device.shell('input tap 800 500')
    time.sleep(5)
    for i in range(1, 7):
        device.shell("input keyevent KEYCODE_POWER")
        time.sleep(2)
        i += 1
        print(i)
    device.shell("input swipe 550 1700 550 380 1000")
    # 判断手机是否解锁成功
    result = True
    while result:
        os.popen('adb shell input swipe 550 1700 550 380')
        time.sleep(2)
        result = get_lock_screen_state(device)
        print result
        time.sleep(2)


def cut_resources2():
    device.shell('am start com.bbk.theme/com.bbk.theme.ResListActivity')
    time.sleep(2)
    device.shell('input tap 225 660')
    time.sleep(2)
    device.shell('input tap 220 1850')
    time.sleep(5)
    for i in range(1, 7):
        device.shell("input keyevent KEYCODE_POWER")
        time.sleep(2)
        i += 1
        print(i)
    device.shell("input swipe 550 1700 550 380 1000")
    # 判断手机是否解锁成功
    result = get_lock_screen_state(device)
    while result:
        os.popen("adb shell input swipe 550 1700 550 380 1000")
        time.sleep(2)
        result = get_lock_screen_state(device)
        print result
        if result == False:
            break
    time.sleep(2)

def cut_resources3():
    device.shell('am start com.bbk.theme/com.bbk.theme.ResListActivity')
    time.sleep(2)
    device.shell('input tap 520 660')
    time.sleep(2)
    device.shell('input tap 220 1850')
    time.sleep(5)
    for i in range(1, 7):
        device.shell("input keyevent KEYCODE_POWER")
        time.sleep(2)
        i += 1
        print(i)
    device.shell("input swipe 550 1700 550 380 1000")
    time.sleep(2)
    result = True
    while result:
        os.popen('adb shell input swipe 550 1700 550 380')
        time.sleep(2)
        result = get_lock_screen_state(device)
        print result
        time.sleep(2)

if __name__ == '__main__':
    for i in range(0, 50):
        cut_resources1()
        cut_resources2()
        cut_resources3()
        print ('运行次数='+ str(i))
