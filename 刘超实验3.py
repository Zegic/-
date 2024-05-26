import string
from time import sleep

import pyautogui
import keyboard

#  若缺少python库，请pip安装

name = "zgx"

def R1():
    str1 = """cd C:\\tools\\apache-tomcat-7.0.57\\bin
startup.bat"""
    sleep(3)
    pyautogui.typewrite(str1,0.2) # 键盘函数，一参字符串，二参输入间隔

def R2():
    sleep(3)
    str2="""cd C:\\tools\\apache-tomcat-7.0.57\\conf
keytool -genkey -alias xxx -keyalg RSA -keystore xxx.keystore -validity 365
123456
123456
www."""+name+""".com
a
a
a
a
cn
y

keytool -export -alias xxx -keystore xxx.keystore -file xxx.cer
123456

"""
    pyautogui.typewrite(str2,0.2) # 键盘函数，一参字符串，二参输入间隔

def Rs():
    str1 = """Connector port="8443" protocol="org.apache.coyote.http11.Http11Protocol" maxThreads="150" SSLEnabled="true" scheme="https" secure="true" clientAuth="false" sslProtocol="TLS" keystoreFile="conf/xxx.keystore"  keystorePass="123456" """
    sleep(3)
    pyautogui.typewrite(str1,0.2) # 键盘函数，一参字符串，二参输入间隔

def R3():
    str1 = """cd C:\\tools\\apache-tomcat-7.0.57\\conf
keytool -genkey -alias client -keyalg RSA -storetype PKCS12 -keystore client.key.p12 -validity 365
123456
123456
www."""+name+""".com
a
a
a
a
cn
y
"""
    str2 = """keytool -export -keystore client.key.p12 -storetype PKCS12 -alias client -file client.key.cer
123456
"""
    str3 = """keytool -import -file client.key.cer -keystore xxx.keystore -v
123456
y
"""
    str4= """keytool -list -keystore xxx.keystore
123456
"""
    st = str1+str2+str3+str4
    sleep(3)
    pyautogui.typewrite(st,0.2) # 键盘函数，一参字符串，二参输入间隔

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
    print("你需要自己完成hosts配置、xml配置")
    userinput = input("""输入想执行的操作：【1】启动服务器；【2】生成www.com密钥库；【3】一键生成客户端
    其他：a:host,s:server-xml,q:quit,
    """)
    # name_ = userinput
    if userinput == "1":
        R1()
   # if userinput == "":
    if userinput == "2":
        R2()
    if userinput == "s":
        Rs()
    if userinput == '3':
        R3()
    if userinput == "a":
        str1 = """C:\\windows\\system32\\drivers\\etc\\hosts"""
        sleep(3)
        pyautogui.typewrite(str1, 0.2)


while True:
    main()
# if "__name__" == "__main__":
#     main()
