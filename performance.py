#!/usr/bin/evn python
# -*- coding:utf-8 -*-


from adbtools import AdbTools
import time
import datetime
from matplotlib import pyplot
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyExcelerator import*


# 设置前提条件
device_name = 'ed4df090'    # device 序列号
package_name = 'dscreate.net.lwp304290.hw'     # 包名
way = 'right'  # 解锁方式，可选择left,right,up,down
running_times = 2000


class CreatChart(object):
    # 生成表格
    def __init__(self, cpu_data, mem_data):
        self.cpu_data_excel = cpu_data
        self.mem_data_excel = mem_data
        self.cpu_data_chart = map(lambda x: float(x[:-1]) / 100, cpu_data)
        self.mem_data_chart = map(lambda x: int(x), mem_data)

    def get_excel(self, description):
        # 得到的cpu/mem数据写入到表格
        w = Workbook()   # 创建一个工作薄
        cpu = w.add_sheet('cpu_repeat_on_off')    # 创建cpu工作表
        mem = w.add_sheet('mem_full_operation')    # 创建内存工作表
        fname = Write_file.get_file_name('f:/huawei/performance', '.xls')
        n = len(self.cpu_data_excel)
        m = len(self.mem_data_excel)
        if description == 'cpu':
            for j in range(1):   # 控制列并生成cpu的sheet页
                i = 0
                cpu.write(i, j, 'cpu')
                for i in range(1, n+1):   # 控制行
                    cpu.write(i, j, cpu_data[i-1])
        elif description == 'mem':
            for j in range(1):    # 控制列并生成memory的sheet页
                i = 0
                mem.write(i, j, 'memory')
                for i in range(1, m+1):
                    mem.write(i, j, mem_data[i-1])
        else:
            pass

        w.save(fname)

    def line_chart(self, description):
        # 绘制cpu/mem折线图
        if description == 'cpu':
            times = range(1, len(self.cpu_data_chart) + 1)  # 定义横坐标
            # print time
            rate = self.cpu_data_chart  # 定义纵坐标
            #        print(rate)
            pyplot.plot(times, rate)  # 生成图表
            pyplot.xlabel('times')  # 执行次数为横坐标
            pyplot.ylabel('usage_rate')  # 得到的数值为纵坐标
            pyplot.title('the cpu usage rate')  # 标题为cpu使用率
            # pyplot.fill_between(time,rate,0,color = 'green')
            #  设置填充选项
            pyplot.grid(True)
            fname = Write_file.get_file_name('f:/huawei/cpu', '.png')
            # pyplot.show()
            pyplot.savefig(fname)  # 保存图表
            pyplot.close()
        elif description == 'mem':
            times = range(1, len(self.mem_data_chart) + 1)  # 定义横坐标
            # print time
            mem = self.mem_data_chart  # 定义纵坐标
            # print(mem)
            pyplot.plot(times, mem)  # 生成图表
            pyplot.xlabel('times')  # 执行次数为横坐标标签
            pyplot.ylabel('memory(kb)')  # 得到的数值为纵坐标标签
            pyplot.title('the memory change chart')  # 标题为cpu使用率
            # pyplot.fill_between(time, mem, 0, color='blue')  # 设置填充选项
            pyplot.grid(True)
            fname = Write_file.get_file_name('f:/huawei/mem', '.png')
            # pyplot.show()
            pyplot.savefig(fname)  # 保存图表
            pyplot.close()


class DataProcessing(object):
    """
         处理读取的数据
    """
    def __init__(self, cpu_data, mem_data):
        # 初始化
        self.cpu_data = cpu_data
        self.mem_data = mem_data

    def average(self, description):
        if description == 'cpu':
            # 计算cpu的均值
            avg = 0
            n = len(self.cpu_data)
            cpu_data_change = map(lambda x: float(x[:-1]) / 100, self.cpu_data)
            for num in cpu_data_change:
                avg += num / n
            return "%.2f%%" % (avg * 100)
        if description == 'mem':
            # 计算mem均值
            avg = 0
            n = len(self.mem_data)
            mem_data_change = map(lambda x: int(x), self.mem_data)
            for num in mem_data_change:
                avg += num / n
            return avg


class Action(object):
    """
    上下左右滑动
    """
    def __init__(self, device):
        self.device = device
        self.width = int(self.device.get_screen_normal_size()[0])
        self.height = int(self.device.get_screen_normal_size()[-1])

    def left_swipe(self, t):
        x1 = int(self.width * 0.9)
        y1 = int(self.height * 0.8)
        x2 = int(self.width * 0.1)
        self.device.shell('input swipe %d %d %d %d %d' % (x1, y1, x2, y1, t))

    def right_swipe(self, t):
        x1 = int(self.width * 0.25)
        y1 = int(self.height * 0.8)
        x2 = int(self.width * 0.75)
        self.device.shell('input swipe %d %d %d %d %d' % (x1, y1, x2, y1, t))

    def up_swipe(self, t):
        x1 = int(self.width * 0.5)
        y1 = int(self.height * 0.8)
        y2 = int(self.width * 0.4)
        self.device.shell('input swipe %d %d %d %d %d' % (x1, y1, x1, y2, t))

    def down_swipe(self, t):
        x1 = int(self.width * 0.25)
        y1 = int(self.height * 0.25)
        y2 = int(self.width * 0.75)
        self.device.shell('input swipe %d %d %d %d %d' % (x1, y1, x1, y2, t))

    def click(self):
        x = int(self.width * 0.3)
        y = int(self.height * 0.25)
        self.device.shell('input tap %d %d' % (x, y))


