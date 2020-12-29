import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("\nEl nombre de tu computadora es: " + hostname)
print("Tu dirección IP es: " + ip + "\n")