import socket

for port in range(1, 1000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex(("192.168.0.15", port))
if 0 == result:
        print("Port: {} Open".format(port))

else:
    print ( "All the ports are close" )
    sock.close()
