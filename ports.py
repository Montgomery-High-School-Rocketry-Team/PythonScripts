import serial
from utils import *
import time

DECODE = 'utf-8'



def dataPort(name: str, baudrate: int):
    ser = serial.Serial(name, baudrate)
    ser.timeout = 2.0
    lines = [] 
    print("python: getting data -- please wait at least 3 seconds.")

    time.sleep(3)

    while ser.inWaiting() > 0:
        
        print("python: reading data...")
        line = ser.readline()
        cc = str(line,  DECODE)
        cc.strip("\n")
        lines.append(cc)

    print("\npython: finished reading data - writing data\n")

    for i in progressbar(range(len(lines)), "Writing data: ",  40):
        writeData(lines[i], i)

    print("python: finished writing data - exitting...\n")
   # for i in progressbar(range(total), "Writing Data: "):
        

#dataPort('/dev/tty.usbmodem124139201', 9600)