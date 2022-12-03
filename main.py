from listports import *
from ports import *

#print(listPort())
# TODO find a method to determine the correct port

#WAIT 10 SECONDS FOR DATA TO COME OVER
dataPort(listPort()[0], 9600)