import serial


port = '/dev/cu.usbmodem14201'
baudrate = 115200

con = serial.Serial(port,baudrate)

while True:
    print("insert op :", end=' ')
    op = input()
    con.write(op.encode())
