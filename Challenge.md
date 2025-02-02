# The Challenge

The challenge is devided into different parts.

Before takkling the challenge right away, please make sure that you have carefully read the tutorials.

> :warning: **General guidelines**:
> 1. Always check your results. Do they make sense? If in doubt, ask your peers or some of the Alice & Bob team.
> 2. Visualize your results. Use plots to visualize your results. You can check the different plotting options at [dynamiqs.org](https://www.dynamiqs.org/stable/python_api/index.html#plotting-dqplot). You are also invited to make your own plots using `matplotlib`, `holoviews`, or your preferred plotting tool.
> 3. Document what you do. In order to keep track of your progress, make sure to document your steps (also those that did not work out). This may include mathematical derivations, plots, and code.
> 4. Be curious. We invite you to explore and understand the physics better. Play with parameters and see what happens, even if it is not explicitly stated in the challenge. Document your findings, it will be reflected in the grading.
> 5. Have fun. This challenge is about learning and finding out about new things - together in a team - in a fun and casual atmosphere. If you find that you have problems for whatever reasons, feel free to reach out to us and we will find a solution.

## Grading:
The grade will be determined by the following factors:
- Code: 40%
- Documentation: 30%
- Presentation on Sunday: 10%
- Ingenuity: 20%

**Tasks:** The tasks are weighted. This gives you the insight of where to focus your work.
- Task 1: 40%
- Task 2: 60%



## How to submit your results

### Instructions

1. **Fork the repository**  
   Click the **Fork** button in GitHub to create your own copy of the challenge repository.

2. **Clone your fork**  
   ```bash
   git clone https://github.com/<your_username>/<repo_name>.git
   cd <repo_name>
   ```

3. **Create a branch**  
   ```bash
   git checkout -b submission/<group_name>
   ```

4. **Create your submission folder**  
   ```bash
   mkdir submissions/<group_name>
   ```
   Add your project files (code, documentation, etc.) into this folder.

5. **Commit and push your changes**  
   ```bash
   git add .
   git commit -m "Add initial submission"
   git push origin submission/<group_name>
   ```

6. **Create a Merge Request**  
   - Go to **Pull Requests** (or **Merge Requests**, depending on the platform) in your forked repository.
   - Choose the branch `submission/<group_name>` you just pushed.
   - Target the original challenge repository’s main branch.
   - Submit the request.

You can update your submission at any time before the deadline by committing more changes to `submission/<group_name>` and pushing again. The merge request will automatically update.

In your submission folder, please include:
   1. Code (plain `.py` files or `.ipynb` files)
   2. Documentation (could be a standalone `.pdf` file or together with a jupyter notebook `.ipynb` file) This documentation includes:
   - Briew documentation of your code: Explain non-trivial approaches.
   - Plots to support your findings.
   - Any mathematical derivations.
   - Discussion/analysis of the results.

**Presentation of your results:** On Sunday Feb. 2, you will present your results as a team. For this, please prepare a slideshow. You have 10 min per team to present your results.

## 1. Simulate the dynamics of cat qubits at the effective Hamiltonian level.

In Tutorial 1, we have introduced that we can dissipatively stabilize a cat qubit by coupling a memory mode  that will store our cat qubit to a lossy buffer mode with a specific interaction that exchanges two photons of the memory mode with one photon in the buffer mode.

For this, consider the Lindblad master equation:

$$\frac{d \hat{\rho}}{dt} = \mathcal{L}[\hat{\rho}] = -i \left[\hat{H}, \hat{\rho}\right] + \kappa_b \mathcal{D}(\hat{b})[\hat{\rho}]$$

The Hamiltonian of the system is given by
```math
\begin{aligned}
\hat{H} &= \hat{H}_{\mathrm{2ph}} + \hat{H}_d,\qquad \mathrm{with}\\
\hat{H}_{\mathrm{2ph}} &= g_2 {{}\hat{a}^\dagger}^2 \hat{b} + g_2^* \hat{a}^2 \hat{b}^\dagger,\\
\hat{H}_d &= \epsilon_d^* \hat{b} + \epsilon_d \hat{b}^\dagger.
\end{aligned}
```

Here, $\hat{H}_{\mathrm{2ph}}$ is the two-photon exchange Hamiltonian and $\hat{H}_d$ is the buffer drive Hamiltonian.

**Task 1.1: Getting started with `dynamiqs`**

Using `dynamiqs`, simulate the time-evolution of this system with the following parameters:

```math
\begin{aligned}
g_2 = 1.0, 
\epsilon_d = -4, 
\kappa_b = 10 
\end{aligned}
```

(For now, we pretend that the parameters are without dimensions)

Use an initial state $\lvert \psi_0 \rangle$ in which both the buffer and the memory are in the vacuum. Use a Hilbert-space truncation of $n_a = 20$ and $n_b = 5$ (number of Fock-states in mode a and mode b, respectively) to begin with. You can play with a different Hilbert-space truncation.

Simulate the dynamics for a time $T=4$. 

Plot the wigner function of mode a (as a GIF or as a mosaic plot).

Also plot the expectation value of the number of photons, as well as the photon number parity in the memory mode.

**Task 1.2: Comparison with eliminated buffer mode**

Compare your result from Task 1.1 to the system where the buffer mode is adiabatically eliminated, in which the dynamics of the memory mode is given by:
```math
\frac{d \hat{\rho}_a}{d t} = \kappa_2 \mathcal{D}[\hat{a}^2 - \alpha^2](\hat{\rho}_a),
```
with two-photon dissipation rate $\kappa_2 = 4|g_2|^2 / \kappa_b$ and cat amplitude $\alpha^2 = -\epsilon_d/g_2^*$.

Compute the time-evolution of the fidelity between the time-evolved states computed with the two-mode system from Task 1.1. What do you observe if you lower $\kappa_b$?

**Task 1.3: Performing a Zeno-gate**

To fully control a cat qubit, we also need to be able to perform gates.

**$Z(\theta)$-rotation**: In addition to the dissipative stabilization mechanism simulated in Task 1.1, find a Hamiltonian that performs a contiuous rotation around the $Z$-axis of the qubit, also called Zeno gate, (as a reminder: the cat states $\lvert \mathcal{C}_\alpha^ \pm \rangle$ define the logical $X$-eigenstates $\lvert\pm\rangle$). This additional Hamiltonian has the form: $\hat{H}_Z = \epsilon_Z^* \hat{O} + \epsilon_Z \hat{O}^\dagger$, where $\hat{O}$ is a bosonic operator.

**a)** Simulate the time-evolution that maps $\lvert+\rangle$ to $\lvert-\rangle$ in a time $T_Z$, where $2T_Z$ is the time it takes to make a full rotation.
The speed of rotation will depend on the strenght of the parameter $\epsilon_Z$ in the Hamiltonian $H_Z$ that generates the rotation.

