import serial
import io

if __name__ == '__main__':

    def calculate(x: float):
        if float(x) > 9.96:
            x = float(x) * 10
            return str(x)
        elif float(x) < 9.95:
            return str(x)

    def receive():
        serrx = serial.Serial('COM2', 9600)
        #print(f'Port {serrx.name} is opened')
        while True:
            line = serrx.readline().decode('utf')
            return line

    sertx = serial.Serial('COM3', 9600)
    print(f'{sertx.name} is opened for transmit')
    while True:
        sertx.write(calculate(receive()).encode('ascii'))

        #flush()


        #ser.write(transfer)

    #calculate()
