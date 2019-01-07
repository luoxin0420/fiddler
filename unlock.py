# -*- coding:utf-8 -*-
# coding:utf-8
from adbtools import AdbTools
import os
import time

devices = '3449aa7b'
file1 = 'E:/11/file1.txt'
file2 = 'E:/11/file2.txt'
file3 = 'E:/11/file3.txt'
file4 = 'E:/11/file4.txt'
# 获取设备状态
def get_device_state(self):
    return self.adb('get-state').read().strip()


# 获取屏幕状态
def get_display_state(self):
    l = self.shell('dumpsys power').readlines()
    for i in l:
        if 'Display Power' in i:
            return 'ON' in i.split('=')[-1].upper()


# 内存泄漏-解锁
def device_state():
        if get_device_state(device):
            get_display_state(device)
            if not get_display_state(device):
                device.shell('input keyevent 26')
                time.sleep(2)
                os.popen('adb shell input swipe 311 2022 950 2040')
                time.sleep(2)
                # 取出单值
                # device.shell(('dumpsys meminfo  com.android.systemui > ') + file1)
                # with open(file1, 'r') as f:
                    # lines = f.readlines()
                    # line=f.readlines()[0].split()[0]
                    # wf = open(file2, 'a')
                    # wf.write(line + '\n')
                    # wf.close()
                    # device.shell('input keyevent 26')
                    # time.sleep(2)
                # 去除所有值
                # device.shell(('dumpsys meminfo  com.android.systemui > ') + file4)
                # device.shell('input keyevent 26')
                # time.sleep(2)
                a = device.shell('dumpsys meminfo com.android.systemui')
                print a
                f = open(a, 'r')
                lines=f.readlines()
                with open(file4, 'a') as f1:
                    # lines=f1.readline()
                    # for line in lines:
                        f1.write(lines)
                device.shell('input keyevent 26')
                time.sleep(2)



# 内存泄漏-切换
def change():
    if get_device_state(device):
            get_display_state(device)
            if not get_display_state(device):
                device.shell('input keyevent 26')
                time.sleep(2)
                os.popen('adb shell input swipe 500 1800 500 500')
                time.sleep(2)
    device.shell(('dumpsys meminfo | findstr com.android.systemui > ') + file1)
    with open(file1, 'r') as f:
        line=f.readlines()[0].split()[0]
        wf = open(file3, 'a')
        wf.write(line + '\n')
        wf.close()
    device.shell('am start com.example.vivotest/.StartActivity bnds')
    time.sleep(2)
    device.shell('am start com.example.vivotest/com.example.vivotheme.MainActivity')
    time.sleep(2)
    os.popen('adb shell input tap 1020 660')
    time.sleep(10)
    device.shell('am start com.example.vivotest/.StartActivity bnds')
    time.sleep(2)
    device.shell('am start com.example.vivotest/com.example.vivotheme.MainActivity')
    time.sleep(2)
    os.popen('adb shell input tap 1000 890')
    time.sleep(5)
    device.shell('input keyevent 26')
    time.sleep(2)





if __name__ == '__main__':
    device = AdbTools(devices)
    # get_device_stat# e(device)
    # get_display_state(device)
    for i in range(2000):
        device_state()
    # for j in range(2000):
    #     change()