**b)** Optimize parameters: In a real-world scenario, also our memory mode is subject to losses of single photons. Let $\kappa_a$ be the single-photon loss rate of mode a.

For various values of $\kappa_a$ from the interval $\kappa_a \in [0.01, 2]$ and for various values of $\epsilon_Z$, plot the parity as a function of time in the presence of $\hat{H}_Z$.

For the parameter range of $\kappa_a$ above, find the optimal times $T_Z$ for a rotation of $\theta = 0 \rightarrow \pi.$

**Task 1.4: Optimal control for state-preparation**

In Task 1.1, we assumed that the parameter $\epsilon_d$ in $\hat{H}_d$ is constant throughout the time evolution. Now, you will simulate what happens if we let $\epsilon_d$ depend on time.

We would like to answer the question: What is the optimal function of time of $\epsilon_d(t)$ to inflate a cat from the vacuum to a target value of $\alpha^2 = 4$ in a given time $T =3$?

For this, first find and define an adequate loss function.
Then, optimize over $\epsilon_d(t)$. For this, you can assume that $\hat{H}_d$ is piecewise constant. You can play with the number of bins in $\hat{H}_d$.
Plot the optimized value of $\epsilon_d(t)$ as a function of time.
What happens if you increase or decrease $T$?




## 2. Simulate the dynamics of cat qubits at the circuit level.

