# Author: AdrianZhang
# Coding Time: 2018/01/12
# Script Function: generate new wifi mac address.

import os
import hashlib

def get_md5_value(ssid):
    encode_ssid = ssid.encode('utf-8')
    ssid_md5_value = hashlib.md5(encode_ssid).hexdigest()
    return ssid_md5_value

def generate_new_mac(ssid_md5_value, ssid_initial_mac):
    ltor_1, ltor_2, ltor_3, ltor_4, ltor_5, ltor_6 = 19, 19, 18, 16, 22, 1
    
    ltor_1_index = ltor_1 - 1
    ltor_2_index = ltor_2 - 1
    ltor_3_index = ltor_3 - 1
    ltor_4_index = ltor_4 - 1
    ltor_5_index = ltor_5 - 1
    ltor_6_index = ltor_6 - 1
    
    bssid_1 = ssid_md5_value[ltor_1_index] + ssid_md5_value[ltor_2_index]
    bssid_2 = ssid_md5_value[ltor_3_index] + ssid_md5_value[ltor_4_index]
    bssid_3 = ssid_md5_value[ltor_5_index] + ssid_md5_value[ltor_6_index]

    new_mac = '{}:{}:{}:{}:{}:{}'.format(ssid_initial_mac.split(':')[0],
                                         bssid_1, bssid_2, bssid_3,
                                         ssid_initial_mac.split(':')[4],
                                         ssid_initial_mac.split(':')[5])
    return new_mac

if __name__ == '__main__':
    ssid = '#!/usr/bin/env python'
    mac = 'c0:aa:7b:af:64:54'
    md5_value = get_md5_value(ssid)
    new_mac = generate_new_mac(md5_value, mac)
    print('SSID Name: {}\nMAC Address: {}\nGenerate MAC Address: {}'.format(ssid, mac, new_mac))


