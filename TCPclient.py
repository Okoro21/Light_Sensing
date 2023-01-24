import socket
import time

TCP_IP = "192.168.0.47"
TCP_PORT = 65432

BUFFER_SIZE = 1024

while True:
    # Connect to Server socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    # Encode that the client is ready to receive data
    flag = 'Rx_True'
    flag_bytes = flag.encode('utf-8')
    s.sendall(flag_bytes)

    # Recieve pwm signal from the server
    data = s.recv(1024)
    data_decode = data.decode('utf-8')

    # Ouput this to pwm signal
    print(f"current pwm is {data_decode}")
    
    time.sleep(3)
    s.close()

