# Author: AdrianZhang
# Script function: 自动登录微博并发布“爬取自网络的上海日出日落”以及从“接口获取的上海天气信息”后退出，
#                  然后将微博首页发布后的结果截图发送至指定邮箱。
# Coding Time: 2017/10/15

import time
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart

def current_time():
    """生成时间戳"""
    get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return get_time

def get_html_text(crawler_url):
    """爬取页面"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3)'
                                 ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        html_content = requests.get(crawler_url, headers=headers, timeout=30)
        html_content.raise_for_status()
        html_content.encoding = html_content.apparent_encoding
        return html_content.text
    except Exception as msg:
        print(msg)

def sunrise_sunset(html):
    """对所爬取页面进行数据提取（日出日落时间）"""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all('div', 'op_exactqa_s_area c-span24 c-span-last'):
        text_data = tag.get_text()    # 从中获取所有文字内容
        list_data = text_data.split()
        content = "【{}】{}".format(list_data[0].replace(":", ""), list_data[1])
        return content

def weather_data(city_code):
    """根据接口地址，获取天气数据，并对天气数据进行易用化处理。"""
    url = "http://www.weather.com.cn/data/cityinfo/{}.html".format(city_code)
    get_data = requests.get(url).text
    transcode = get_data.encode('ISO-8859-1').decode('utf-8')
    json_datas = json.loads(transcode)
    city = json_datas["weatherinfo"]["city"]
    city_id = json_datas["weatherinfo"]["cityid"]
    temperature_low = json_datas["weatherinfo"]["temp1"]
    temperature_high = json_datas["weatherinfo"]["temp2"]
    weather = json_datas["weatherinfo"]["weather"]
    image_1 = json_datas["weatherinfo"]["img1"]
    image_2 = json_datas["weatherinfo"]["img2"]
    publish_time = json_datas["weatherinfo"]["ptime"]
    content = "【{}今日天气：】{}, 最高气温：{}, 最低气温：{}".format(city, weather, temperature_high, temperature_low)
    return content


class Selenium(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_chrome(self):
        """打开浏览器并全屏窗口"""
        self.driver.maximize_window()

    def weibo_login(self, account, password, weibo_url, publish_content):
        """登录微博"""
        self.driver.get(weibo_url)
        time.sleep(3)
        self.driver.find_element_by_id("loginname").clear()
        self.driver.find_element_by_id("loginname").send_keys(account)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='pl_login_form']/div/div[3]/div[2]/div/input").clear()
        self.driver.find_element_by_xpath("//*[@id='pl_login_form']/div/div[3]/div[2]/div/input").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='pl_login_form']/div/div[3]/div[6]/a").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='v6_pl_content_publishertop']/div/div[2]/textarea").click()
        self.driver.find_element_by_xpath("//*[@id='v6_pl_content_publishertop']/div/div[2]/textarea").send_keys(publish_content)
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='v6_pl_content_publishertop']/div/div[3]/div[1]/a").click()
        time.sleep(8)

    def screenshot(self, save_img_path):
        """截屏"""
        self.driver.get_screenshot_as_file(save_img_path)
        time.sleep(1)

    def weibo_logout(self):
        """退出微博"""
        above_account_setting = self.driver.find_element_by_xpath("//*[@id='plc_top']/div/div/div[3]/div[2]/div[2]/a")
        ActionChains(self.driver).move_to_element(above_account_setting).perform()
        time.sleep(1)
        above_quit = self.driver.find_element_by_xpath("//*[@id='plc_top']/div/div/div[3]/div[2]/div[2]/div/ul/li[10]/a")
        ActionChains(self.driver).move_to_element(above_quit).perform()
        ActionChains(self.driver).click().perform()
        time.sleep(3)

    def quit_chrome(self):
        """关闭浏览器"""
        self.driver.quit()


class Email(object):
    def __init__(self):
        self.smtp_server = 'smtp.qq.com'

    def format_address(self, strings):
        """邮件地址格式整理"""
        name, address = parseaddr(strings)
        return formataddr((Header(name, 'utf-8').encode(), address))

    def handle_text(self):
        """文字处理"""
        msg_text = MIMEText(report_result, 'plain', 'utf-8')
        email_text = msg_root.attach(msg_text)
        return email_text

    def handle_image(self, save_img_path):
        """图片处理"""
        fp = open(save_img_path, 'rb')
        msg_image = MIMEImage(fp.read())
        fp.close()
        msg_image.add_header('Content_ID', '<image>')
        email_image = msg_root.attach(msg_image)
        return email_image

    def send_email(self):
        """发送邮件"""
        server = smtplib.SMTP_SSL(self.smtp_server, 465, timeout=10)
        server.set_debuglevel(0)
        server.login(sender, sender_password)
        server.sendmail(sender, receiver, msg_root.as_string())
        server.quit()


if __name__ == '__main__':
    crawler_url = "http://t.cn/RO1dLxn"     # get_html_text()函数用到
    html = get_html_text(crawler_url)       # sunrise_sunset()函数用到
    sun_info = sunrise_sunset(html)         # sun_info变量中存储“日出、日落”数据
    # ----------------------
    city_code = "101020100"                 # weather_data()函数用到，"101020100"为上海城市编码
    weather_info = weather_data(city_code)  # weather_info变量中存储“天气”数据
    # ---WeiBo--------------
    account = "********@163.com"            # Selenium类用到以下数据
    password = "********"
    weibo_url = "https://www.weibo.com/login.php"
    time_tail = current_time()              # 从current_time()函数中获取当前时间戳
    information = "The Message Is Come From Selenium Script And The Publish Time Is: "
    publish_content = "{}\n{}\n{}{}".format(sun_info, weather_info, information, time_tail)
    save_img_path = "D:\\WeiBoImage.png"    # 截图保存地址
    # ---Selenium()---------
    do_test = Selenium()                    # 执行Selenium()类
    do_test.open_chrome()
    do_test.weibo_login(account, password, weibo_url, publish_content)
    do_test.screenshot(save_img_path)
    do_test.weibo_logout()
    do_test.quit_chrome()
    # ---Email()------------
    report_result = "Result: --> Pass" + "\n\n" + publish_content
    sender = '********@qq.com'
    sender_password = '********'            # 注意！此处的密码为邮箱的“授权码”，而非登录密码！
    receiver = '********@163.com'
    subject = '微博自动发布每日结果汇报'
    execute = Email()                       # 执行Email()类
    msg_root = MIMEMultipart('related')
    msg_root['Subject'] = Header(subject, 'utf-8').encode()
    msg_root['From'] = execute.format_address('Selenium Scripts<%s>' % sender)
    msg_root['To'] = execute.format_address('龙哥<%s>' % receiver)
    execute.handle_text()
    execute.handle_image(save_img_path)
    execute.send_email()
