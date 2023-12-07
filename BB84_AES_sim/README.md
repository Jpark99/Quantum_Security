# Communication Protocol Simulator with BB84 and AES
Based on https://github.com/Qiskit/textbook/blob/main/notebooks/ch-algorithms/quantum-key-distribution.ipynb

# Product mission
Provide cybersecurity professionals with a cutting-edge communication protocol for the transmission of sensitive data, providing safety even against quantum computers. 

## Key generation: BB84 Quantum Key Distribution protocol

- **Photon Preparation:**<br/>
Alice sends particles of light (photons) to Bob.

- **Quantum Transmission:**<br/>
Each photon carries a special property, like polarization, which represents a bit of information.

- **Photon Measurement:**<br/>
Bob measures the polarization of each received photon.

- **Public Communication:**<br/>
Bob tells Alice, through a regular communication channel, which polarization he measured for each photon.

- **Error Detection:**<br/>
Alice and Bob compare a few photons to check for any discrepancies. If there are errors, it may indicate eavesdropping.

- **Error Correction:**<br/>
If errors are detected, Alice and Bob abort and try again.

- **Privacy Amplification:**<br/>
They sample the shared information to create a shorter, more secure key.

- **Secret Key Generation:**<br/>
The remaining information becomes their secret key, which can be used for secure communication.

- **Secure Communication:**<br/>
Alice and Bob now use this secret key for encrypting and decrypting messages, ensuring secure communication.

<a data-flickr-embed="true" data-header="true"  href="https://www.researchgate.net/figure/Key-exchange-in-the-BB84-protocol-implemented-with-polarization-of-photons-adapted-from_fig1_324115273" title=""><img src="https://github.com/Jpark99/Quantum_Security/assets/10427379/257c7751-839a-42ac-a252-b19378e0b12f" width="320" height="213" alt="Caught in the App LONDON"></a>

 _(source: [The Impact of Quantum Computing on Present Cryptography](https://www.researchgate.net/figure/Key-exchange-in-the-BB84-protocol-implemented-with-polarization-of-photons-adapted-from_fig1_324115273) by Kamer Vishi on ResearchGate_



## Guide

