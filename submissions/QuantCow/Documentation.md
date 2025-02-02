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

We also looked at exponentially reducing Buffer Decay rates (kappa_b) and saw the fidelity decrease. We plotted this as well.


## Task 1.3
We optimized parity as a function of time for different values of epsilon_z while keeping kappa constant and then we optimized for different values of kappa while keeping epsilon_z constant. We plotted the results for both cases. Generally, we observed that the parity was more robust with higher values of kappa and lower values of epsilon_z.

As for optimizing T_z, we could not quite get our function to work, although we used dq.unit() to normalize our parity, the values were less than -1 and greater than 1 for some reason.


## Task 1.4

To find the optimal time-dependent function, \( \epsilon_d(t) \), we first defined a loss function. We designed this with the target state being when \( \alpha^2 = 4 \), so the loss function was defined as:

\[ \text{Loss} = (\langle n \rangle - 4)^2 \]

This ensures the state matches the desired cat state.

Next, we used a piecewise function for \( H_d \) with \( N \) bins for the constant \( \text{Time} = 3 \). What we should have done is also make \( \epsilon_d \) a piecewise function, as \( H_d = \epsilon_d (b + b^\dagger) \).

The next step was to use the `jax.grad` function to calculate the gradient of the loss with respect to \( \epsilon_d \).

Once this was done, we used multiple epochs and a learning rate equation to update the step and optimize \( \epsilon_d \) to minimize the loss, and then plotted the results.

## Task 2.1

This was probably one of the most difficult tasks. A large part of the confusion came from figuring out how to write our wrapper function correctly. We knew that \( H \) needed to be time-dependent, but it took a long time and some assistance from our mentors to understand that, like always, there's a convenient function for that. When we eventually figured out how to use the wrapper functions, we were having trouble running and collecting plots because of how long it initially took. We weren't sure if our code was broken, if it was possible, or if we just didn't understand something. It turns out, we were very much on the right path; we just needed to make certain computational changes to be more efficient. Finally, after hours of trying to run, we ended with a plot that was barely moving and had to again doubt if something went wrong. But after collaborating with peers, we realized we had actually figured it out.

## Task 2.2

After cracking 2.1, it felt that 2.2 just fell through in momentum. The pattern of determining the appropriate Hamiltonian, coding the math into Python, and hashing out the bugs was far more familiar. We knew what to expect -- that the qubit should look almost perfectly still -- and to test it, we increased the energies and driving frequencies to extremely high levels and compared what this looked like on the state from 2.1. We observed a very clear contrast: 2.1 was extremely sporadic and energized, while 2.2, being in the rest frame, remained perfectly still.

## Task 2.3

Finally, we needed to compare fidelities between the qubit state from Task 1.1 and this newly created "rest frame" qubit from 2.2. However, when we first went to compare fidelities, we forgot that the qubit from 1.1 was being solved over a time frame of 4 seconds, while the qubit in 2.2 was being solved over a range of about 100 ns. So, we had to compare them on equal time frames to calculate an accurate fidelity.

## Task 2.4

Although we were unable to get our optimizer to function correctly, we had created a good start.