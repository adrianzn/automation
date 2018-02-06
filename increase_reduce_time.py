# Author: AdrianZhang
# Coding Time: 2018/02/06
# Script Function: Increase and reduce the time.

import time
from datetime import datetime

def time_count(times):
    current_time = time.mktime(datetime.now().timetuple())
    future_time = time.mktime(datetime.now().timetuple()) + times
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time))
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(future_time))
    return current_time, future_time, start_time, end_time

if __name__ == '__main__':
    times = 60 * 3  # total: 3 minutes
    time_result = time_count(times)
    print('Start Time: {} >>> {}'
          '\nEnd   Time: {} >>> {}'.format(time_result[0], time_result[2], time_result[1], time_result[3]))

