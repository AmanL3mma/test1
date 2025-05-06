import socket

ip = socket.gethostbyname("hackthissite.org")

for port in range(1024):
    try:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.settimeout(0.3)
        if serv.connect_ex((ip, port)) == 0:
            print('[OPEN] Port open :', port)
    finally:
        serv.close()