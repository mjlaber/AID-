"""
chat room 客户端
发送请求，展示结果
"""

from socket import *
import os,sys

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 进入聊天室
def login(s):
    while True:
        try:
            name = input("请输入昵称:")
            if not name:
                continue
        except KeyboardInterrupt:
            sys.exit("谢谢使用")
        msg = "L " + name
        s.sendto(msg.encode(),ADDR)
        #　接收反馈结果
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            return
        else:
            print(data.decode())

# 客户端启动函数
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    login(s) # 请求进入聊天室


main()

