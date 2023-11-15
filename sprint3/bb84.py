# Jiwon Park, Inigo Perez Gamiz

from qiskit import QuantumCircuit, Aer
from numpy.random import randint
import numpy as np

def encode_key(bits, bases, n):
    message = []
    for i in range(n):
        qc = QuantumCircuit(1,1)
        if bases[i] == 0: # Prepare qubit in Z-basis
            if bits[i] == 0:
                pass 
            else:
                qc.x(0)
        else: # Prepare qubit in X-basis
            if bits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        message.append(qc)
    return message

def measure_key(key, bases, n):
    measurements = []
    for q in range(n):
        if bases[q] == 0: # measuring in Z-basis
            key[q].measure(0,0)
        if bases[q] == 1: # measuring in X-basis
            key[q].h(0)
            key[q].measure(0,0)
        aer_sim = Aer.get_backend('aer_simulator')
        result = aer_sim.run(key[q], shots=1, memory=True).result()
        measured_bit = int(result.get_memory()[0])
        measurements.append(measured_bit)
    return measurements

def remove_bits(alice_bases, bob_bases, bits, n):
    final_bits = []
    for q in range(n):
        if alice_bases[q] == bob_bases[q]:
            # If both used the same basis, add
            # this to the list of final bits
            final_bits.append(bits[q])
    return final_bits

def sample_bits(bits, selection):
    sample = []
    for i in selection:
        # use np.mod to make sure the
        # bit we sample is always in 
        # the list range
        i = np.mod(i, len(bits))
        # pop(i) removes the element of the
        # list at index 'i'
        sample.append(bits.pop(i))
    return sample

def run_bb84(seed, n, sample, eve):
    np.random.seed(seed=seed)

    ## Step 1
    # Alice generates bits
    alice_bits = randint(2, size=n)

    ## Step 2
    # Create an array to tell us which qubits
    # are encoded in which bases
    alice_bases = randint(2, size=n)
    key = encode_key(alice_bits, alice_bases, n)
    # Check if there is interception
    if (eve):
        eve_bases = randint(2, size=n)
        intercepted_key = measure_key(key, eve_bases, n)
        print("Warning: somebody tried to intercept the encryption key")
    ## Step 3
    # Decide which basis to measure in
    bob_bases = randint(2, size=n)
    bob_bits = measure_key(key, bob_bases, n)
    
    ## Step 4
    # Clean keys
    alice_key = remove_bits(alice_bases, bob_bases, alice_bits, n)
    bob_key = remove_bits(alice_bases, bob_bases, bob_bits, n)

    ## Step 5
    # Sample keys to get only 256 bits
    bit_selection = randint(n, size=sample)

    bob_sample = sample_bits(bob_key, bit_selection)
    alice_sample = sample_bits(alice_key, bit_selection)
    print("alice_key = ",alice_sample)
    print("bob_key = ", bob_sample)
    print("Successful key generation: ", alice_sample == bob_sample)
    if alice_sample == bob_sample:
        return alice_sample
    return None


def bb84_protocol():
    seed = randint(9949)
    size = 600
    sample = 256
    eve_intercepts = False
    return run_bb84(seed, size, sample, eve_intercepts)


if __name__=="__main__":
    bb84_protocol()
