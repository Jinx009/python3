import socket


def client_connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.connect(('127.0.0.1', 8888))
    import time

    time.sleep(2)
    # s.send(str.encode('test'))
    s.send(str.encode('123'))
    print(str.encode('123'))
    print('1', s.recv(1024))

    s.close()


if __name__ == '__main__':
    client_connect()

