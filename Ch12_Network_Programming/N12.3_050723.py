print('N12.3_050723.py')

# There's alot of information to store xd
# I also will be working tmr as my first day :D
# woohoo
# Im going to take a break for now
# I went to take a break which I played 1 Valorant Comp lol
# And updated my Computer to Windows 11.
# I like the phone link feature.

# --- --- --- Using HTTP in Python --- --- ---

# -- -- -- Writing a Web Browser -- -- --
# -- -- -- HTTP Request in Python -- -- --

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
