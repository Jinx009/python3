import socket


def client_connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.connect(('115.159.124.222', 5983))
    import time

    time.sleep(2)
    # s.send(str.encode('test'))
    s.send(str.encode('11223344556677880x4800300101'))
    print(str.encode('11223344556677880x4800300101'))
    print('1', s.recv(1024))

    s.close()


if __name__ == '__main__':
    client_connect()

