# Author: AdrianZhang
# Coding Time: 2017/11/05
# Script Function: 一个根据网站开放API获取指定城市空气质量的脚本。
# 本程序API数据获取自: http://pm25.in
# 请勿滥用公共测试AppKey: 5j1znBVAsnSf5xQyNQyq

import json
import requests

def head_info():
    api = "http://www.pm25.in/api/querys/pm2_5.json?city={}&token=5j1znBVAsnSf5xQyNQyq&stations=no".format(city_name)
    api_data = requests.get(api).text
    api_json = json.loads(api_data)
    city = api_json[0]["area"]
    quality = api_json[0]["quality"]
    publish_time = api_json[0]["time_point"].replace("T", " ").replace("Z", "")
    aqi = api_json[0]["aqi"]
    main_info = "{:<18}\t{:<20}\n{:<18}\t{:<20}\n{:<18}\t{:<20}\n{:<18}\t{:<20}"\
        .format("City:", city, "Air Quality:", quality, "AQI:", aqi, "Publish Time:", publish_time)
    return main_info

def get_pm2_5():
    """ PM2.5: 细颗粒物 """
    pm2_5_api = "http://www.pm25.in/api/querys/pm2_5.json?city={}&token=5j1znBVAsnSf5xQyNQyq&stations=no".format(city_name)
    pm2_5_api_content = requests.get(pm2_5_api).text
    pm2_5_json = json.loads(pm2_5_api_content)
    pm2_5_pm2_5 = pm2_5_json[0]["pm2_5"]
    pm2_5_data = "{:<18}\t{:<25}".format("PM2.5/1h:", str(pm2_5_pm2_5) + " μg/m3")
    return pm2_5_data

def get_pm10():
    """ PM10: 可吸入颗粒物 """
    pm10_api = "http://www.pm25.in/api/querys/pm10.json?city={}&token=5j1znBVAsnSf5xQyNQyq&stations=no".format(city_name)
    pm10_api_content = requests.get(pm10_api).text
    pm10_json = json.loads(pm10_api_content)
    pm10_pm10 = pm10_json[0]["pm10"]
    pm10_data = "{:<18}\t{:<25}".format("PM10/1h:", str(pm10_pm10) + " μg/m3")
    return pm10_data

def get_co():
    """ CO: 一氧化碳 """
    co_api = "http://www.pm25.in/api/querys/co.json?city={}&token=5j1znBVAsnSf5xQyNQyq&stations=no".format(city_name)
    co_api_content = requests.get(co_api).text
    co_json = json.loads(co_api_content)
    co_co = co_json[0]["co"]
    co_data = "{:<18}\t{:<20}".format("CO/1h:", str(co_co) + " mg/m3")
    return co_data

def get_no2():
    """ NO2: 二氧化氮 """
    no2_api = "http://www.pm25.in/api/querys/no2.json?city={}&token=5j1znBVAsnSf5xQyNQyq&stations=no".format(city_name)
    no2_api_content = requests.get(no2_api).text
    no2_json = json.loads(no2_api_content)
    no2_no2 = no2_json[0]["no2"]
    no2_data = "{:<18}\t{:<20}".format("NO2/1h:", str(no2_no2) + " μg/m3")
    return no2_data

def get_o3():
    """ O3: 臭氧 """
    o3_api = "http://www.pm25.in/api/querys/o3.json?city={}&token=5j1znBVAsnSf5xQyNQyq&stations=no".format(city_name)
    o3_api_content = requests.get(o3_api).text
    o3_json = json.loads(o3_api_content)
    o3_o3 = o3_json[0]["o3"]
    o3_o3_8h = o3_json[0]["o3_8h"]
    o3_data = "{:<18}\t{:<20}\n{:<18}\t{:<20}".format("O3/1h:", str(o3_o3) + " μg/m3", "O3/8h", str(o3_o3_8h) + " μg/m3")
    return o3_data

def get_so2():
    """ SO2: 二氧化硫 """
    so2_api = "http://www.pm25.in/api/querys/so2.json?city={}&token=5j1znBVAsnSf5xQyNQyq&stations=no".format(city_name)
    so2_api_content = requests.get(so2_api).text
    so2_json = json.loads(so2_api_content)
    so2_so2 = so2_json[0]["so2"]
    so2_data = "{:<18}\t{:<20}".format("SO2/1h:", str(so2_so2) + " μg/m3")
    return so2_data

if __name__ == '__main__':
    city_name = "shanghai"
    head_info = head_info()
    pm2_5 = get_pm2_5()
    pm10 = get_pm10()
    co = get_co()
    no2 = get_no2()
    o3 = get_o3()
    so2 = get_so2()
    print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(head_info, pm2_5, pm10, co, no2, o3, so2))

