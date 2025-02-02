import dynamiqs as dq
import jax
import jax.numpy as jnp # the JAX version of numpy
from matplotlib import pyplot as plt
# parameters
na = 20  # number of Fock states for a
nb = 5  # number of Fock states for b
T = 4  # length of the simulation
omega = jnp.pi/T  # frequency of the oscillator
eps = -4 # coupling strength
Kb = 10 # kappa in the paper
numTimes = 1000
t_save = jnp.linspace(0, 4, numTimes)  # or your actual t_save array

# annihilation operators
a, b = dq.destroy(na, nb)
# dims of above are na*nb
g2 = 1 # coupling strength

Ib = dq.eye(nb)

psi0 = dq.fock((na,nb), (0,0))  # vacuum state
a_tensored = a
adag_tensored = dq.dag(a)
b_tensored = b
bdag_tensored = dq.dag(b)
psi0a = dq.coherent(na, 0)  # vacuum state for mode a
psi0b = dq.coherent(nb, 0)  # vacuum state for mode b
psi0 = dq.tensor(psi0a, psi0b)