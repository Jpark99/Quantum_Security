from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_histogram
from numpy.random import randint
import numpy as np

class QKD:
    def __init__(self, n=100, sample_size=25, seed=2978):
        self.n = n
        self.sample_size = sample_size
        self.seed = seed
        self.alice_bits = None
        self.alice_bases = None
        self.message = None
        self.eve_bases = None
        self.intercepted_message = None
        self.bob_bases = None
        self.bob_results = None
        self.alice_key = None
        self.bob_key = None
        self.bob_sample = None
        self.alice_sample = None

    def encode_message(self):
        self.alice_bits = randint(2, size=self.n)
        self.alice_bases = randint(2, size=self.n)
        message = []
        for i in range(self.n):
            qc = QuantumCircuit(1, 1)
            if self.alice_bases[i] == 0:  # Prepare qubit in Z-basis
                if self.alice_bits[i] == 0:
                    pass
                else:
                    qc.x(0)
            else:  # Prepare qubit in X-basis
                if self.alice_bits[i] == 0:
                    qc.h(0)
                else:
                    qc.x(0)
                    qc.h(0)
            qc.barrier()
            message.append(qc)
        self.message = message

    def measure_message(self):
        backend = Aer.get_backend('aer_simulator')
        measurements = []
        for q in range(self.n):
            if self.bob_bases[q] == 0: # measuring in Z-basis
                self.message[q].measure(0,0)
            if self.bob_bases[q] == 1: # measuring in X-basis
                self.message[q].h(0)
                self.message[q].measure(0,0)
            aer_sim = Aer.get_backend('aer_simulator')
            result = aer_sim.run(self.message[q], shots=1, memory=True).result()
            measured_bit = int(result.get_memory()[0])
            measurements.append(measured_bit)
        return measurements
    
    def eve_measure_message(self):
        backend = Aer.get_backend('aer_simulator')
        measurements = []
        for q in range(self.n):
            if self.eve_bases[q] == 0:  # measuring in Z-basis
                self.message[q].measure(0, 0)
            if self.eve_bases[q] == 1:  # measuring in X-basis
                self.message[q].h(0)
                self.message[q].measure(0, 0)
            aer_sim = Aer.get_backend('aer_simulator')
            result = aer_sim.run(self.message[q], shots=1, memory=True).result()
            measured_bit = int(result.get_memory()[0])
            measurements.append(measured_bit)
        return measurements

    def remove_garbage(self):
        good_bits = []
        for q in range(self.n):
            if self.alice_bases[q] == self.bob_bases[q]:
                good_bits.append(self.alice_bits[q])
        return good_bits


    def sample_bits(self, bits, selection):
        sample = []
        for i in selection:
            i = np.mod(i, len(bits))
            sample.append(bits.pop(i))
        return sample

    def run(self):
        np.random.seed(seed=self.seed)
        self.encode_message()
        self.eve_bases = randint(2, size=self.n)
        self.intercepted_message = self.eve_measure_message()
        self.bob_bases = randint(2, size=self.n)
        self.bob_results = self.measure_message()
        self.alice_key = self.remove_garbage()
        self.bob_key = self.remove_garbage()
        bit_selection = randint(self.n, size=self.sample_size)
        self.bob_sample = self.sample_bits(self.bob_key, bit_selection)
        self.alice_sample = self.sample_bits(self.alice_key, bit_selection)
        print("alice_sample = ", self.alice_sample)
        print("bob_sample = ", self.bob_sample)

        return self.bob_sample == self.alice_sample

if __name__ == "__main__":
    qkd = QKD(n=100, sample_size=25, seed=298)
    no_interception = qkd.run()
    print("No interception detected:", no_interception)
