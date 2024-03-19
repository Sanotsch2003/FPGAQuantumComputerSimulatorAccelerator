from QBridge.Benchmarks import groversAlgorithm, randomCircuit


randomCircuit(nRandomGates=30, nQubits=27, printRunTimes=True, runCustom=False)


def calculatePointers(n, t, c):
    distance = 2**t
    print(f"distance: {distance}")
    max_o = int(2**(n-1)/c)
    print(f"max_o: {max_o}")
    
    o = 0
    pointer_a = 2*distance*int(o*c/distance)+(o*c)%distance
    pointer_b = pointer_a + distance
    print(f"o: {o} pointer_a: {pointer_a} pointer_b: {pointer_b}")
    o += 1

    while o < max_o:
        pointer_a = 2*distance*int(o*c/distance)+(o*c)%distance
        pointer_b = pointer_a + distance
        print(f"o: {o} pointer_a: {pointer_a} pointer_b: {pointer_b}")
        o += 1
n = 5
t = 0
simulator = CustomQCSimulator(n)
simulator.h(t)
simulator.run()

calculatePointers(n=n, t=t, c=4)