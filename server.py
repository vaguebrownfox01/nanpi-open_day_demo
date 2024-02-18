import time
import socket
import random
import math

PORT = 1234
ENCODE = 'utf-8'

def setup_socket():
    print('Setup server...'); time.sleep(1)

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)

    print(f"host name: {host_name}, ip: {ip}")

    soc.bind((host_name, PORT))

    print('Waiting for connection...')
    soc.listen(5)


    client_soc, addr = soc.accept()
    clint_name = client_soc.recv(1024).decode()

    print(f"Receiced connection from {addr}")
    print(f"connection established form {clint_name}")


    connection = client_soc

    return connection


def send_data(data, connection):
    if (not connection): return print("Not connected")
    
    # message string
    msg = f"{data}"

    print(f"SENDING MESSAGE to client: {msg} of type({type(msg)})")

    connection.send(bytes(msg, ENCODE))

def test_loop():
    speeds = [(round((math.sin(0 + i * ((2 * math.pi) / 100)) + 1) * 50)) for i in range(101)]
    conn = setup_socket()

    c = 0
    while True:
        c += 1
        data = speeds[c % len(speeds)]
        send_data(data, conn)
        time.sleep(0.03)

if __name__ == "__main__":
    test_loop()