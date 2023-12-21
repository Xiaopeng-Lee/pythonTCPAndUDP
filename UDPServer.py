import socket

UDP_SERVER_PORT = 8000


# 服务器IP地址和端口号
server_address = ('', UDP_SERVER_PORT)

# 创建一个 socket 对象
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定服务端的IP地址和端口号
udp_socket.bind(server_address)

print('UDP Server Waiting for clients...')

# 循环监听客户端的请求
while True:
    # 接收客户端的请求数据和地址
    data, client_address = udp_socket.recvfrom(1024)
    print('UDP Server Received Data From {0}: {1}'.format(f'{client_address}', data))

    # 回复客户端
    udp_socket.sendto(b'RECV FROM YOU', client_address)