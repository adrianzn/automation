# Author: AdrianZhang
# Script function: Android计算器的冒烟测试：(整数，小数、负数)的加法、减法、乘法、除法，输入、删除功能。
# Coding Time: 2017/10/23

import time
from appium import webdriver

def device_info():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.1'
    desired_caps['deviceName'] = 'emulator-5554'
    desired_caps['appPackage'] = 'com.android.calculator2'
    desired_caps['appActivity'] = '.Calculator'
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'
    return desired_caps

class CalculatorSmoke(object):
    def __init__(self):
        self.desired_caps = device_info()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def addition_integers(self):
        # 整数加法："1 + 7"
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        addition_integers_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if addition_integers_result == str(addition_integers_correct_value):
                print("Addition Integers: {} = {} is Pass!".format(addition_integers_demo, addition_integers_result))
            else:
                print("Addition Integers {} calculation is wrong!".format(addition_integers_demo))
        except Exception as msg:
            print(msg)

    def addition_decimals(self):
        # 小数加法："0.1 + 0.7"
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        addition_decimals_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if addition_decimals_result == str(addition_decimals_correct_value):
                print("Addition Decimals: {} = {} is Pass!".format(addition_decimals_demo, addition_decimals_result))
            else:
                print("Addition Decimals {} calculation is wrong!".format(addition_decimals_demo))
        except Exception as msg:
            print(msg)

    def addition_negative(self):
        # 负数加法："-1 + (-7)"
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.swipe(1060, 1300, 300, 1300, 1000)      # 左滑
        self.driver.find_element_by_id('com.android.calculator2:id/lparen').click()
        self.driver.swipe(300, 1300, 1060, 1300, 1000)      # 右滑
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.driver.swipe(1060, 1300, 300, 1300, 1000)      # 左滑
        self.driver.find_element_by_id('com.android.calculator2:id/rparen').click()
        self.driver.swipe(300, 1300, 1060, 1300, 1000)      # 右滑
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        addition_negative_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if addition_negative_result == str(addition_negative_correct_value):
                print("Addition Negative: {} = {} is Pass!".format(addition_negative_demo, addition_negative_result))
            else:
                print("Addition Negative {} calculation is wrong!".format(addition_negative_demo))
        except Exception as msg:
            print(msg)

    def subtraction_integers(self):
        # 整数减法："6 - 2"
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        subtraction_integers_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if subtraction_integers_result == str(subtraction_integers_correct_value):
                print("Subtraction Integers: {} = {} is Pass!".format(subtraction_integers_demo, subtraction_integers_result))
            else:
                print("Subtraction Integers {} calculation is wrong!".format(subtraction_integers_demo))
        except Exception as msg:
            print(msg)

    def subtraction_decimals(self):
        # 小数减法："0.6 - 0.2"
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        subtraction_decimals_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if subtraction_decimals_result == str(subtraction_decimals_correct_value):
                print("Subtraction Decimals: {} = {} is Pass!".format(subtraction_decimals_demo, subtraction_decimals_result))
            else:
                print("Subtraction Decimals {} calculation is wrong!".format(subtraction_decimals_demo))
        except Exception as msg:
            print(msg)

    def subtraction_negative(self):
        # 负数减法："-6 - (-2)"
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.swipe(1060, 1300, 300, 1300, 1000)      # 左滑
        self.driver.find_element_by_id('com.android.calculator2:id/lparen').click()
        self.driver.swipe(300, 1300, 1060, 1300, 1000)      # 右滑
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.driver.swipe(1060, 1300, 300, 1300, 1000)      # 左滑
        self.driver.find_element_by_id('com.android.calculator2:id/rparen').click()
        self.driver.swipe(300, 1300, 1060, 1300, 1000)      # 右滑
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        subtraction_negative_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if subtraction_negative_result == str(subtraction_negative_correct_value):
                print("Subtraction Negative: {} = {} is Pass!".format(subtraction_negative_demo, subtraction_negative_result))
            else:
                print("Subtraction Negative {} calculation is wrong!".format(subtraction_negative_demo))
        except Exception as msg:
            print(msg)

    def multiplication_integers(self):
        # 整数乘法："5 * 4"
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        multiplication_integers_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if multiplication_integers_result == str(multiplication_integers_correct_value):
                print("Multiplication Integers: {} = {} is Pass!".format(multiplication_integers_demo, multiplication_integers_result))
            else:
                print("Multiplication Integers {} calculation is wrong!".format(multiplication_integers_demo))
        except Exception as msg:
            print(msg)

    def multiplication_decimals(self):
        # 小数乘法："0.5 * 0.4"
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        multiplication_decimals_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if multiplication_decimals_result == str(multiplication_decimals_correct_value):
                print("Multiplication Decimals: {} = {} is Pass!".format(multiplication_decimals_demo, multiplication_decimals_result))
            else:
                print("Multiplication Decimals {} calculation is wrong!".format(multiplication_decimals_demo))
        except Exception as msg:
            print(msg)

    def multiplication_negative(self):
        # 负数乘法："-5 * 4"
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        multiplication_negative_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if multiplication_negative_result == str(multiplication_negative_correct_value):
                print("Multiplication Negative: {} = {} is Pass!".format(multiplication_negative_demo, multiplication_negative_result))
            else:
                print("Multiplication Negative {} calculation is wrong!".format(multiplication_negative_demo))
        except Exception as msg:
            print(msg)

    def division_integers(self):
        # 整数除法："9 / 3"
        self.driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        division_integers_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if division_integers_result == str(division_integers_correct_value):
                print("Division Integers: {} = {} is Pass!".format(division_integers_demo, division_integers_result))
            else:
                print("Division Integers {} calculation is wrong!".format(division_integers_demo))
        except Exception as msg:
            print(msg)

    def division_decimals(self):
        # 小数除法："0.9 / 0.3"
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        division_decimals_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if division_decimals_result == str(division_decimals_correct_value):
                print("Division Decimals: {} = {} is Pass!".format(division_decimals_demo, division_decimals_result))
            else:
                print("Division Decimals {} calculation is wrong!".format(division_decimals_demo))
        except Exception as msg:
            print(msg)

    def division_negative(self):
        # 负数除法："-9 / 3"
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        division_negative_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if division_negative_result == str(division_negative_correct_value):
                print("Division Negative: {} = {} is Pass!".format(division_negative_demo, division_negative_result))
            else:
                print("Division Negative {} calculation is wrong!".format(division_negative_demo))
        except Exception as msg:
            print(msg)

