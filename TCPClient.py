import socket
import threading
import time


TCP_TARGET_IP = "192.168.1.100"
TCP_TARGET_PORT = 8000

client = socket.socket()
addr = (TCP_TARGET_IP, TCP_TARGET_PORT)
def recv():
    while True:
        try:
            data = client.recv(1024)
            if data:
                print('TCP Client Received Data from {0}: {1}'.format(TCP_TARGET_IP, data) )
        except Exception as e:
            client.close()
            print("Connect Fail!")
            break


try:
    client.connect(addr)
    t0 = threading.Thread(target=recv)
    t0.start()
    while True:
        send_data = input(">>>")
        client.send(send_data.encode('utf-8'))
        # time.sleep(1)

except Exception as e:
    print("Connect to server Fail!")

