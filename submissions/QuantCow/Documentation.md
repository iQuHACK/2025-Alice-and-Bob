# Preperation

We spent about an hour and a half coursing through the Tutorials offered to us, building up familiarity with the following:

- The general terminology
- Equation and variable conventions
- The ```dynamiqs``` and the ```jax``` libraries
- *Alice and Bob's* approach to accounting for bit-flipping errors
- Key Quantum Computing Concepts

# Tasks
## Task 1.1

We built basic simulations based on the tutorials, and intially encountered some issues that were attributed to markdown rendering problems on the given problem statement. 

In addition, we also had some dimensionality issues that we resolved first using tensor products. 

```python
# An Alternative (more brute-force way to define the annihilation operators while sharing dimensionality)
a = dq.tensor(dq.destroy(na), dq.eye(nb))  # Memory mode
b = dq.tensor(dq.eye(na), dq.destroy(nb))  # Buffer mode
```

We then found out in-build ```dynamiqs``` functionality that allowed us to directly address the problem. 

```python
a, b = dq.destroy(na, nb)
```

Finally, on plotting, we saw a convoluted plot, which allowed us to realize (after also looking through the discord channel) that we were plotting multiple modes conjoined. We used ```dynamiqs.ptrace``` to isolate the mode of interest and plot it individually.

We also encountered problematic default y-axis behavior by ```matplotlib.pyplot```, which we fixed using ```plt.ylim```

## Task 1.2

On initial examination, we understood this to be a single-mode approximation of the previous two-mode system. We used the same approach as before, but with a single mode, defining an effective hamiltonian of zeros, and obtaining the photon-loss operators from the given equations. We then used the ```dynamiqs``` library to calculate the *Fidelity*, simulate the system and plot the results.

## Task 1.3
