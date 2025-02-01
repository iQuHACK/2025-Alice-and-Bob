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

In addition, we also had some dimensionality issues that we resolved first using tensor products. We then found out in-build ```dynamiqs``` functionality that allowed us to directly address the problem. 

Finally, on plotting, we saw a convoluted plot, which allowed us to realize (after also looking through the discord channel) that we were plotting multiple modes conjoined. We used ```dynamiqs.ptrace``` to isolate the mode of interest and plot it individually.

## Task 1.2

