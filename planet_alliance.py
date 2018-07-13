# Author: AdrianZhang
# Coding Time: 2018/07/12
# Script Function: A script for get more integral star coin.

import os
import random
import time
from datetime import datetime


def get_screen_size():
    try:
        adb_log = os.popen("adb shell wm size").readlines()
        for size in adb_log:
            if "Physical size:" in size:
                resolution = size.split(": ")[-1].strip("\n")
                x_size = int(resolution.split("x")[0])
                y_size = int(resolution.split("x")[-1])
                return x_size, y_size
    except Exception as error:
        print(error)


def up_swipe():
    location = get_screen_size()
    x_start = location[0] * 0.5
    y_start = location[-1] * 0.75
    x_end = location[0] * 0.5
    y_end = location[-1] * 0.25
    os.popen("adb shell input swipe {} {} {} {}".format(x_start, y_start, x_end, y_end))


def down_swipe():
    location = get_screen_size()
    x_start = location[0] * 0.5
    y_start = location[-1] * 0.25
    x_end = location[0] * 0.5
    y_end = location[-1] * 0.75
    os.popen("adb shell input swipe {} {} {} {}".format(x_start, y_start, x_end, y_end))


def left_swipe():
    location = get_screen_size()
    x_start = location[0] * 0.75
    y_start = location[-1] * 0.5
    x_end = location[0] * 0.25
    y_end = location[-1] * 0.5
    os.popen("adb shell input swipe {} {} {} {}".format(x_start, y_start, x_end, y_end))


def right_swipe():
    location = get_screen_size()
    x_start = location[0] * 0.25
    y_start = location[-1] * 0.5
    x_end = location[0] * 0.75
    y_end = location[-1] * 0.5
    os.popen("adb shell input swipe {} {} {} {}".format(x_start, y_start, x_end, y_end))


def operate_app(test_time):
    os.popen("adb shell am start -W -n com.browser2345/.StartBrowserActivity")
    time.sleep(5)
    
    start_time_calculation = time.mktime(datetime.now().timetuple())
    start_time_read = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time_calculation))
    print("{} >>> 任务开始时间".format(start_time_read))
    
    end_time_calculation = start_time_calculation + test_time
    end_time_read = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time_calculation))
    print("{} >>> 任务结束时间\n".format(end_time_read))
    
    time.sleep(3)
    time_num = 0
    while start_time_calculation < end_time_calculation:
        seconds = random.randint(5, 15)
        time_num += 1
        print("{} >>> 这是第 {} 次测试".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), time_num))
        
        time.sleep(seconds)
        down_swipe()
        print("{} >>> 下拉刷新完成".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

        time.sleep(seconds)
        location = get_screen_size()
        x = location[0] * 0.5
        y = location[-1] * 0.2
        os.popen("adb shell input tap {} {}".format(x, y))
        print("{} >>> 点击资讯完成".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

        time.sleep(seconds)
        up_swipe()
        print("{} >>> 浏览资讯完成".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

        time.sleep(seconds)
        os.popen("adb shell input keyevent KEYCODE_BACK")
        print("{} >>> 返回前页完成\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        
        start_time_calculation = time.mktime(datetime.now().timetuple())
    print("{} >>> 任务结束".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    os.popen("adb shell am force-stop com.browser2345")


if __name__ == '__main__':
    test_time = 60 * 60 * 24  # 1 day
    operate_app(test_time)


