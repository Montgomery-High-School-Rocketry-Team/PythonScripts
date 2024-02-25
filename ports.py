import serial
from utils import *
import time


def dataPort(name: str, baudrate: int):
    DECODE = "utf-8"
    KEEPALL = False
    count = 25

    ser = serial.Serial(name, baudrate)
    ser.timeout = 10
    hashtag_count = 0
    lines = []

    while True:
        if hashtag_count == 0:
            line = str(ser.readline(), "utf-8")
            print("python LOG: " + line)
            if line.startswith("##"):
                hashtag_count += 1
                print(f"python: getting data - will take a few seconds")
        elif hashtag_count == 1:
            if not KEEPALL:
                count += 1
                if count < 25:
                    continue

            line = str(ser.readline(), "utf-8")
            if line.startswith("##"):
                hashtag_count += 1
            else:
                line = line.strip("\n")
                line = line.strip("\r")
                line = line + "\n"
                if not KEEPALL:
                    if line.count(",") == 10:
                        lines.append(line)
        elif hashtag_count == 2:
            break
        else:
            break

    # lines = str(ser.readall(), "utf-8").split("\n")
    print("\npython: finished reading data - writing data\n")

    for i in progressbar(range(50), "Writing data: ", 40):
        pass

    print("python: wrapping up...")
    writeData(lines)
    print("python: done!")

    print("python: finished writing data - exitting...\n")


# for i in progressbar(range(total), "Writing Data: "):


# dataPort('/dev/tty.usbmodem124139201', 9600)
