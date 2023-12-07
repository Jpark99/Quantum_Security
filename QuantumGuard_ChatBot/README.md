# QuantumGuard ChatBot

## Next-Gen Encrypted Messaging with Kyber and ChatGPT

QuantumGuard ChatBot is a secure and innovative chatbot implementation that leverages the power of Kyber512 encapsulation and ChatGPT for a next-generation encrypted communication experience.

## Features

- **Shared Key Generation:** Utilize the Kyber512 encapsulation method to generate shared keys, ensuring a robust encryption foundation based on the Learning With Errors (LWE) lattice problem

- **AES Encryption:** Encrypt and decrypt messages using the generated key through the Advanced Encryption Standard (AES)

- **ChatBot Responses:** ChatBot's responses are generated using the OpenAI API

## Kyber

- This chatbot implementation uses scripts from https://github.com/GiacomoPope/kyber-py for Kyber512 encapsulation method
  
- Kyber is a Post-Quantum Key Encapsualtion Method (PQ-KEM), resistant to Quantum Computer attacks

- Kyber is based on Learning with Error Lattice problem, which is not efficiently solvable by any Quantum algorithm as of now

- A simple look at KEM:

![image](https://github.com/Jpark99/Quantum_Security/assets/10427379/00cd9bf7-794d-424d-a32a-e14660a7c50f)

- To learn more about Kyber or PQ-KEM, take a look here: https://blog.cloudflare.com/post-quantum-key-encapsulation/

## Guide

- Install dependencies:
```bash
pip install -r requirements.txt
```
- Run Server:
```bash
python server.py
```
- Run Client:
  
