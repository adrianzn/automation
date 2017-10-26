# Author: AdrianZhang
# Coding Time: 2017/10/23
# Script Function: 
#    Android计算器的冒烟测试：(整数，小数、负数)的加法、减法、乘法、除法；
#    0的乘法、除法；0~9数字输入、删除功能。

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

    def number_button(self):
        """ Case-01: 输入0~9(number_button 0~9): 0,1,2,3,4,5,6,7,8,9 """
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
        number_button_result = self.driver.find_element_by_id('com.android.calculator2:id/formula').text
        time.sleep(1)
        for i in range(10):
            self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        try:
            if number_button_result == number_button_correct_value:
                print("Case-01: 输入0~9(number_button 0~9): {} = {} is Pass!".format(number_button_demo,
                                                                                   number_button_result))
            else:
                print("Case-01: 输入0~9(number_button 0~9): {} input is wrong!".format(number_button_demo))
        except Exception as msg:
            print(msg)

    def delete_button(self):
        """ Case-02: 删除0~9(delete_button 0~9) """
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        delete_button_result = self.driver.find_element_by_id('com.android.calculator2:id/formula').text
        time.sleep(1)
        try:
            if delete_button_result == delete_button_correct_value:
                print("Case-02: 删除0~9(delete_button 0~9): {} = {} is Pass!".format(delete_button_demo,
                                                                                   delete_button_result))
            else:
                print("Case-02: 删除0~9(delete_button 0~9): {} is wrong!".format(delete_button_demo))
        except Exception as msg:
            print(msg)

    def addition_integers(self):
        """ Case-03: 整数相加(addition_integers): '1 + 7' """
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        addition_integers_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if addition_integers_result == addition_integers_correct_value:
                print("Case-03: 整数相加(addition_integers): {} = {} is Pass!".format(addition_integers_demo, addition_integers_result))
            else:
                print("Case-03: 整数相加(addition_integers): {} calculation is wrong!".format(addition_integers_demo))
        except Exception as msg:
            print(msg)

    def addition_decimals(self):
        """ Case-04: 小数相加(addition_decimals): '0.1 + 0.7' """
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
            if addition_decimals_result == addition_decimals_correct_value:
                print("Case-04: 小数相加(addition_decimals): {} = {} is Pass!".format(addition_decimals_demo, addition_decimals_result))
            else:
                print("Case-04: 小数相加(addition_decimals): {} calculation is wrong!".format(addition_decimals_demo))
        except Exception as msg:
            print(msg)

    def addition_negative(self):
        """ Case-05: 负数相加(addition_negative): '−1 + (−7)' """
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
            if addition_negative_result == addition_negative_correct_value:
                print("Case-05: 负数相加(addition_negative): {} = {} is Pass!".format(addition_negative_demo, addition_negative_result))
            else:
                print("Case-05: 负数相加(addition_negative): {} calculation is wrong!".format(addition_negative_demo))
        except Exception as msg:
            print(msg)

    def subtraction_integers(self):
        """ Case-06: 整数相减(subtraction_integers): '6 − 2' """
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        subtraction_integers_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if subtraction_integers_result == subtraction_integers_correct_value:
                print("Case-06: 整数相减(subtraction_integers): {} = {} is Pass!".format(subtraction_integers_demo, subtraction_integers_result))
            else:
                print("Case-06: 整数相减(subtraction_integers): {} calculation is wrong!".format(subtraction_integers_demo))
        except Exception as msg:
            print(msg)

    def subtraction_decimals(self):
        """ Case-07: 小数相减(subtraction_decimals): '0.6 − 0.2' """
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
            if subtraction_decimals_result == subtraction_decimals_correct_value:
                print("Case-07: 小数相减(subtraction_decimals): {} = {} is Pass!".format(subtraction_decimals_demo, subtraction_decimals_result))
            else:
                print("Case-07: 小数相减(subtraction_decimals): {} calculation is wrong!".format(subtraction_decimals_demo))
        except Exception as msg:
            print(msg)

    def subtraction_negative(self):
        """ Case-08: 负数相减(subtraction_negative): '−6 − (−2)' """
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
            if subtraction_negative_result == subtraction_negative_correct_value:
                print("Case-08: 负数相减(subtraction_negative): {} = {} is Pass!".format(subtraction_negative_demo, subtraction_negative_result))
            else:
                print("Case-08: 负数相减(subtraction_negative): {} calculation is wrong!".format(subtraction_negative_demo))
        except Exception as msg:
            print(msg)

    def multiplication_integers(self):
        """ Case-09: 整数相乘(multiplication_integers): '5 * 4' """
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        multiplication_integers_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if multiplication_integers_result == multiplication_integers_correct_value:
                print("Case-09: 整数相乘(multiplication_integers): {} = {} is Pass!".format(multiplication_integers_demo, multiplication_integers_result))
            else:
                print("Case-09: 整数相乘(multiplication_integers): {} calculation is wrong!".format(multiplication_integers_demo))
        except Exception as msg:
            print(msg)

    def multiplication_decimals(self):
        """ Case-10: 小数相乘(multiplication_decimals): '0.5 * 0.4' """
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
            if multiplication_decimals_result == multiplication_decimals_correct_value:
                print("Case-10: 小数相乘(multiplication_decimals): {} = {} is Pass!".format(multiplication_decimals_demo, multiplication_decimals_result))
            else:
                print("Case-10: 小数相乘(multiplication_decimals): {} calculation is wrong!".format(multiplication_decimals_demo))
        except Exception as msg:
            print(msg)

    def multiplication_negative(self):
        """ Case-11: 负数相乘(multiplication_negative): '−5 * 4' """
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        multiplication_negative_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if multiplication_negative_result == multiplication_negative_correct_value:
                print("Case-11: 负数相乘(multiplication_negative): {} = {} is Pass!".format(multiplication_negative_demo, multiplication_negative_result))
            else:
                print("Case-11: 负数相乘(multiplication_negative): {} calculation is wrong!".format(multiplication_negative_demo))
        except Exception as msg:
            print(msg)

    def division_integers(self):
        """ Case-12: 整数相除(division_integers): '9 / 3' """
        self.driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        division_integers_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if division_integers_result == division_integers_correct_value:
                print("Case-12: 整数相除(division_integers): {} = {} is Pass!".format(division_integers_demo, division_integers_result))
            else:
                print("Case-12: 整数相除(division_integers): {} calculation is wrong!".format(division_integers_demo))
        except Exception as msg:
            print(msg)

    def division_decimals(self):
        """ Case-13: 小数相除(division_decimals): '0.9 / 0.3' """
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
            if division_decimals_result == division_decimals_correct_value:
                print("Case-13: 小数相除(division_decimals): {} = {} is Pass!".format(division_decimals_demo, division_decimals_result))
            else:
                print("Case-13: 小数相除(division_decimals): {} calculation is wrong!".format(division_decimals_demo))
        except Exception as msg:
            print(msg)

    def division_negative(self):
        """ Case-14: 负数相除(division_negative): '−9 / 3' """
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        division_negative_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if division_negative_result == division_negative_correct_value:
                print("Case-14: 负数相除(division_negative): {} = {} is Pass!".format(division_negative_demo, division_negative_result))
            else:
                print("Case-14: 负数相除(division_negative): {} calculation is wrong!".format(division_negative_demo))
        except Exception as msg:
            print(msg)

    def zero_multiplication(self):
        """ Case-15: 0的相乘(zero_multiplication): '0 * 8' """
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        zero_multiplication_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if zero_multiplication_result == zero_multiplication_correct_value:
                print("Case-15: 0的相乘(zero_multiplication): {} = {} is Pass!".format(zero_multiplication_demo, zero_multiplication_result))
            else:
                print("Case-15: 0的相乘(zero_multiplication): {} calculation is wrong!".format(zero_multiplication_demo))
        except Exception as msg:
            print(msg)

    def zero_division_numerator(self):
        """ Case-16: 0为分子除法(zero_division_numerator): '0 / (−8)' """
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.swipe(1060, 1300, 300, 1300, 1000)      # 左滑
        self.driver.find_element_by_id('com.android.calculator2:id/lparen').click()
        self.driver.swipe(300, 1300, 1060, 1300, 1000)      # 右滑
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
        self.driver.swipe(1060, 1300, 300, 1300, 1000)      # 左滑
        self.driver.find_element_by_id('com.android.calculator2:id/rparen').click()
        self.driver.swipe(300, 1300, 1060, 1300, 1000)      # 右滑
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        zero_division_numerator_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        self.driver.find_element_by_id('com.android.calculator2:id/clr').click()
        try:
            if zero_division_numerator_result == zero_division_numerator_correct_value:
                print("Case-16: 0为分子除法(zero_division_numerator): {} = {} is Pass!".format(zero_division_numerator_demo, zero_division_numerator_result))
            else:
                print("Case-16: 0为分子除法(zero_division_numerator): {} calculation is wrong!".format(zero_division_numerator_demo))
        except Exception as msg:
            print(msg)

    def zero_division_denominator(self):
        """ Case-17: 0为分母除法(zero_division_denominator): '0.8 / 0' """
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        zero_division_denominator_result = self.driver.find_element_by_id('com.android.calculator2:id/result').text
        time.sleep(1)
        for i in range(5):
            self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        try:
            if zero_division_denominator_result == zero_division_denominator_correct_value:
                print("Case-17: 0为分母除法(zero_division_denominator): {} = {} is Pass!".format(zero_division_denominator_demo, zero_division_denominator_result))
            else:
                print("Case-17: 0为分母除法(zero_division_denominator): {} calculation is wrong!".format(zero_division_denominator_demo))
        except Exception as msg:
            print(msg)

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    calculator = CalculatorSmoke()

    # Case-01: 输入0~9(number_button 0~9)
    number_button_demo = "0123456789"
    number_button_correct_value = "0123456789"
    number_button = calculator.number_button()
    # Case-02: 删除0~9(delete_button 0~9)
    delete_button_demo = "删除至'空'"
    delete_button_correct_value = ""
    delete_button = calculator.delete_button()

    # Case-03: 整数相加(addition_integers)
    addition_integers_demo = "1 + 7"
    addition_integers_correct_value = "8"
    addition_integers = calculator.addition_integers()
    # Case-04: 小数相加(addition_decimals)
    addition_decimals_demo = "0.1 + 0.7"
    addition_decimals_correct_value = "0.8"
    addition_decimals = calculator.addition_decimals()
    # Case-05: 负数相加(addition_negative)
    addition_negative_demo = "−1 + (−7)"
    addition_negative_correct_value = "−8"
    addition_negative = calculator.addition_negative()

    # Case-06: 整数相减(subtraction_integers)
    subtraction_integers_demo = "6 − 2"
    subtraction_integers_correct_value = "4"
    subtraction_integers = calculator.subtraction_integers()
    # Case-07: 小数相减(subtraction_decimals)
    subtraction_decimals_demo = "0.6 − 0.2"
    subtraction_decimals_correct_value = "0.4"
    subtraction_decimals = calculator.subtraction_decimals()
    # Case-08: 负数相减(subtraction_negative)
    subtraction_negative_demo = "−6 − (−2)"
    subtraction_negative_correct_value = "−4"
    subtraction_negative = calculator.subtraction_negative()

    # Case-09: 整数相乘(multiplication_integers)
    multiplication_integers_demo = "5 * 4"
    multiplication_integers_correct_value = "20"
    multiplication_integers = calculator.multiplication_integers()
    # Case-10: 小数相乘(multiplication_decimals)
    multiplication_decimals_demo = "0.5 * 0.4"
    multiplication_decimals_correct_value = "0.2"
    multiplication_decimals = calculator.multiplication_decimals()
    # Case-11: 负数相乘(multiplication_negative)
    multiplication_negative_demo = "−5 * 4"
    multiplication_negative_correct_value = "−20"
    multiplication_negative = calculator.multiplication_negative()

    # Case-12: 整数相除(division_integers)
    division_integers_demo = "9 / 3"
    division_integers_correct_value = "3"
    division_integers = calculator.division_integers()
    # Case-13: 小数相除(division_decimals)
    division_decimals_demo = "0.9 / 0.3"
    division_decimals_correct_value = "3"
    division_decimals = calculator.division_decimals()
    # Case-14: 负数相除(division_negative)
    division_negative_demo = "−9 / 3"
    division_negative_correct_value = "−3"
    division_negative = calculator.division_negative()

    # Case-15: 0的相乘(zero_multiplication)
    zero_multiplication_demo = "0 * 8"
    zero_multiplication_correct_value = "0"
    zero_multiplication = calculator.zero_multiplication()
    # Case-16: 0为分子除法(zero_division_numerator)
    zero_division_numerator_demo = "0 / (−8)"
    zero_division_numerator_correct_value = "0"
    zero_division_numerator = calculator.zero_division_numerator()
    # Case-17: 0为分母除法(zero_division_denominator)
    zero_division_denominator_demo = "0.8 / 0"
    zero_division_denominator_correct_value = "不能除以 0"
    zero_division_denominator = calculator.zero_division_denominator()

    calculator.quit()

   
