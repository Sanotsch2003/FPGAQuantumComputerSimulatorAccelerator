
import serial
import serial.tools.list_ports
from tqdm import tqdm
import pathlib



def convertToDecimal(binary_string, roundingThreshold = 0.00000001):
    temp = 0
    if binary_string[0] == '1':
        temp = -2

    for i in range(31):
        if binary_string[i+1] == '1':
            temp = temp + 2 ** (-i)

    if temp < roundingThreshold and temp > -roundingThreshold:
        temp = 0
    return temp

def convertToComplex(binary_string, roundingThreshold = 0.00000001):

    real = binary_string[0:32]
    imaginary = binary_string[32:64]

    real = convertToDecimal(real, roundingThreshold)
    imaginary = convertToDecimal(imaginary, roundingThreshold)

    c = complex(real, imaginary)
    return c

def getSerialPort(baudRate = 9600):
    ports = serial.tools.list_ports.comports(include_links=True)
    if len(ports) == 0:
        return None, None
    else:
        return serial.Serial(ports[0].device, baudRate, timeout=1),  ports[0].device

def sendByte(port, byte):
    try:
        port.write(byte)
    except serial.SerialException as e:
        print(f"Error sending data: {e}")

def fileLength(filePath):
    with filePath.open() as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def uploadProgram(port, filepath, filename):
    StartEndByte = "11111111"

    if not filename.endswith(".prg"):
        filename = filename + ".prg"
    filePath = pathlib.Path(filepath) / pathlib.Path(filename)
    try:
        sendByte(port = port, byte = int(StartEndByte, 2).to_bytes(1, byteorder='big')) #send start byte
        print(f"Opening file {filename}...")
        with filePath.open('r') as file:
            total_lines = fileLength(filePath)
            for line in tqdm(file, total=total_lines, desc="Uploading"):
                byte = line.strip().split(" --")[0]
                try:
                    byte_value = int(byte, 2)
                    byte_data = byte_value.to_bytes(1, byteorder='big')
                    sendByte(port = port, byte = byte_data)

                except ValueError as e:
                    print(f"Error converting binary string to byte: {e}")

        sendByte(port = port, byte = int(StartEndByte, 2).to_bytes(1, byteorder='big')) #send end byte
        print("File uploaded")

    except Exception as e:
        print(f"Error uploading program: {e}")
