import serial

CmdMacId=252
CmdFan=253
CmdHeat=254
CmdTemp=255

Max_Heat=100
Max_Fan=100

class SBHS:
    def __init__(self):
        self.heat=0
        self.fan=0
        self.temperature=0
        self.ser=serial.Serial(port="/dev/ttyUSB0", baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=2)

    def setHeat(self,heatval):
        self.ser.write(chr(CmdHeat))
        self.ser.write(chr(heatval))

    def setFan(self,fanval):
        self.ser.write(chr(CmdFan))
        self.ser.write(chr(fanval))

    def getTemp(self):
        self.ser.write(chr(CmdTemp))
        temp=ord(self.ser.read(1)) + (0.1 * ord(self.ser.read(1)))
        return temp
