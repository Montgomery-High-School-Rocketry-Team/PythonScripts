import serial
import sys
import glob
import serial
from serial.tools.list_ports import comports

def serialPorts():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def listPort():
    comport = list(comports())
    listComs = []
    for port in comport:
        for ports in port:
            print(f"Python LOG -- PORT INFO: {ports}")
        if port[1].startswith("USB Serial") and port[2].startswith("USB"):
            listComs.append(port[0])
    return listComs
            
        #for portinfo in port:
        #    
        #    print(portinfo)  
            
    
    # ports = serialPorts()
    # for port in ports:
    #     print(port)

