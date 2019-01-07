#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import os,sys
import random
import selenium
from selenium import webdriver  # 导入webdriver包
import time
'''
游戏猜密码
name = "22"
passwd = "22"
print ("请输入用户名")
for x in range(3):
    username = raw_input('username:').strip()
    print ("请输入密码")
    user_password = raw_input('password:').strip()
    if user_password == passwd and username == name:
        print("希望这是最后一次")
        break
    else:
        print("傻逼，输入错误")


游戏猜拳
player = input('请输⼊：剪⼑(0) ⽯头(1) 布(2):')
player = int(player)
computer = random.randint(0,2)
if ((player == 0) and (computer == 2)) or ((player ==1) and (computer ==2)):
    print('获胜，哈哈，你太厉害了')
elif player == computer:
    print('平局，要不再来⼀局')
else:
    print('输了，不要走，洗洗⼿接着来，决战到天亮')


乘法口诀
i = 1
while i <= 9:
    j = 1
    sum = i*j
    while j <= i:
        print("%d*%d=%-2d "%(j,i,i*j))
        j += 1
    #print('\n')
    i += 1

i = 1
while i<=5:
    j = 1
    while j<=i:
        print("* ")
        j+=1
    print("\n")
    i+=1
    '''

# A = ['xiaoWang','xiaoZhang','xiaoHua']
# print("-----添加之前，列表A的数据-----")
# for tempName in A:
#     print(tempName)
#提示、并添加元素
# temp = raw_input('请输⼊要添加的学⽣姓名:')
# A.append(temp)
# print("-----添加之后，列表A的数据-----")
# for tempName in A:
#     print(tempName)

# 求每个字母个数
# str = "hello world"
# count = {}
# for item in str:
#     count[item] = count.get(item, 0) + 1
# print(count)

# 函数间的调用（可传参）
'''
def add2num(a, b,c):
    # 求参数个数
    yy = add2num.func_code.co_argcount
    return a+b+c, yy

def addavg(a, b,c):
    sum0 = add2num(a, b,c)
    sum = sum0[0]
    sum1 = sum0[1]
    avg = sum/sum1
    # return sum, avg
    print sum, '\n', avg
'''

def line(row):
    for i in range(1,row+1):
        print("{}*{}={}\t".format(i, row, i*row))
for row in range(1, 10):
    line(row)

if __name__ == '__main__':
    # add2num()
    # addavg(11, 22, 11)
    line(row)

# loadrunner网页测试
# driver = webdriver.Firefox() # 初始化一个火狐浏览器实例：driver
# driver.maximize_window() # 最大化浏览器
# time.sleep(5) # 暂停5秒钟
# driver.get("https://www.baidu.com") # 通过get()方法，打开一个url站点

# 打印行
# def line():
#     print('*' *30)
# def lines(num):
#     i =0
#     while i < num:
#         line()
#         i += 1
# lines(4)
