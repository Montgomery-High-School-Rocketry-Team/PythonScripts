import serial
from utils import *

DECODE = 'utf-8'



def dataPort(name: str, baudrate: int):
    counter = 0
    ser = serial.Serial(name, baudrate)
    total = 100
    lines = [] 

    while True:
        line = ser.readline()
        cc = str(line,  DECODE)
        lines.append(cc)
        # print(len(cc))
        # print(cc)
        counter += 1
        
        



    for i in range(len(lines)):
        writeData(lines[i], i)

   # for i in progressbar(range(total), "Writing Data: "):
        

#dataPort('/dev/tty.usbmodem124139201', 9600)