# Author: AdrianZhang
# Coding Time: 2017/11/28
# Script Function: Check the web page is updated or not updated.

import requests
import hashlib
import os

url = "http://your.web.address"
html = requests.get(url).text.encode('utf-8-sig')
new_html_md5 = hashlib.md5(html).hexdigest()

if os.path.exists('old_html_md5.txt'):
    with open('old_html_md5.txt', 'r') as f:
        old_md5 = f.read()

    if new_html_md5 != old_md5:
        with open('old_html_md5.txt', 'w') as f:
            old_md5 = f.write(new_html_md5)
        print('HaHa, The Web is update!')

    else:
        print('Sorry, The Web is not update!')

else:
    with open('old_html_md5.txt', 'w') as f:
        f.write(new_html_md5)
    print('Oh, this is the first time to make md5 file.')

