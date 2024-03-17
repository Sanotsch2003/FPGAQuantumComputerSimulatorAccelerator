from classes.quantumCircuits import QiskitQCSimulator, CustomQCSimulator, FPGAQCCompiler, QuantumCircuit
import numpy as np


#define the number of qubits here
nQbits = 4
filename = "test"
circuit = FPGAQCCompiler(nQbits)
circuit.startTimer()

#define the circuit here
circuit.h(target=1)
#end

circuit.stopTimer()
circuit.serialTransmitStateVector()
circuit.compile(name=filename)


testCircuit = QiskitQCSimulator(nQbits)
    
testCircuit.circuit = circuit.circuit
testCircuit.run()
testCircuit.printStateVector()

