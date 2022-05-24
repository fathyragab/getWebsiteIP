import socket
web = input("Enter url site :")
ip = socket.gethostbyname(web)
print(ip)