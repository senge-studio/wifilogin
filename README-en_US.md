# Wi-Fi login
## How to use
This program can only work on Henan University of Urban Constructions, if you want to use it on other university, please edit the source code manually.
## Open source license
This program is using [MIT license](https://opensource.org/licenses/MIT/) , you can edit it and distribute.
## How to install
### Windows/Linux:
```bash
$ pip install pywifi
$ pip install requests 
```
> Warning:
> - $ means that you should run this command directory
> - # means that you should run this command by super user
### macOS:
Install pywifi
```bash
$ git clone -b macos_dev https://github.com/awkman/pywifi.git ~/.pywifi
$ cd ~/.pywifi
$ pip3 install .
```
Install dependence manually
```bash
$ pip3 install iface
$ pip3 install pyobjc
```
> Warning: Don't install `pywifi` directory by `pip` on macOS, or the program can not work.
## How to use:
Clone the source code from GitHub
```bash
$ git clone https://github.com/senge-x/wifilogin.git
```
edit `profile.json`
```json
{
  "UserName": "201900000",
  "Password": "123456",
  "Operator": "Mobile"
}
```
> Warning:
> - Please edit the json file manually
> - `UserName` your user name
> - `Password` your password
> - `Operator` the operator, China Mobile operator : `Mobile`. China Unicom operator: `Unicom`.
### Windows
Link `wifilogin.bat` to desktop, then double click to run this command.
### macOS/Linux
```bash
$ cd wifilogin
# cp wifilogin.py /usr/bin/
# cp profile.json /usr/bin/
$ chmod +x wifilogin.py
```
run `wifilogin.py` in terminal to run this command
