import serial
from time import sleep


#ser = serial.Serial('/dev/ttyUSB0', 115200)

s = serial.Serial('/dev/ttyACM0', 115200)

queue = [0 for i in range(10)]
while (True):
    receive = s.readline()
    if receive.decode('ascii') == "\r\n":
        continue
    
    r_decoded = int(receive.decode('ascii'))
    queue.append(r_decoded)
    queue.pop(0)

    print(queue)

ser.close()