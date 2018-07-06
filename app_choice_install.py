# Author: AdrianZhang
# Coding Time: 2018/07/03
# Script Function: A script for auto install the version of app which you want to install .


import os


def get_device_name():
    try:
        adb_log = os.popen("adb devices").readlines()
        for line in adb_log:
            if "\t" in line:
                device_name = line.split("\t")[0]
                return device_name
            else:
                return "未发现设备..."
    except Exception as msg:
        print(msg)


def install_1_0_version():
    apk_name = "planetAlliance_guanfang_1.0_1_20180510.apk"
    apk_path = "C:\\Users\\zhanglong\\Desktop\\测试资料\\APP版本\\" + apk_name
    install_1_0_log = os.popen('adb install {}'.format(apk_path)).read()
    return install_1_0_log


def install_1_1_version():
    apk_name = "planetAlliance_guanfang_1.1_2_20180608_release.apk"
    apk_path = "C:\\Users\\zhanglong\\Desktop\\测试资料\\APP版本\\" + apk_name
    install_1_1_log = os.popen('adb install {}'.format(apk_path)).read()
    return install_1_1_log


def install_1_1_1_version():
    apk_name = "planetAlliance_guanfang_1.1.1_3_20180612.apk"
    apk_path = "C:\\Users\\zhanglong\\Desktop\\测试资料\\APP版本\\" + apk_name
    install_1_1_1_log = os.popen('adb install {}'.format(apk_path)).read()
    return install_1_1_1_log


def install_1_4_version():
    apk_name = "planetAlliance_guanfang_1.4_2018061501.apk"
    apk_path = "C:\\Users\\zhanglong\\Desktop\\测试资料\\APP版本\\" + apk_name
    install_1_4_log = os.popen('adb install {}'.format(apk_path)).read()
    return install_1_4_log


def install_1_4_1_version():
    apk_name = "planetAlliance_guanfang_1.4.1_5_20180621.apk"
    apk_path = "C:\\Users\\zhanglong\\Desktop\\测试资料\\APP版本\\" + apk_name
    install_1_4_1_log = os.popen('adb install {}'.format(apk_path)).read()
    return install_1_4_1_log


if __name__ == '__main__':
    # get your phone device name.
    connect_device_name = get_device_name()
    print(connect_device_name)

    # test your phone whether have the package of 2345.
    test = ''  # app_list中是否有com.2345

    # install 1.0 version for Android.
    install_1_0_result = install_1_0_version()
    print(install_1_0_result)
    # 还需要返回dumpsys里的packagename包版本

    # install 1.1 version for Android.
    install_1_1_result = install_1_1_version()
    print(install_1_1_result)

    # install 1.1.1 version for Android.
    install_1_1_1_result = install_1_1_1_version()
    print(install_1_1_1_result)

    # install 1.4 version for Android.
    install_1_4_result = install_1_4_version()
    print(install_1_4_result)

    # install 1.4.1 version for Android.
    install_1_4_1_result = install_1_4_1_version()
    print(install_1_4_1_result)

