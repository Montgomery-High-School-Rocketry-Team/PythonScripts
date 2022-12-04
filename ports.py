import serial
from utils import *
import time

DECODE = 'utf-8'



def dataPort(name: str, baudrate: int):
    ser = serial.Serial(name, baudrate)
    ser.timeout = 10
    
    print(f"python: getting data - will take a few seconds")
    lines = str(ser.readall(), "utf-8").split("\n")
    print("\npython: finished reading data - writing data\n")

    for i in progressbar(range(len(lines)), "Writing data: ",  40):
        writeData(lines[i], i)

    print("python: finished writing data - exitting...\n")
   # for i in progressbar(range(total), "Writing Data: "):
        

#dataPort('/dev/tty.usbmodem124139201', 9600)