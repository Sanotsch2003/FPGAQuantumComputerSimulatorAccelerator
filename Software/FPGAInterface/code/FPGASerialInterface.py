from helperFunctions.functions import sendByte, readSerial, getSerialPort, uploadProgram
import threading
import sys


terminate = False

def writeSerial(port):
    global terminate
    while True:
        userInput = input("Enter command (type help for list of commands):\n")

        if userInput == "exit":
            terminate = True
            break
            
        elif userInput == "help":
            print("Commands: ")
            print("exit: exit the program")
            print("help: show this help message")
            print("send <byte String>: send a byte to the FPGA")
            print("upload <file name>: upload a file to the FPGA")
            print("getRunTime <HexCode> get the run time of a program assumung the timer runs with a 100MHz clock frequency")

        elif userInput.split(" ")[0] == "send":
            byteInput = userInput.split(" ")[1]
            try:
                byte_value = int(byteInput, 2)
                print(f"Byte value: {byte_value}")
                byte_data = byte_value.to_bytes(1, byteorder='big')
                print(f"Byte data: {byte_data}")

            except ValueError as e:
                print(f"Error converting binary string to byte: {e}")

            sendByte(port = port, byte = byte_data)

        elif userInput.split(" ")[0] == "upload":
            fileName = userInput.split(" ")[1]
            uploadProgram(port, fileName)

        elif userInput.split(" ")[0] == "getRunTime":

            commandLength = len(userInput.split(" "))

            if commandLength == 1:
                print("Please enter the hex code")
                continue
                
            elif commandLength > 1:
                try:
                    intCode = int(userInput.split(" ")[1], 16)
                    clkFreq = 100000000
                    print(f"Using default clock frequency of {clkFreq/1000000} MHz")
                    print(f"Program took {intCode/clkFreq} seconds ({intCode/clkFreq*1000}ms) to run")


                except ValueError as e:
                    print(f"Error converting hex string to int: {e}")
            
#port = getSerialPort(921600)
#port = getSerialPort(9600)
port = getSerialPort(460800)
read_thread = threading.Thread(target=readSerial, args=(port, False, 0.0000001))
read_thread.daemon = True
read_thread.start()

write_thread = threading.Thread(target=writeSerial, args=(port,))
write_thread.daemon = True
write_thread.start()

while not terminate:
    pass

sys.exit()
