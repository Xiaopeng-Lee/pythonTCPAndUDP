import socket
import threading

UDP_TARGET_IP = "192.168.124.5"
UDP_TARGET_PORT = 9999

# 服务器IP地址和端口号
server_address = (UDP_TARGET_IP, UDP_TARGET_PORT)

# 创建一个 socket 对象
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def recv_msg(socket):          # 接收消息（任务线程）
    while True:
        # 接收数据和地址
        data, server_address = udp_socket.recvfrom(1024)
        print('UDP Client Received Data From {0}: {1}'.format(f'{server_address}', data))
        if len(data) == 0:
            break


threading.Thread(target=recv_msg, args=(socket,)).start()

while True:
    msg = input(">>>")
    udp_socket.sendto(msg.encode('utf-8'), server_address)