#    def input_button(self):
#        pass

#    def delete_button(self):
#        pass

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    calculator = CalculatorSmoke()

    # 整数加法： addition_integers
    addition_integers_demo = "1 + 7"
    addition_integers_correct_value = 8
    addition_integers = calculator.addition_integers()
    # 小数加法： addition_decimals
    addition_decimals_demo = "0.1 + 0.7"
    addition_decimals_correct_value = 0.8
    addition_decimals = calculator.addition_decimals()
    # 负数加法： addition_negative
    addition_negative_demo = "-1 + (-7)"
    addition_negative_correct_value = -8
    addition_negative = calculator.addition_negative()

    # 整数减法：subtraction_integers
    subtraction_integers_demo = "6 - 2"
    subtraction_integers_correct_value = 4
    subtraction_integers = calculator.subtraction_integers()
    # 小数减法：subtraction_decimals
    subtraction_decimals_demo = "0.6 - 0.2"
    subtraction_decimals_correct_value = 0.4
    subtraction_decimals = calculator.subtraction_decimals()
    # 负数减法：subtraction_negative
    subtraction_negative_demo = "-6 - (-2)"
    subtraction_negative_correct_value = -4
    subtraction_negative = calculator.subtraction_negative()

    # 整数乘法：multiplication_integers
    multiplication_integers_demo = "5 * 4"
    multiplication_integers_correct_value = 20
    multiplication_integers = calculator.multiplication_integers()
    # 小数乘法：multiplication_decimals
    multiplication_decimals_demo = "0.5 * 0.4"
    multiplication_decimals_correct_value = 0.2
    multiplication_decimals = calculator.multiplication_decimals()
    # 负数乘法：multiplication_negative
    multiplication_negative_demo = "-5 * 4"
    multiplication_negative_correct_value = -20
    multiplication_negative = calculator.multiplication_negative()

    # 整数除法：division_integers
    division_integers_demo = "9 / 3"
    division_integers_correct_value = 3
    division_integers = calculator.division_integers()
    # 小数除法：division_decimals
    division_decimals_demo = "0.9 / 0.3"
    division_decimals_correct_value = 3
    division_decimals = calculator.division_decimals()
    # 负数除法：division_negative
    division_negative_demo = "-9 / 3"
    division_negative_correct_value = -3
    division_negative = calculator.division_negative()

    calculator.quit()

"""
    # input 0,1,2,3,4,5,6,7,8,9
    input_button_0 = "0"
    input_button_1 = "1"
    input_button_2 = "2"
    input_button_3 = "3"
    input_button_4 = "4"
    input_button_5 = "5"
    input_button_6 = "6"
    input_button_7 = "7"
    input_button_8 = "8"
    input_button_9 = "9"
    input_button_0_correct_value = 0
    input_button_1_correct_value = 1
    input_button_2_correct_value = 2
    input_button_3_correct_value = 3
    input_button_4_correct_value = 4
    input_button_5_correct_value = 5
    input_button_6_correct_value = 6
    input_button_7_correct_value = 7
    input_button_8_correct_value = 8
    input_button_9_correct_value = 9
    input_button = calculator.input_button()

    # delete 0,1,2,3,4,5,6,7,8,9
    delete_button = calculator.delete_button()
"""
