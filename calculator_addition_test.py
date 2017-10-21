# Author: AdrianZhang
# Script function: 测试计算器的加法功能：“1+7=”的结果。
# Coding Time: 2017/10/21

import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'

calculate = 1 + 7

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
driver.find_element_by_id('com.android.calculator2:id/op_add').click()
driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
driver.find_element_by_id('com.android.calculator2:id/eq').click()
time.sleep(1)
result = driver.find_element_by_id('com.android.calculator2:id/result').text

try:
    if result == str(calculate):
        print("Addition: 1 + 7 = {} is Pass!".format(result))
    else:
        print("Calculation is wrong!")
except Exception as msg:
    print(msg)

driver.quit()
