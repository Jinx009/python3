import socket

addr=('115.159.124.222', 5983)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input()
    s.sendto(msg.encode('utf-8'), addr)
    if msg == 'bye':
        break
s.close()