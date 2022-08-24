

# ex. 1
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # endcodes data to UTF-8
mysock.send(cmd)

# ex. 2
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode()) # decodes fata from UTF-8 to UNICODE   
mysock.close()