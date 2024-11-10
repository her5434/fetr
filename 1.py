import socket

def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # Слушаем все адреса на порту 12345
server_socket.listen(1)

print("подождите")
conn, addr = server_socket.accept()
print(f"Подключено: {addr}")

ip_address = get_ip()
conn.send(ip_address.encode())  # Отправляем IP-адрес клиенту
conn.close()
server_socket.close()