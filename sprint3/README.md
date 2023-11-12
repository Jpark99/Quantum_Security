## Sprint 3: Quantum Computation and Cybersecurity

So far, we have implemented the BB84 Quantum Key Distribution protocol for key generation, and we have integrated it with the symmetric AES algorithm for the encryption of data. The procedure to transfer data between two parties is the following:

1. Use BB84 QKD protocol for safe generation of an encryption key. If somebody tries to intercept the key, the process is aborted. Otherwise, a key encryption that is shared between the sender and the receiver is generated.
2. The generated key is used to encrypt data in the AES algorithm. This encryption method requires a specific key length (128, 192, or 256 bits), so before using the key we have to extend or reduce it to the desired case. For an enhaced security, we choose the length to be 256 bits.
