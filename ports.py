import serial
from utils import *

DECODE = 'utf-8'



def dataPort(name: str, baudrate: int):
    counter = 0
    ser = serial.Serial(name, baudrate)
    total = 100
    for i in progressbar(range(total), "Writing Data: "):
        line = ser.readline()
        cc = str(line,  DECODE)


        #print(cc)

        writeData(cc, counter)
            
        
        counter += 1