class TestCase():
    """
    测试步骤与数据获取
    """
    def __init__(self, device):
        self.device = device
        self.action = Action(self.device)

    def get_cpu_data_top(self):
        # 获取cpu数据
        data_string = self.device.shell('top -n 1| findstr %s' % package_name).read()
        data_list = data_string.split()
        cpu = data_list[2]
        return cpu

    def get_mem_data_dump(self):
        # 获取内存数据
        mem_string = self.device.shell('dumpsys meminfo | findstr %s' % package_name).read()
        mem_list = mem_string.split()
        mem = mem_list[0]
        return mem

    def _unlock_map(self, act, value):
        self.func_dict = {'left': self.action.left_swipe,
                          'right': self.action.right_swipe,
                          'up': self.action.up_swipe,
                          'down': self.action.down_swipe}
        return self.func_dict[act](value)
        # if way == 'left':
        #     self.swipe.left_swipe(200)
        # elif way == 'right':
        #     self.swipe.right_swipe(200)
        # elif way == 'up':
        #     self.swipe.up_swipe(200)
        # elif way == 'down':
        #     self.swipe.down_swipe(200)
        # else:
        #     print('please select unlock way')

    def unlock(self):
        """
        解锁到桌面
        :return:
        """
        device_id = self.device.get_devices()
#       # print device_id
        if device_id != 'None':
            if self.device.get_device_state() == 'device':
                if self.device.get_display_state():
                    if self.device.get_lock_screen_state():
                        self._unlock_map(way, 200)
                    else:
                        pass
                else:
                    self.device.send_keyevent(26)
                    self._unlock_map(way, 200)
            else:
                print('the device is not online')
        else:
            print('the device is not found')

    def cpu_repeat_screen_on_off(self):
        """
        测试步骤
        1、开机注册现网，关闭除测试工具外的后台程序
        2、按power键灭屏后进入待机
        3、等待5分钟使得系统稳定
        4、Power键亮屏解锁→2s后记录cpu值— > Power键灭屏→2s后开启下一次循环— > 循环200次：查看进程CPU情况，取平均值
        :return:cpu_data
        """

        cpu_data = []
        # self.device.reboot()
#        重启
#        time.sleep(60)
        self.unlock()
        self.device.send_keyevent(26)
        time.sleep(3)
#        等待5分钟使手机稳定
        for degree in range(running_times):
            # 主要操作
            self.unlock()
            time.sleep(2)
            cpu_data.append(self.get_cpu_data_top())
            self.device.send_keyevent(26)
            time.sleep(2)
        return cpu_data

    def full_memory(self):
        """
        1、重启手机—>等待3分钟手机稳定
        2、点击任意APP→home返回→点击屏幕任意位置→左右切换屏幕→上下滑动屏幕→home键返回
           →所有动作完成后1s后记录一次内存—>循环2000次：查看进程内存情况，取平均值（操作无间隔时间）
        :return:mem_data
        """
        mem_data = []
#        self.device.reboot()
        # 重启
#        time.sleep(60)
        self.unlock()
#       self.device.send_keyevent(26)
        time.sleep(3)
        # 等待3分钟使手机稳定
        for num in range(running_times):
            # 主要操作
            self.unlock()
            self.device.start_application('com.android.dialer/.BBKTwelveKeyDialer')
            self.device.send_keyevent(3)
            self.device.clear_app_data('com.android.dialer')     # 点击任意app
            self.action.click()    # 点击任意位置
            self.action.left_swipe(200)     # 滑动到下一屏
            self.device.send_keyevent(3)   # 防止滑动屏幕到最后一屏
            self.action.down_swipe(200)    # 下滑
            self.action.up_swipe(200)      # 上滑
            self.device.send_keyevent(3)
            time.sleep(1)
            mem_data.append(self.get_mem_data_dump())
        return mem_data


class Write_file(object):
    """
    文件按时间戳命名，写入文件
    """
    def get_file_name(self, file_path, file_type,):
        format_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        name = file_path + format_time + file_type
        return name

    def write_data(self, file_data, file_path, file_type):
        name = self.get_file_name(file_path, file_type)
        with open(name, 'a') as f:
            f.write(str(file_data))
            f.write('\n')

if __name__ == '__main__':
    device = AdbTools(device_name)    # AdbTools实例化
    test_case = TestCase(device)         # TestCase实例化
    file_name = Write_file()                # File实例化
    cpu_data = test_case.cpu_repeat_screen_on_off()   # 执行cpu测试用例并生成cpu数据
    mem_data = test_case.full_memory()     # 执行mem测试用例并生成mem数据
    data_processing = DataProcessing(cpu_data, mem_data)     # DataProcessing实例化
    chart = CreatChart(cpu_data, mem_data)    # 创建CreatChart实例化
    cpu_avg = data_processing.average('cpu')   # 求取cpu平均值并打印
    file_name.write_data(cpu_avg, 'f:/huawei/cpu', '.txt')
    print('The cpu of repeat screenON and screenOFF is', cpu_avg)
    mem_avg = data_processing.average('mem')    # 求取内存平均值并打印
    file_name.write_data(mem_avg, 'f:/huawei/mem_avg', '.txt')
    print('The memory of FULL operation is', mem_avg)
    chart.get_excel('cpu')
    chart.get_excel('mem')
    chart.line_chart('cpu')
    chart.line_chart('mem')


