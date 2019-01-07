# -*- coding:utf-8 -*-
# coding:utf-8
from adbtools import AdbTools
import os
import time

devices = 'c248f4b7'
# def adb(self, args):
#     cmd = "%s %s %s" % (self.__command, self.__device_id, str(args))
#     return os.popen(cmd)

# 获取设备状态
def get_device_state(self):
    return self.adb('get-state').read().strip()

# 获取屏幕状态
def get_display_state(self):
    l = self.shell('dumpsys power').readlines()
    for i in l:
        if 'Display Power' in i:
            return 'ON' in i.split('=')[-1].upper()
# 解锁
def device_state():
    device = AdbTools(devices)
    if get_device_state(device):
        get_display_state(device)
        if not get_display_state(device):
            device.shell('input keyevent 26')
            time.sleep(1)
            os.popen('adb shell input swipe 700 2500 700 300')
            time.sleep(2)
            print ('lock success')
    else:
        print ('no devices')



if __name__ == '__main__':
    # device = adbtools.AdbTools('ZX1G426D5C')
    # adb = device.adb('get-state')
    device = AdbTools(devices)
    # state = get_display_state(device)
    # if not state:
    #     print ('lock success')
    device_state()











