import serial

FILE_NAME = "data.csv"
FILE_HEADER = "#Time(ms),Accel x(m/s^2),Accel y(m/s^2),Accel z(m/s^2),Gyro x(radians/s),Gyro y(radians/s),Gyro z(radians/s),Temperature(C),Pressure(hPa),Altitude(m)"
WRITE_DATA = "w"
READ_DATA = "r"
DECODE = 'utf-8'


def dataPort(name: str, baudrate: int):
    counter = 0
    ser = serial.Serial(name, baudrate)
    while counter < 100:
        line = ser.readline()
        cc = str(line,  DECODE)


        print(cc)
    
        writeData(cc, counter)
            
        
        counter += 1

def writeData(cc, counter:int):
    if(counter == 0):
        with open(FILE_NAME, WRITE_DATA) as f:
            f.writelines([FILE_HEADER,cc])
        return
    lines = []
    with open(FILE_NAME, READ_DATA ) as f:
            lines = f.readlines()
        
    lines.append(cc)
    with open(FILE_NAME, WRITE_DATA) as f:
        f.writelines(lines)
    return
