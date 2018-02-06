# Author: AdrianZhang
# Coding Time: 2018/02/06
# Script Function: Through this script, you can get before time, current time and after time.

import time
from datetime import datetime

def before_time():
    history_time = time.mktime(datetime.now().timetuple()) - times
    before_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(history_time))
    return history_time, before_time

def current_time():
    now_time = time.mktime(datetime.now().timetuple())
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now_time))
    return now_time, current_time

def after_time():
    future_time = time.mktime(datetime.now().timetuple()) + times
    after_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(future_time))
    return future_time, after_time

if __name__ == '__main__':
    times = 60 * 3  # total: 3 minutes
    before_time = before_time()
    current_time = current_time()
    after_time = after_time()
    print("Before Time: \n{}\n{}\n".format(before_time[0], before_time[1]))
    print("Current Time: \n{}\n{}\n".format(current_time[0], current_time[1]))
    print("After Time: \n{}\n{}\n".format(after_time[0], after_time[1]))

