#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from adbtools import AdbTools
from adbtools import KeyCode
import time


device_name = '8BN0217830008829'
def key_code(device):
    '''
    挂断电话
    :param device: 设备号
    :return:
    '''
    keycode =KeyCode.KEYCODE_ENDCALL
    hangup = device.shell('input keyevent %s' % keycode)
    return hangup


def phone_number():

    '''
    电话本
    :return:电话本列表
    '''
    with open('C:/Users/admin/Desktop/callnumber.txt') as phonebook:
        numbers = phonebook.read().splitlines()
        phonebook.close()
        PHONE = []
        for num in numbers:
            PHONE.append(num)
    return PHONE


def get_display_state(self):
    """
    获取屏幕状态
    :return: 亮屏/灭屏
    """
    l = self.shell('dumpsys power').readlines()
    for i in l:
        if 'Display Power' in i:
            return 'ON' in i.split('=')[-1].upper()

def screen_status():
    device =AdbTools(device_name)
    if not get_display_state(device):
        device.shell('input keyevent %s' % '26')
        time.sleep(1)
        device.shell('input swipe 280 1618 990 1495')
        time.sleep(1)
    else:
        pass





if __name__ == '__main__':
    device = AdbTools(device_name)
    #判断屏幕状态并解锁
    screen_status()
    device.shell('am start %s' % 'com.android.contacts/.activities.DialtactsActivity')
    time.sleep(2)
    for phone in phone_number():
        #拨打电话
        device.call(phone)
        time.sleep(1)
        #截图
        device.screenshot(phone,'f:/work')
        time.sleep(3)
        #挂断电话
        key_code(device)
        time.sleep(1)
        #回到home界面
        device.send_keyevent(KeyCode.KEYCODE_HOME)
        time.sleep(2)














