## Sprint 3: Quantum Computation and Cybersecurity

So far, we have implemented the BB84 Quantum Key Distribution protocol for key generation, and we have integrated it with the symmetric AES algorithm for the encryption of data. The procedure to transfer data between two parties is the following:

1. Use BB84 QKD protocol for safe generation of an encryption key. If somebody tries to intercept the key, the process is aborted. Otherwise, a key encryption that is shared between the sender and the receiver is generated. Initially, the size of the obtained key is larger than 256 bits (necessary key size for AES encryption), so we sample it to reduce it to 256 bits.
2. The generated quantum key is used by the sender to encrypt data in the AES algorithm. This encryption method requires a specific key length (128, 192, or 256 bits). In this case, we chose the length to be 256 bits for an enhaced security.
3. Once the encrypted data is transmitted, the receiver uses the same private quantum key to decrypt the data. 
