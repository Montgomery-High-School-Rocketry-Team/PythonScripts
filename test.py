import serial
from serial.tools.list_ports import comports

comport = list(comports())
listComs = []
for port in comport:
    for portt in port:
        print(portt)
        
ser = serial.Serial("COM3", 9600, timeout=2)

# while True:
#     #asfasdf
#     ads=0
#print(str(ser.readline(), "utf-8"))
#print(str(ser.read_all(), "utf-8"))
print(str(ser.readall(), "utf-8"))