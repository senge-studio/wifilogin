# 校园网Wi-Fi连接
## 开源协议
本程序采用 [MIT开源协议](https://opensource.org/licenses/MIT/) ，可以按需自行修改或分发。
## 安装方法
### Windows/Linux：
```bash
$ pip install pywifi
$ pip install requests 
```
> 注意：
> - 命令行前的$代表以非管理员模式运行
> - 命令行前的#代表以管理员模式运行（前面加上`sudo`）
### macOS:
安装pywifi
```bash
$ git clone -b macos_dev https://github.com/awkman/pywifi.git ~/.pywifi
$ cd ~/.pywifi
$ pip3 install .
```
安装依赖
```bash
$ pip3 install iface
$ pip3 install pyobjc
```
> 注意：macOS请勿直接使用pip安装pywifi，不然会报错
## 使用方法：
从GitHub克隆脚本
```bash
$ git clone https://github.com/senge-x/wifilogin.git
```
编辑`profile.json`(以下内容为示例，请改成自己的用户名或密码)
```json
{
  "UserName": "201900000",
  "Password": "123456",
  "Operator": "Mobile"
}
```
> 注意
> - 以上配置文件无法登录，请改成自己的用户名和密码
> - `UserName`代表用户名
> - `Password`代表密码，初始密码是身份证号后六位
> - `Operator`代表运营商，移动用户填写`Mobile`，联通用户填写`Unicom`
### Windows
将wifilogin.bat快捷方式复制到桌面，然后需要运行时直接双击运行
### macOS/Linux
```bash
$ cd wifilogin
# cp wifilogin.py /usr/bin/
# cp profile.json /usr/bin/
$ chmod +x wifilogin.py
```
运行时只需要终端运行`wifilogin.py`即可
