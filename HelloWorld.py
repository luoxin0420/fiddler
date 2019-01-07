#!/usr/bin/python3
import os
import re


def get_event_max_value(cmd):
    event_out_message = ''.join(os.popen(cmd).read().split())
    for message in event_out_message.split(","):
        if "max" in message:
            return int(message[3:])
    return 0


def get_screen_display_resolution_value(event_width, event_height):
    screen_resolution_message = os.popen("adb shell dumpsys window displays | findstr cur=").read()
    cur_index = screen_resolution_message.index("cur")
    return screen_resolution_message[cur_index+4:cur_index+len(str(event_width))+len(str(event_height))+5]


def get_touch_message():
    out_message = os.popen("adb shell getevent -c 6 | findstr /c:0035 /c:0036").read()
    print(out_message)
    start_touch_x, start_touch_y = 0, 0
    for message in out_message.split("\n"):
        if "0035" in message:
            touch_width_list = re.split(r" +", message)
            start_touch_x = int(touch_width_list[len(touch_width_list) - 1], 16)

        if "0036" in message:
            touch_width_list = re.split(r" +", message)
            start_touch_y = int(touch_width_list[len(touch_width_list) - 1], 16)
    touch_list = [start_touch_x, start_touch_y]
    return touch_list


def start():
    touch_list = get_touch_message()
    event_width = get_event_max_value("adb shell getevent -p | findstr /c:0035")
    event_height = get_event_max_value("adb shell getevent -p | findstr /c:0036")
    screen_resolution_message = get_screen_display_resolution_value(event_width, event_height)
    screen_display_data_list = screen_resolution_message.split("x")
    rate_width = int(screen_display_data_list[0])/event_width
    rate_height = int(screen_display_data_list[1])/event_height
    touch_x = touch_list[0]*rate_width
    touch_y = touch_list[1]*rate_height
    print("touch_x = "+str(touch_x)+" , touch_y = "+str(touch_y))
    return


start()
