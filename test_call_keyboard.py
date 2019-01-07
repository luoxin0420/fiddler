#!usr/bin/env python 
# -*-coding: UTF-8 -*-

import os
import time
import sys
# from uiautomator import Device as d

class Phone_call():
	def call(self):
		os.system('adb devices')
		#d = Device('0123456789ABCDEF')
		#唤醒屏幕
		#self.d.screen.on()
		os.system('adb shell input keyevent 224')

		#滑动解锁
		os.system('adb shell input swipe 500 1700 500 400')
		time.sleep(2)
		#启动拨号程序进程
		os.system('adb shell am start -n com.android.dialer/.TwelveKeyDialer')
		#从文件读取号码并拨号
		Number = []
		fd = file('E:\test\number.txt','r')
		for line in fd.readlines():
			Number.append(list(map(int,line.split(','))))
		print(Number)
		for item in Number:
			for it in item:
				os.system('adb shell am start -a android.intent.action.CALL -d tel:%s'% it)
				time.sleep(2)
				#截图并保存到pc
				os.system('adb shell screencap -p /sdcard/screen.png')
				os.system('adb pull /sdcard/screen.png E:\test\picture')
				self.rename_file('E:\test\picture\screen.png')
				#挂断
				self.choice_function_key('HUNGUP')
				#返回主界面
				self.choice_function_key('HOME')
	def choice_function_key(self,key):
		if key == 'call':
			os.system('adb shell input tap 550 1700')
		#回到HOME界面
		if key == 'HOME':
			os.system('adb shell input keyevent 3')
		if key == 'HUNGUP':
			os.system('adb shell input tap 550 1700')
	def add_timestamp(self):
		stamp = time.strftime("%Y%m%d%H%M%S",time.localtime())
		return(stamp)
	def rename_file(self,filename_without_timestamp):
		#分离文件名与扩展名
		(file_without_suff,extention) = os.path.splitext(filename_without_timestamp)  
		stamp = self.add_timestamp()  
		file_add_timestamp = file_without_suff + stamp  
		file_with_timestamp =  file_add_timestamp + extention  
		# print filename_without_timestamp,file_with_timestamp  
		os.rename(filename_without_timestamp,file_with_timestamp)

if __name__=="__main__":
	Recurse=input('Please enter recurse time:')
	while Recurse>0:
		dialer=Phone_call()
		dialer.call()
		Recurse=Recurse-1

