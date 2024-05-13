import string
from time import sleep

import pyautogui
import keyboard

#  若缺少python库，请pip安装

name = "zgx"

def R1():
    print("1")
    str0 = "sys\nsys "+name+"R1"
    str1 = str0+"""\n
int g0/0/0
ip add 192.168.1.254 24
int g0/0/1
ip add 10.1.1.1 24
dis ip int b
q
ip route-static 0.0.0.0 0  10.1.1.2
ike proposal 10
encryption-algorithm 3des-cbc
authentication-algorithm md5
sa duration 10000
dh group5
q
ike peer zb v1
pre-shared-key simple 123
remote-address 20.1.1.1
q
ipsec proposal 10
esp encryption-algorithm aes-128
q
acl number 3000
rule 5  permit ip sou 192.168.1.0 0.0.0.255 dest 192.168.2.0 0.0.0.255
q
ipsec policy my-policy 20 isakmp
security acl 3000
ike-peer zb
proposal 10
q
int g0/0/1
ipsec policy my-policy
q
dis ike sa
dis ipsec sa    
    """
    sleep(3)
    pyautogui.typewrite(str1,0.2) # 键盘函数，一参字符串，二参输入间隔
    print("1 ok")

def R2():
    print("2")
    str0 = "sys\nsys " + name + "R2"
    str1 = str0 + """\n
int g0/0/0
ip add 10.1.1.2 24
int g0/0/1
ip add 20.1.1.2 24
dis ip int b    
    """
    sleep(3)
    pyautogui.typewrite(str1, 0.2)  # 键盘函数，一参字符串，二参输入间隔

def R3():
    print("3")
    str0 = "sys\nsys " + name + "R3"
    str1 = str0 + """\n
int g0/0/1
ip add 20.1.1.1 24
int g0/0/0
ip add 192.168.2.254 24
dis ip int b
q
ip route-static 0.0.0.0 0 20.1.1.2
ike proposal 10
encryption-algorithm 3des-cbc
authentication-algorithm md5
sa duration 10000
dh group5
q
ike peer fb v1
pre-shared-key simple 123
remote-address 10.1.1.1
q
ipsec proposal 10
esp encryption-algorithm aes-128
q
acl number 3000
rule 5 permit ip sou 192.168.2.0 0.0.0.255 dest 192.168.1.0 0.0.0.255
q
ipsec policy my-policy 20 isakmp
security acl 3000
ike-peer fb
proposal 10
q
int g0/0/1
ipsec policy my-policy
q
dis ike sa
dis ipsec sa
    """
    sleep(3)
    pyautogui.typewrite(str1, 0.2)  # 键盘函数，一参字符串，二参输入间隔

def N():
    strsb = """
    http://tools.yijinglab.com/tools/eNSP.zip
    """
    sleep(3)
    pyautogui.typewrite(strsb, 0.2)



def main():
    global name_
    print()
#     print("""*-------------------------------------*
# |       ZGX Public License            |
# | This software is made by Zegic and  |
# | other developer.The license         |
# | is same as GNU or GPL license.      |
# |      All rights reserved(c)         |
# *-------------------------------------*""")
    print("""
叠甲时间:
*-------------------------------------------------*
|                ZGX开源声明
|该声明和GNU/GPL声明相同，包括但不限于：
|1，该软件免费发布，允许任何人修改源代码并二次分发.
|2，出现任何问题，软件提供方不负任何责任.
|3，任何基于该软件的分发都需要包含本License，并标明贡献人员
*-------------------------------------------------*

开发者：zegic，xsheep
鸣谢：v2 debug xsheep，测试者 h
此软件专为刘超的实验课打造的辅助软件，用于快速搭建--的、--的蚁-平台环境
本软件基于GNU协议打造，可以任意修改代码，可以任意分发，但必须保留GNU Punlic License声明。
    """        )
    print()
    print()
    print()
    print("""
    此软件是专为刘超的实验课打造的辅助软件，用于快速搭建愚蠢的、自灭的蚁精平台环境
    警告：你的路由器必须像下面一样连接：(重点看端口)
    g0/0/1->                       <-g0/0/1
    [R1]------g0/0/0[R2]g0/0/1---------[R3]
     |g0/0/0                       g0/0/0|
     |  |                              | | 
     |  \/                            \/ |
    PC1                                PC2
    (顺序：PC1->R1,PC2->R3,R1->R2,R3->R2)
    使用方法：
    1 首先在python代码中修改你的名字，不然你的路由器就要叫zgx路由器了。
    2 打开你的路由器终端，然后在脚本里输入123代表你想配置R1 R2 R3
    3 三秒后脚本将开始输入。你把鼠标放在输入框里
    注意：你必须按照上图的端口配置你的路由器
    警告：软件模拟键盘输入，输入期间鼠标不要乱动，否则字符可能缺失
    提示：理论上来说，出现问题仅需重新运行脚本输入，无需删除路由器等
    """) # name变量在最上面

    userinput = input("按下数字并回车，将鼠标放在路由器终端上，3秒后软件自动粘贴并配置一个路由器。\n输入：Router1:[1],Router2:[2],Router3:[3]")
    if userinput == '1':
        R1()
    elif userinput == '2':
        R2()
    elif userinput == '3':
        R3()
    elif userinput == 'n':
        N()
    elif userinput == 'q':
        exit(0)
    else:
        print("让你输入1，2，3，你都不会？")
        sleep(5)


while True:
    main()
# if "__name__" == "__main__":
#     main()
