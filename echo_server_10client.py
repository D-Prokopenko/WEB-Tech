import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 2222))
serv.listen(10)  # количество подключений (клиентов)

while True:
    conn, adrr = serv.accept()
    while True:
        data = conn.recv(1024)
        if not data or data == 'close':
            break
        conn.send(data)
    conn.close()
