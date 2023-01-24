import socket
import time

TCP_IP = "192.168.0.47"
TCP_PORT = 65432

BUFFER_SIZE = 1024

# Create Server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

while True:
    '''

    Communicate with STM here

    Get desired PWM output signal here

    '''
    pwm_signals = b'150'

    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(BUFFER_SIZE)
        flag = data.decode('utf-8')

        # When the client is ready to receive data
        if flag == 'Rx_True':
            print('Client is ready to receive')
            conn.sendall(pwm_signals)


