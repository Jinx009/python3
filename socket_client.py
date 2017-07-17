import socket


def client_connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.connect(('localhost', 8888))
    import time

    time.sleep(2)
    s.send(str.encode('test'))
    print('1', s.recv(1024))

    s.close()


if __name__ == '__main__':
    client_connect()

