# Author: AdrianZhang
# Coding Time: 2017/11/19
# Script Function: 一个获取网页表格并转化成本地.csv文件。

import requests
import csv

def get_html():
    html_content = requests.get('http://bills.mugglecode.com/sample.html').text
    return html_content

def get_data(html_content):
    split_data = html_content.split("\n")

    data_list = []
    for each in split_data:
        new_each = each.strip()
        if new_each.endswith("</td>"):
            clean_data = new_each.strip("</td>").split(">")[-1]
            data_list.append(clean_data)
    return data_list

def format_data(data_list):
    unit = []
    formatted_data = [
        ["ACCOUNT", "DUE DATE", "AMOUNT", "PERIOD"],
    ]

    for each in data_list:
        unit.append(each)
        if len(unit) == 4:
            formatted_data.append(unit)
            unit = []

    return formatted_data

def write_csv(formatted_data):
    file = open("result.csv", "w+")
    writer = csv.writer(file)
    for unit in formatted_data:
        writer.writerow(unit)
    file.close()

if __name__ == '__main__':
    html_content = get_html()
    data_list = get_data(html_content)
    format_list = format_data(data_list)
    write_csv(format_list)

