import serial
from utils import *
import time

DECODE = 'utf-8'



def dataPort(name: str, baudrate: int):
    ser = serial.Serial(name, baudrate)
    ser.timeout = 10
    hashtag_count = 0
    lines = []
    
    
    
    while True:
        if(hashtag_count == 0):
            line = str(ser.readline(), "utf-8")
            #print("python LOG: " + line)
            if(line.startswith("##")):
                hashtag_count += 1
                print(f"python: getting data - will take a few seconds")
                
        elif (hashtag_count == 1):
            lines.append( str(ser.readline(), "utf-8"))
            if(line.startswith("##")):
                hashtag_count += 1
        
        elif (hashtag_count == 2):
            break
        else:
            break
        
            
        
    
    
    # lines = str(ser.readall(), "utf-8").split("\n")
    print("\npython: finished reading data - writing data\n")



    for i in progressbar(range(50), "Writing data: ",  40):
        pass

    print("python: wrapping up...")
    writeData(lines)
    print("python: done!")

    print("python: finished writing data - exitting...\n")
   # for i in progressbar(range(total), "Writing Data: "):
        

#dataPort('/dev/tty.usbmodem124139201', 9600)