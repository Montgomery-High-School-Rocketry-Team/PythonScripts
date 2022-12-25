import sys

FILE_NAME = "data.csv"
#FILE_HEADER = "#Time(ms),Accel x(m/s^2),Accel y(m/s^2),Accel z(m/s^2),Gyro x(radians/s),Gyro y(radians/s),Gyro z(radians/s),Temperature(C),Pressure(hPa),Altitude(m)"
WRITE_DATA = "w"
READ_DATA = "r"


def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "█"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

def writeData(lines):
    with open(FILE_NAME, WRITE_DATA) as f:
        f.writelines(lines)
    return


    

