"""
chat room
env: python3.6
socket udp & fork
"""
from socket import *
import os,sys

# 服务端地址
ADDR = ('0.0.0.0',8888)
# 存储用户的结构 {name:address}
user = {}

# 处理登录
def do_login(s,name,addr):
    if name in user:
        s.sendto("该用户存在".encode(),addr)
        return

    # 加入用户
    msg = "欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr
    s.sendto(b'OK',addr)

# 接受请求，分发给不同方法处理
def do_request(s):
    while True:
        # 循环接收来自客户端请求
        data,addr = s.recvfrom(1024)
        tmp = data.decode().split(' ')
        # 根据不同的请求类型分发函数处理
        # L 进入
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)

# 搭建网络
def main():
    # udp服务端
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    do_request(s) # 处理客户端请求

main()
