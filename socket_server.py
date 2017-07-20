import socket


def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.bind(('127.0.0.01', 5983))
    s.listen(5)
    while True:
        connection, address = s.accept()
        print('connection:::', connection)
        print('address:::', address)

        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            print('buf::', buf)
            print('str:', bytes.decode(buf))
            if buf == '1':
                connection.send(str.encode('welcome to server!'))
            else:
                connection.send(str.encode('.'))
        except socket.timeout:
            print('time out')
        connection.close()


if __name__ == '__main__':
    print('begin...')
    listen()
    print('end...')


