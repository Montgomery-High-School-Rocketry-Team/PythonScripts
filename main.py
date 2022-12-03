from listports import *
from ports import *

#listPort()
# TODO find a method to determine the correct port

#WAIT 10 SECONDS FOR DATA TO COME OVER
dataPort(serialPorts()[1], 9600)