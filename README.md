# Noisy but Nice (Adam Godel, Jacky Lin, Felix Bagurskas Rubio, Ege Topkoc, Artemios Kayas)
We had a great time working on the Alice & Bob challenge at iQuHACK 2025! Our code and documentation, as well as a short reflection of our experiences, can be found in the [Challenge.ipynb](https://github.com/adam-godel/2025-Alice-and-Bob/blob/main/submissions/Challenge.ipynb) Jupyter notebook. Our slides presentation can be found [here](https://docs.google.com/presentation/d/11sxBHB6MFSx5BH7zxZ23o3aZRl83dwnfjfeL56ac5fA/edit?usp=sharing).

# Alice & Bob challenge at iQuHACK 2025

**Welcome to the challenge: Simulating the dynamics of a cat qubit at the circuit level**

## Overview

Error correction is a cornerstone of scalable quantum computing. In quantum systems, errors arise from environmental noise and imperfections in hardware. To build quantum computers capable of solving real-world problems, such as optimizing supply chains or advancing drug discovery, we need robust error correction to maintain the integrity of quantum information.

Cat qubits, developed at Alice & Bob, are a promising approach to reducing the hardware overhead required for error correction. Inspired by Schrödinger's cat, they leverage quantum superposition states in superconducting circuits. These states are engineered to resist certain types of errors, such as bit-flips, more naturally than standard qubits. This unique property significantly lowers the number of physical qubits needed to implement a reliable logical qubit, bringing us closer to practical quantum computing.

In this challenge, you will explore how cat qubits work and how they can be realized by carefully engineering a superconducting circuit. You will simulate the dynamics of cat qubits with `dynamiqs`, a high-performance simulation package using GPU acceleration.

![](media/wigner-cat7.gif "Wigner function of a dissipatively stabilized cat state")

## The Challenge

The challenge is described in detail [here](Challenge.md).

The challenge consists of multiple parts:
1. Simulate the dynamics of cat qubits at the effective Hamiltonian level.
2. Simulate the dynamics at the hardware level.

## What you will learn in this challenge:
- Understand Alice and Bob's cat qubits.
- Understand essential circuit QED.
- Code high-performance numerical quantum simulations in `dynamiqs` on GPUs.
- Simulate the dynamics of cat qubits on different levels.

## Who is this challenge for?
This challenge is for everyone who wants to learn about cat qubits. 
In the challenge, you will encounter tasks of various difficulty.
Prior knowledge about basic quantum mechanics and programming is benefitial, but not strictly required.
If you have questions or need some guidance, we are always happy to help.

## What if you have questions?
No worries, someone from A & B is here to help you should you have any questions or encounter problems.
We will also have someone who can help you remotely.

## How will the challenge be graded?
The challenge will be graded based on the submission of your code, documentation, presentation on Sunday, as well as your ingenuity of approaching the challenge. Please submit everything as a team. For details, see the [challenge description](Challenge.md).

## Working on qBraid

You will have access to GPUs on the qBraid platform.

To access the challenge repository in qBaid you can directly launch it on qBraid:

[<img src="https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png" width="150">](https://account.qbraid.com/?gitHubUrl=https://github.com/iQuHACK/2025-Alice-and-Bob.git)

While you can run simulations using `dynamiqs` locally, you can benefit from GPU-accelerated simulations with **qbraid**.


## Resources

We have compiled a [list of useful resources](Resources.md) to get started, including:
- Detailed tutorials and background information about cat qubit physics and `dynamiqs`.
- References on background physics: circuit-QED, cat qubits, open quantum systems.