When simulating a quantum system at the circuit level, the system becomes a bit more complex.
In Tutorial 2, we have seen that ATS with a flux pump can be used to engineer the two-photon interaction, let's simulate this in practice:

For this, consider the Lindblad master equation:

$$\frac{d \hat{\rho}}{dt} = \mathcal{L}[\hat{\rho}] = -i \left[\hat{H}, \hat{\rho}\right] + \kappa_b \mathcal{D}(\hat{b})[\hat{\rho}] +  \kappa_a \mathcal{D}(\hat{a})[\hat{\rho}]$$

At the saddle point ($\varphi_\Sigma = \pi/2 + \epsilon(t)$, $\varphi_\Delta = \pi/2$) the Hamiltonian of the system in the lab frame is given by
```math
\begin{aligned}
\hat{H} &= \hat{H}_0 + \hat{H}_{\mathrm{ATS}} + \hat{H}_d,\qquad \mathrm{with}\\
\hat{H}_0 &= \omega_{a,0}\hat{a}^\dagger \hat{a} + \omega_{b,0} \hat{b}^\dagger \hat{b}\\ 
\hat{H}_{ATS} &= -2 E_J \sin(\epsilon(t)) \sin(\hat{\varphi}) +2 \Delta E_J \cos(\epsilon(t)) \cos(\hat{\varphi}),\\
\hat{H}_d &= 2 \epsilon_d \cos(\omega_d t) \left(\hat{b} +  \hat{b}^\dagger\right).
\end{aligned}
```

Here, $\epsilon(t) = \epsilon_p \cos(\omega_p t)$.

**Task 2.1: Lab frame simulation**

Using `dynamiqs`, simulate the time-evolution of this system with the following parameters (taken [from this paper](https://arxiv.org/abs/2307.06617)):
```math
\begin{aligned}
\omega_{a,0}/2\pi &= 5.26\; \mathrm{GHz}\\
\omega_{b,0}/2\pi &= 7.70\; \mathrm{GHz}\\
\varphi_a &= 0.06\\
\varphi_b &= 0.29\\
E_J/h &= 42.76\; \mathrm{GHz}\\
\Delta E_J / h &= 0.47\;\mathrm{GHz}\\
\omega_d/2\pi &= 7.623 \; \mathrm{GHz}\\
\omega_p/2\pi &= 2.891 \; \mathrm{GHz}\\
\epsilon_d/2\pi &= -3.815 \; \mathrm{MHz}\\
\epsilon_p &= 0.122 \; \mathrm{rad}
\end{aligned}
```

Starting from the vacuum in both modes, simulate the dynamics of this system for a time $T = X \; \mu \mathrm{s}$.
Plot the evolution of the wigner function in mode a.


**Task 2.2: Rotated-displaced frame simulation**

To compare with the system at the effective Hamiltonian level, we have to transform our circuit level system into a rotated-displaced frame.
Find the correct rotated-displaced frame for the system.

Then, simulate the time-evolution of this system with the previous parameters.

Plot again the evolution of the wigner funciton in mode a. What is different in this frame?

**Task 2.3: Comparison with effective model**
Compare the results from Task 2.2 with the effective model, indroduced in Task 1.1. Calculate the fidelity between these two models as a function of time. You can use `dq.fidelity` for this. What do you observe?

**Task 2.4. Optimal control**
In this task, you are invited to really explore what is possible and come up with your own fresh ideas. No limits here! 

Here, we want to optimize parameters again to inflate the cat as fast as possible from the vacuum to a cat, but this time on the full circuit Hamiltonian. 

What are parameters that can easiliy be changed for an existing fabricated chip?
**a)** First, optimize over one or multiple of such parameters. You can optimize the constant values and/or assume that some parameters can be time-dependent (Such as the ATS drive or buffer drive amplitudes).

Properly visualize your results.

Finally, if you could also tune parameters that are given by the circuit: Optimize over one or multiple of such parameters. Think about what might be feasible or unfeasible physically.