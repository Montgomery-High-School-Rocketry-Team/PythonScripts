from listports import *
from ports import *

#print(listPort())
# TODO find a method to determine the correct port
#TODO i just remembered i need to make sure that  the team member has termainl set as the running thing (brian and I)
#WAIT 10 SECONDS FOR DATA TO COME OVER
dataPort(listPort()[0], 9600)
