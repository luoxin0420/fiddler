__author__ = 'Administrator'
# coding: utf-8
import adbtools
import os
import datetime
import time

def command():
    with open('E:/1/monkey.txt') as file:
        data = file.readlines()
        str = ''.join(data)
        file.close()
    print(str)
    os.popen(str)

def write_result():
    format_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'e:/1/'
    filename = 'monkey_run.txt'
    end_name = format_time + filename
    os.rename(path + filename, path + end_name)
    print (end_name)

if __name__ == '__main__':
    device = adbtools.AdbTools('c248f4b7')
    command()
    write_result()



