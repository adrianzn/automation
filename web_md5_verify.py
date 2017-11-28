# Author: AdrianZhang
# Coding Time: 2017/11/28
# Script Function: 校验一个网页是否更新。

import requests
import hashlib
import os

url = "http://news.baidu.com"
html = requests.get(url).text.encode('utf-8-sig')
new_html_md5 = hashlib.md5(html).hexdigest()

if os.path.exists('old_html_md5.txt'):
    with open('old_html_md5.txt', 'r') as f:
        old_md5 = f.read()

    if new_html_md5 != old_md5:
        with open('old_html_md5.txt', 'w') as f:
            old_md5 = f.write(new_html_md5)
        print('网页数据已更新！')

    else:
        print('网页数据未更新！')

else:
    with open('old_html_md5.txt', 'w') as f:
        f.write(new_html_md5)
    print('哈哈，这是第一次生成md5文件啊~')

