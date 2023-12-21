# 这是服务器端
import socket
import threading

IP = "127.0.0.1"
PORT = 10001

# 创建Socket TCP对象
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind(('', PORT))   # 绑定本地端口
print('---------------------------服务器端--------------------------')

# 启动监听列队
Server.listen(8)


# 多线程任务
def send_msg(socket):          # 发送消息（任务线程）
    while True:
        msg = input(">>>")
        socket.send(msg.encode('utf-8'))

def recv_msg(socket):          # 接收消息（任务线程）
    while True:
        remsg = socket.recv(1024).decode('utf-8')
        print("客户端：" + f'{remsg}')
        if len(remsg) == 0:
            break


# 循环接纳客户端
while True:
    socket, addr_info = Server.accept()  # 返回值传参赋值
    threading.Thread(target=send_msg, args=(socket,)).start()
    threading.Thread(target=recv_msg, args=(socket,)).start()
    print(f'{addr_info}' + "客户端与与服务器连接成功...")
