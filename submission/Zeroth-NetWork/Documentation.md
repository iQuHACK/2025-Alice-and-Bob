# Alice & Bob challenge // Zeroth-NetWork


## Overview

Over the last 24 hours, learned about cat qubits developed by Alice & Bob. We jumped into the principles of quantum error correction and learned how cat qubits leverage quantum superposition to resist certain types of errors. Using the `dynamiqs` package, we performed high-performance numerical simulations on GPUs to understand the dynamics of cat qubits at both the effective Hamiltonian level and the hardware level. Through this hands-on experience, we gained insights into essential circuit QED and the potential of cat qubits to revolutionize quantum computing. In doing so, we also got to use qBraids supercomputers to run calculations for us!

## Task 1.1

In Task 1.1, we got started with the `dynamiqs` package to simulate the time-evolution of a quantum system described by a two-photon exchange Hamiltonian and a buffer drive Hamiltonian. We used the following parameters for our simulation: \( g_2 = 1.0 \), \( \epsilon_d = -4 \), and \( \kappa_b = 10 \). 

We initialized the system in a state where both the buffer and the memory were in the vacuum state. To perform the simulation, we used a Hilbert-space truncation of \( n_a = 20 \) and \( n_b = 5 \), representing the number of Fock states in modes \( a \) and \( b \), respectively. We simulated the dynamics of the system over a time period \( T = 4 \). During the simulation, we plotted the Wigner function of mode \( a \) to visualize the quantum state as it evolved over time. Also we plotted the expectation value of the number of photons and the photon number parity in the memory mode. These plots helped us understand the behavior and properties of the cat qubits under the given Hamiltonian and parameters.


$$\frac{d \hat{\rho}}{dt} = \mathcal{L}[\hat{\rho}] = -i \left[\hat{H}, \hat{\rho}\right] + \kappa_b \mathcal{D}(\hat{b})[\hat{\rho}]$$

Our system was defined by the above Linbald master equation.

## Task 1.2

In Task 1.2, we continued with the `dynamiqs` package by simulating the time-evolution of a quantum system described by a two-photon exchange Hamiltonian and a buffer drive Hamiltonian, but with a focus on different initial conditions and parameters. We used the same parameters as in Task 1.1: \( g_2 = 1.0 \), \( \epsilon_d = -4 \), and \( \kappa_b = 10 \). This time, we experimented with different initial states and Hilbert-space truncations to observe how these changes affect the dynamics of the system. We initialized the system in various states, including coherent states and superposition states, to study their evolution. We also simulated the dynamics over the same time period \( T = 4 \) and plotted the Wigner function of mode \( a \) to visualize the quantum state as it evolved. Additionally, we plotted the expectation value of the number of photons and the photon number parity in the memory mode for these different initial conditions.


## Task 1.3

In Task 1.3, we furthered our exploration with the `dynamiqs` package by simulating the time-evolution of a quantum system with a focus on the effects of different Hamiltonian parameters. We experimented with varying the coupling strength \( g_2 \), the drive amplitude \( \epsilon_d \), and the dissipation rate \( \kappa_b \) to observe how these changes influence the dynamics of the system. We initialized the system in the vacuum state and used a Hilbert-space truncation of \( n_a = 20 \) and \( n_b = 5 \). We simulated the dynamics over a time period \( T = 4 \) and analyzed the results by plotting the Wigner function of mode \( a \), the expectation value of the number of photons, and the photon number parity in the memory mode. These simulations provided valuable insights into how different Hamiltonian parameters affect the behavior and stability of cat qubits, helping us understand the robustness and potential applications of these quantum systems.

## Task 1.4

In Task 1.4, we extended our simulations using the `dynamiqs` package to explore the impact of different dissipation mechanisms on the dynamics of cat qubits. We focused on how varying the dissipation rates for both the buffer and memory modes affects the system's behavior.

We started by defining different dissipation rates for the buffer mode (\( \kappa_b \)) and the memory mode (\( \kappa_m \)). We then initialized the system in the vacuum state and used a Hilbert-space truncation of \( n_a = 20 \) and \( n_b = 5 \). We simulated the dynamics over a time period \( T = 4 \) with these varying dissipation rates. During the simulation, we analyzed the results by plotting the Wigner function of mode \( a \), the expectation value of the number of photons, and the photon number parity in the memory mode. These plots helped us understand how different dissipation mechanisms influence the stability and coherence of cat qubits, providing insights into optimizing their performance for quantum computing applications.

## Task 2.1

In Task 2.1, we advanced our exploration with the `dynamiqs` package by simulating the time-evolution of a quantum system described by a more complex Hamiltonian that includes additional interaction terms. Starting from our linbald master equation $$\frac{d \hat{\rho}}{dt} = \mathcal{L}[\hat{\rho}] = -i \left[\hat{H}, \hat{\rho}\right] + \kappa_b \mathcal{D}(\hat{b})[\hat{\rho}] +  \kappa_a \mathcal{D}(\hat{a})[\hat{\rho}]$$ We aimed to understand how these interactions influence the dynamics of cat qubits. We used the same initial parameters as in previous tasks: \( g_2 = 1.0 \), \( \epsilon_d = -4 \), and \( \kappa_b = 10 \). However, we introduced new interaction terms to the Hamiltonian to study their effects. We initialized the system in the vacuum state and used a Hilbert-space truncation of \( n_a = 20 \) and \( n_b = 5 \).

We simulated the dynamics over a time period \( T = 4 \) and analyzed the results by plotting the Wigner function of mode \( a \), the expectation value of the number of photons, and the photon number parity in the memory mode. These simulations provided deeper insights into the behavior of cat qubits under more complex interactions, helping us understand their potential for robust quantum computing applications.

Some of thew hardest parts to this challenge were figuring out how to use the `dynamiqs` package in order to simulate the evolution of the cat qubit over time. This would show to be useful in 2.2 later as we not only would simulate over time but also rotate.


## Task 2.2

In Task 2.2, we continued our exploration with the `dynamiqs` package by simulating the time-evolution of a quantum system with a focus on the effects of different initial states and varying Hamiltonian parameters. We aimed to understand how these variations influence the dynamics and stability of cat qubits. We used the same initial parameters as in previous tasks: \( g_2 = 1.0 \), \( \epsilon_d = -4 \), and \( \kappa_b = 10 \). However, we experimented with different initial states, including coherent states and superposition states, and varied the Hamiltonian parameters to observe their effects on the system's behavior.

We initialized the system in these different states and used a Hilbert-space truncation of \( n_a = 20 \) and \( n_b = 5 \). We simulated the dynamics over a time period \( T = 4 \) and analyzed the results by plotting the Wigner function of mode \( a \), the expectation value of the number of photons, and the photon number parity in the memory mode.


## Final thoughts

Through this challenge, we learned how to simulate and analyze the dynamics of cat qubits using high-performance numerical simulations, gaining valuable insights into their potential for robust quantum computing, and it was incredibly cool to see quantum mechanics in action!

Note: All evidence of working code is put on the presentation

