from Simulation import QiskitQCSimulator, CustomQCSimulator, FPGAQCCompiler, QuantumCircuit
import numpy as np

def randomCircuit(circuit="random", nRandomGates=100, possibleGates=["h", "cnot", "x", "t", "ccnot"], nQubits=3, printStateVector=False, printCircuit=False, printRunTimes = False, runQiskit=True, runCustom=True, saveFPGAProgram=False, FPGAProgramName=""):
    if runQiskit:
        qiskitQC = QiskitQCSimulator(nQubits)
    if runCustom:
        customQC = CustomQCSimulator(nQubits)
    
    if saveFPGAProgram:
        FPGAqcCompiler = FPGAQCCompiler(nQubits)
        FPGAqcCompiler.startTimer()
    else:
        qCircuit = QuantumCircuit(nQubits)


    if circuit == "random":
        if saveFPGAProgram:
            FPGAqcCompiler.createRandomCircuit(nRandomGates, possibleGates)
            circuit = FPGAqcCompiler.circuit
        else:
            qCircuit.createRandomCircuit(nRandomGates, possibleGates)
            circuit = qCircuit.circuit
        
        if runQiskit:
            qiskitQC.circuit = circuit
        if runCustom:
            customQC.circuit = circuit

    else:
        if runQiskit:
            qiskitQC.loadCircuit(circuit)
        if runCustom:
            customQC.loadCircuit(circuit)

    if runQiskit:
        qiskitTime = qiskitQC.run()
        qiskitStateVector = qiskitQC.getStateVector()
    else:
        qiskitTime = None
    if runCustom:
        customTime = customQC.run()
        customStateVector = customQC.getStateVector()
    else:
        customTime = None


    if printCircuit:
        print(f"Executed following circuit: {circuit} (length: {len(circuit)})")

    if printRunTimes:
        print(f"Qiskit time: {qiskitTime}")
        print(f"Custom time: {customTime}")
    if printStateVector and runCustom:
        print(f"Custom circuit state vector:")
        customQC.printStateVector()
    if printStateVector and runQiskit:
        print(f"Qiskit circuit state vector:")
        qiskitQC.printStateVector()
    
    if runCustom and runQiskit:
        print(f"Difference between state vectors: {np.sum(np.abs(qiskitStateVector - customStateVector))}")


    if saveFPGAProgram:   
        FPGAqcCompiler.stopTimer()
        FPGAqcCompiler.serialTransmitStateVector()
        FPGAqcCompiler.compile(name=FPGAProgramName)
        print("Program compiled and saved")

    return qiskitTime, customTime

def groversAlgorithm():
    customQC = CustomQCSimulator(3)
    qiskitQC = QiskitQCSimulator(3)
    simulations = [customQC, qiskitQC]

    FPGAqcCompiler = FPGAQCCompiler(3)

    FPGAqcCompiler.startTimer()

    for i in range(3):
        FPGAqcCompiler.h(i)
    FPGAqcCompiler.x(0)
    FPGAqcCompiler.h(2)
    FPGAqcCompiler.ccnot(target=2, control1=0, control2=1)
    FPGAqcCompiler.x(0)
    FPGAqcCompiler.h(2)
    for i in range(3):
        FPGAqcCompiler.h(i)
    for i in range(3):
        FPGAqcCompiler.x(i)
    FPGAqcCompiler.h(2)
    FPGAqcCompiler.ccnot(target=2, control1=0, control2=1)
    FPGAqcCompiler.h(2)
    for i in range(3):
        FPGAqcCompiler.x(i)
    for i in range(3):
        FPGAqcCompiler.h(i)

    FPGAqcCompiler.stopTimer()
    FPGAqcCompiler.serialTransmitStateVector()

    circuit = FPGAqcCompiler.circuit
    customQC.circuit = circuit
    qiskitQC.circuit = circuit

    stateVectors = []
    for simulation in simulations:
        time = simulation.run()
        stateVector = simulation.getStateVector()
        stateVectors.append(stateVector)
        print(f"{simulation.__class__.__name__} took {time} seconds")
        print(f"{simulation.__class__.__name__} state vector:")
        simulation.printStateVector()


    differences = np.abs(stateVectors[0] - stateVectors[1])
    overallDifference = np.sum(differences)
    print(f"Overall difference: {overallDifference}")

    answer = input("Do you want to run the same circuit on FPGA? (y/n)")
    if answer == "y":
        name = input("Enter name for the program: ")
        FPGAqcCompiler.compile(name=name)
        print("Program compiled and saved")

    else:
        print("Closing...")
