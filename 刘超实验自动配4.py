import string
from time import sleep

import pyautogui
import keyboard

#  若缺少python库，请自行 pip安装

name = "zgxFirewall"


def FW():
    names = name

    str1 = """system-view
sys """+names+""" 
int g 0/0/1
ip address 10.1.0.1 16
quit
int g 0/0/2
ip address 10.2.0.1 16
quit
int g 0/0/3
ip address 10.3.0.1 16
quit
display ip interface brief
firewall zone untrust 
add interface g 0/0/1
quit
firewall zone trust
add interface g 0/0/3
quit
firewall zone dmz
add interface g 0/0/2
display zone
quit
policy interzone trust untrust outbound
policy 100
policy source 10.3.0.0 0.0.255.255
policy destination 10.1.0.0 0.0.255.255
action permit
quit
quit
policy interzone trust dmz outbound
policy 101
policy source 10.3.0.0 0.0.255.255
policy destination 10.2.0.0 0.0.255.255
action permit
quit
quit
policy interzone untrust dmz inbound
policy 102
policy source 10.1.0.0 0.0.255.255
policy destination 10.2.0.0 0.0.255.255
action permit

"""
    pyautogui.typewrite(str1,0.1)    # 0.1是输入间隔 如果出现字符缺失，将它调大即可



def main():
    global name_

#     print("""*-------------------------------------*
# |       ZGX Public License            |
# | This software is made by Zegic and  |
# | other developer.The license         |
# | is same as GNU or GPL license.      |
# |      All rights reserved(c)         |
# *-------------------------------------*""")
   # print("使用此脚本前，先去name里把zgx改成你的名字。")
    print("你需要自己完成ip配置")
    print("""注意，你必须这样连接电缆：
              GE0/0/2
                 |
    ---GE0/0/3---FW---GE0/0/1----
    """)
    userinput = input("""记得把name=zgx改成自己的名字（在最上面）
    输入任意字符开始配置
    """)
    print("你有五秒钟时间将鼠标移到输入区，鼠标不要移动：")
    sleep(4)
    FW()



while True:
    main()
# if "__name__" == "__main__":
#     main()
