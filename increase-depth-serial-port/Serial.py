import serial.tools.list_ports

if __name__ == '__main__':
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()

    portList = []
    for OnePort in ports:
        portList.append(str(OnePort))
        print(str(OnePort))
    val = input('Select port: COM')
    for x in range(0, len(portList)):
        if portList[x].startswith('COM' + str(val)):
            portVar = 'COM' + str(val)
            print(portVar)
    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.open()

    while True:
        def edit(x):
            print(f'{x} dfv')
        if serialInst.in_waiting:
            packet = serialInst.readline()
            before = packet.decode('utf')
            edit(before)

