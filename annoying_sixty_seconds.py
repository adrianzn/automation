# Author: AdrianZhang
# Coding Time: 2017/10/18
# Script Function: “故君子之治人也，即以其人之道，还治其人之身。”

import time
from selenium import webdriver

class Control(object):
    def __init__(self, count):
        self.message_send = MessageSend()
        self.counter = count

    def get_current_time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return current_time

    def single_test(self):
        self.message_send.zhihu_message()
        current_time = self.get_current_time()
        print("No.{}  [Send To:] {} ({})".format(self.counter, phone_number, current_time))

    def many_times_test(self):
        while self.counter > 0:
            self.single_test()
            self.counter -= 1
        if self.counter == 0:
            self.message_send.quit_chrome()


class MessageSend(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def zhihu_message(self):
        self.driver.maximize_window()
        self.driver.get(zhihu_url)
        self.driver.find_element_by_xpath("//*[@class='AppHeader-profile']/div/button").click()
        self.driver.find_element_by_xpath("//*[@class='Modal-inner']/div/div/form/div[4]/button").click()
        self.driver.find_element_by_xpath("//*[@class='Modal-inner']/div/div/form/div/div[2]/div/input").click()
        self.driver.find_element_by_xpath("//*[@class='Modal-inner']/div/div/form/div/div[2]/div/input").clear()
        self.driver.find_element_by_xpath("//*[@class='Modal-inner']/div/div/form/div/div[2]/div/input").send_keys(phone_number)
        self.driver.find_element_by_xpath("//*[@class='Modal-inner']/div/div/form/div[3]/button").click()
        time.sleep(1)

    def quit_chrome(self):
        self.driver.quit()

if __name__ == '__main__':
    times = 5
    phone_number = "***********"
    zhihu_url = "https://www.zhihu.com/question/24191741"
    controler = Control(times)
    controler.many_times_test()

    
