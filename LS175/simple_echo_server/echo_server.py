import socket
from random import randint

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_number = 3003
server_socket.bind(('localhost', port_number))
server_socket.listen()

print(f"Server is running on localhost:{port_number}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    request = client_socket.recv(1024).decode()
    if (not request) or ('favicon.ico' in request):
        client_socket.close()
        continue

    request_line = request.splitlines()[0]
    method, info, protocol = request_line.split()
    try:
        path, parameters = info.split("?")
        param_1, param_2 = parameters.split("&")
        param_1_key, param_1_val = param_1.split("=")
        param_2_key, param_2_val = param_2.split("=")
    except:
        path = "/"
        param_1_val = 1
        param_2_val = 6

    roll_count = int(param_1_val)
    dice_size = int(param_2_val)

    msg_array = []

    msg_array.append(f"Request Line: {request_line}")
    msg_array.append(f"HTTP Method: {method}")
    msg_array.append(f"Path: {path}")
    msg_array.append(f"Parameters: rolls:{roll_count}, sides:{dice_size}")

    for val in range(roll_count):
        msg_array.append(f"Roll:{randint(1, dice_size)}")

    full_response = f"<p>{'\n'.join(msg_array)}</p>"

    response = ("HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(full_response)}\r\n"
                "\r\n"
                f"{full_response}\n")

    client_socket.sendall(response.encode())
    client_socket.close()