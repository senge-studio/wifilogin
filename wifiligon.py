import pywifi
import requests
import json
from pywifi import const


# 通过SSID连接校园网
def wifi_connect(operator):
    wifi = pywifi.PyWiFi()
    # 选择内置Wi-Fi无线网卡
    iface = wifi.interfaces()[0]
    # 断开Wi-Fi连接
    iface.disconnect()
    try:
        assert iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
    except AssertionError:
        print(f'Disconnecting Wi-Fi failed!')
        exit(1)
    else:
        print('Wi-Fi disconnected.')
    # 通过SSID连接Wi-Fi
    profile = pywifi.Profile()
    profile.ssid = f'Hncj-{operator}'
    # 无密码连接
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_NONE)
    profile.cipher = const.CIPHER_TYPE_CCMP
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    try:
        assert iface.status() == const.IFACE_CONNECTED
    except AssertionError:
        print(f'Connecting Wi-Fi Hncj-{operator} Failed')
        exit(1)
    else:
        print(f'Wi-Fi Hncj-{operator} connected.')


# 检测网络连接
def network_check():
    try:
        res = requests.get(url='https://wwww.baidu.com', timeout=2).status_code
    except Exception:
        pass
    else:
        if res == 200:
            return True
        else:
            return False


# 退出校园网账号
def logout(username, password):
    # 浏览器代理
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/84.0.4147.105 Safari/537.36 '
    }
    # 读取用户信息
    data = dict(action="logout", username=username, password=password, ac_id="1", user_ip="", nas_ip="",
                user_mac="",
                save_me="1", ajax="1")
    url = 'http://10.248.254.250:801/srun_portal_pc.php?ac_id=1&'
    # 执行登录操作
    try:
        res = requests.post(url, data, headers=headers).status_code
    except Exception as e:
        print(f' Wi-Fi login failed.\nError code:{e}')
    else:
        if res == 200:
            print(f'Wi-Fi logout successfully.')
        else:
            print(f'Wi-Fi logout failed')


# 登录操作
def login(username, password):
    # 浏览器代理
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/84.0.4147.105 Safari/537.36 '
    }
    # 读取用户信息
    data = dict(action="login", username=username, password=password, ac_id="1", user_ip="", nas_ip="",
                user_mac="",
                save_me="1", ajax="1")
    url = 'http://10.248.254.250:801/srun_portal_pc.php?ac_id=1&'
    # 登录操作
    try:
        res = requests.post(url, data, headers=headers).status_code
    except Exception as e:
        print(f' Wi-Fi login failed.\nError code:{e}')
    else:
        if res == 200:
            if network_check():
                print('Wi-Fi login successfully.')
                return True
            else:
                print(f'Wi-Fi login failed. Please check your username or password.')
        else:
            print(f'Wi-Fi login failed.\n HTTP:{res}')
    exit(1)


if __name__ == '__main__':
    # 读取json文件
    with open('profile.json', 'r') as file:
        data = json.loads(file.read())
    # 读取运营商、用户名和密码
    operator = data['Operator']
    username = data['UserName']
    password = data['Password']
    # 检测网络连接
    if network_check():
        print('Wi-Fi has already connected, you needn\'t to login.')
    else:
        # 连接Wi-Fi
        wifi_connect(operator)
        # 注销账号
        logout(username, password)
        # 登录账号
        login(username, password)
