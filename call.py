__author__ = 'Administrator'
 #-*- coding: UTF-8 -*-
import adbtools
import os
import time

def call_number(number):

    device.call(number)

if __name__ == '__main__':

    device = adbtools.AdbTools('c248f4b7')
    state = device.get_display_state()
    stage_devices = device.get_device_state()
    result = device.adb(26)
    cmd = 'input keyevent 26'
    # if state:
    #     call_number('13920407303')
    #     time.sleep(2)
    #     device.screenshot('1.png','e:/1')
    #     time.sleep(1)
    #     print('OK')
    #     device.shell('input keyevent 6')
    #     time.sleep(2)
    #     device.shell('input keyevent 3')
    # else:
    #     device.shell('input keyevent 26')
    #     time.sleep(1)
    #     os.popen('adb shell input swipe 700 2500 700 300')
    #     time.sleep(2)
    #     print ('lock success')
    # name = "device"
# for name  in stage_devices:
    if stage_devices:
        if not state:
            device.shell('input keyevent 26')
            time.sleep(1)
            os.popen('adb shell input swipe 700 2500 700 300')
            time.sleep(2)
            print ('lock success')
        call_number('13920407303')
        time.sleep(5)
        device.screenshot('1.png','e:/1')
        time.sleep(1)
        print('OK')
        device.shell('input keyevent 6')
        time.sleep(2)
        device.shell('input keyevent 3')
    else:
        print ("no devices")












