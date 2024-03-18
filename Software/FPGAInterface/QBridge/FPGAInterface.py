import threading
import time
import sys
from tools import convertToComplex, getSerialPort, sendByte, uploadProgram


helpInfo = "Commands: \n" \
            "exit: exit the program\n" \
            "help: show this help message\n" \
            "send <byte String>: send a byte to the FPGA\n" \
            "upload <file name>: upload a file to the FPGA\n" \
            "getRunTime <HexCode>: get the run time of a program assumung the timer runs with a 100MHz clock frequency\n" \
            "connect <baudRate>: connect to the FPGA with the specified baud rate\n"

terminate = False
port = None

def waitForSerialData(showEntireStateVector, roundingThreshold = 0.00000001):
    global port
    time.sleep(1)

    i = 0
    current_number_bit_string = ""
    last_data_time = time.time()
    transmitting = False

    while True:
        if port == None:
            time.sleep(10)
            continue

        if time.time() - last_data_time > 0.5:
            if transmitting:
                print("End of data")
                transmitting = False
                i = 0

        if port.in_waiting:
            if not transmitting:
                #new line
                print("\n")
                print("Start of data")
                transmitting = True
            data = port.read(port.in_waiting)
            last_data_time = time.time()

            for byte in data:
                    byte = format(byte, '08b')
                    if byte == "00000001": # start byte
                        current_number_bit_string = ""

                    elif byte == "10000001": # end byte
                        if len(current_number_bit_string) == 70:
                            current_number_bit_string = current_number_bit_string[0:64]

                            c = convertToComplex(current_number_bit_string, roundingThreshold)
                            if c.real != 0 or showEntireStateVector:
                                print(i, c)
                                pass
                            i += 1

                    else:
                        current_number_bit_string += byte[0:7]

def terminalInteraction():
    global port
    global terminate
    while True:
        userInput = input("Enter command: ")

        if userInput == "exit":
            terminate = True
            break

        elif userInput == "help":
            print(helpInfo)

        elif userInput.split(" ")[0] == "send":
            if connected:
                byteInput = userInput.split(" ")[1]
                try:
                    byte_value = int(byteInput, 2)
                    print(f"Byte value: {byte_value}")
                    byte_data = byte_value.to_bytes(1, byteorder='big')
                    print(f"Byte data: {byte_data}")

                except ValueError as e:
                    print(f"Error converting binary string to byte: {e}")

                sendByte(port = port, byte = byte_data)
            else:
                print("Not connected to FPGA")

        elif userInput.split(" ")[0] == "upload":
            if connected:
                fileName = userInput.split(" ")[1]
                uploadProgram(port, fileName)
            else:
                print("Not connected to FPGA")
        elif userInput.split(" ")[0] == "getRunTime":
            if connected:
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
            else:
                print("Not connected to FPGA")

        elif userInput.split(" ")[0] == "connect":
            if connected:
                print("Already connected to FPGA")
            else:
                baudRate = int(userInput.split(" ")[1])
                port, portname = getSerialPort(baudRate)
                if port is None:
                    print("No serial port found, please connect the FPGA and type <connect baudrate> to connect")
                else:
                    print(f"Connected to {portname} with baud rate {baudRate}")
                    connected = True

def FPGAInterface(showEntireStateVector = False, roundingThreshold = 0.00000001):

    print("Welcome to the Quantum Bridge terminal interface")
    print("Type 'help' for a list of commands")

    read_thread = threading.Thread(target=waitForSerialData, args=(showEntireStateVector, roundingThreshold))
    read_thread.daemon = True
    read_thread.start()

    write_thread = threading.Thread(target=terminalInteraction, args=())
    write_thread.daemon = True
    write_thread.start()

    while not terminate:
        pass

    sys.exit()


FPGAInterface(showEntireStateVector=False, roundingThreshold=0.00000001)