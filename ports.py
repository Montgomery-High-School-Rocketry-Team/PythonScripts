import serial
from utils import *
import time

DECODE = 'utf-8'



def dataPort(name: str, baudrate: int):
    ser = serial.Serial(name, baudrate)
    ser.timeout = 10
    
    while True:
        line = str(ser.readline(), "utf-8")
        #print("python LOG: " + line)
        if(line.startswith("#")):
            break
    
    print(f"python: getting data - will take a few seconds")
    lines = str(ser.readall(), "utf-8").split("\n")
    print("\npython: finished reading data - writing data\n")



    for i in progressbar(range(100), "Writing data: ",  40):
        pass

    print("python: wrapping up...")
    writeData(lines)
    print("python: done!")

    print("python: finished writing data - exitting...\n")
   # for i in progressbar(range(total), "Writing Data: "):
        

#dataPort('/dev/tty.usbmodem124139201', 9600)