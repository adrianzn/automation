# Author: AdrianZhang
# Coding Time: 2018/07/10
# Script Function: A script for choice the apk file which you want to install.

import os
import time


def get_device_status():
    try:
        adb_log = os.popen("adb devices").readlines()
        print(adb_log)
        for line in adb_log:
            if "\t" in line:
                device_name = line.split("\t")[0]
                return device_name
            else:
                return "未发现设备..."
    except Exception as msg:
        print(msg)


def install_app(apk_path, test_package):
    apk_info = {}
    packages = []
    version_number = []
    try:
        package_list = os.popen('adb shell pm list packages -3').readlines()
        for each_package in package_list:
            packages.append(each_package.split(':')[-1].replace('\n', ''))
        if test_package in packages:
            print(">>> Begin to uninstall existing version...")
            uninstall_app(test_package)
            time.sleep(2)
        
        print(">>> Now, begin to install the version which you choice...\n")
        install_log = os.popen('adb install {}'.format(apk_path)).read()
        if "Success" in install_log:
            version_list = os.popen("adb shell dumpsys package {}".format(test_package)).readlines()
            for each_version in version_list:
                if "version" in each_version:
                    version_info = each_version.split(" ")
                    while "" in version_info:
                        version_info.remove("")
                    for element in version_info:
                        version_number.append(element.strip('\n'))
    except Exception as msg:
        print(msg)
                            
    apk_info['versionCode'] = version_number[0]
    apk_info['minSdk'] = version_number[1]
    apk_info['targetSdk'] = version_number[2]
    apk_info['versionName'] = version_number[3]
    return apk_info
    

def uninstall_app(test_package):
    uninstall_log = os.popen("adb uninstall {}".format(test_package)).read()
    uninstall_result = uninstall_log.replace("\n", "")
    if "Success" in uninstall_result:
        print(">>> Uninstall Success!")


if __name__ == '__main__':
    # get device name.
    connect_device_name = get_device_status()
    print("Device name: ", connect_device_name)

    test_package = 'com.magicbox2345'
    version_number_list = ['1.0', '1.1', '1.1.1', '1.4', '1.4.1']
    apk_folder = 'C:\\Users\\username\\Desktop\\test\\APPversion\\'
    apk_dict = {'1.0': 'planetAlliance_guanfang_1.0_1_20180510.apk',
                '1.1': 'planetAlliance_guanfang_1.1_2_20180608_release.apk',
                '1.1.1': 'planetAlliance_guanfang_1.1.1_3_20180612.apk',
                '1.4': 'planetAlliance_guanfang_1.4_2018061501.apk',
                '1.4.1': 'planetAlliance_guanfang_1.4.1_5_20180621.apk'}

    try:
        while True:
            choice_version = input(">>> Please choice a version number which you want to install: \n"
                                   ">>> 1.0 / 1.1 / 1.1.1 / 1.4 / 1.4.1\n>>> ")
            if choice_version in version_number_list:
                apk_path = apk_folder + apk_dict[choice_version]
                install_result = install_app(apk_path, test_package)
                print("===================================")
                print("{:<15}{}".format("PackageName: ", test_package))
                print("{:<15}{}".format("VersionCode: ", install_result['versionCode']))
                print("{:<15}{}".format("MinSdk: ", install_result['minSdk']))
                print("{:<15}{}".format("TargetSdk: ", install_result['targetSdk']))
                print("{:<15}{}".format("VersionName: ", install_result['versionName']))
                print("===================================")
                break
            else:
                print(">>> Sorry, please enter a valid version number!\n")
                continue
    except Exception as msg:
        print(msg)

