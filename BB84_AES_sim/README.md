<h1 align="center"> Communication Protocol Simulator based on BB84 and AES </h1>

Based on https://github.com/Qiskit/textbook/blob/main/notebooks/ch-algorithms/quantum-key-distribution.ipynb

# Description
Simulator intended for the secure transmission of data between two parties. Initially, a private shared key is generated using the BB84 Quantum Key Distribution protocol. This key is later used to encrypt and decrypt data during its transmission. The communication protocol is intended only for quantum computers, and a quantum channel is necessary for an actual physical implementation.

## Key generation: BB84 Quantum Key Distribution protocol

Quantum Key Distribution is a secure communication protocol that aims to generate a shared private key between two parties (Alice and Bob). It is particularly interesting because it relies on the laws of Quantum Mechanics, specially on two main principles: the disturbance by measurement and the no-cloning theorem. If a third party (Eve) tries to intercept the key while it is being generated, by the no-cloning theorem she will not be able to copy the state of the key. The only way she has to get information about the key is measuring and, consequently, disturbing it. As a result, Alice and Bob will be able to detect the attack.

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

