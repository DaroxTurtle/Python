print('E12.1_050923.py')

# Exercise 12.1
# Change the socket program 'socket.py' to prompt the user for the URL so it can read any web page.
# You can use 'split('/')' to break the URL into its component parts so you can extract the host name for the
# socket 'connect' call. Add error checking using try and except to handl the condition where the user
# enters an improperly formatted or non-existent URL.

import socket

Uinput = input('Enter URL: ')
Uinput = Uinput.lower()

URL = Uinput.split('/')
URL = URL[2]
print(URL)


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((URL, 80))
cmd = b'GET ' + Uinput.encode() + b' HTTP/1.0\r\n\r\n'
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
