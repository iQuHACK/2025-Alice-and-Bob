---
tags:
  - Tidbit
Author: 
Link:
  - "[[Challenge]]"
type: 
date: 2025-02-01
---
# Overview


# Notes

## Problem 1

### 1.2 Tasks
![](../../../../../Supplemental%20Files/images/Pasted%20image%2020250201225004.png)
Above is a graph of the fidelity over time with the original $k_{B}$.


## Problem 2
We need to calc the below hamiltonian
$$
\begin{aligned}
\hat{H} &= \hat{H}_0 + \hat{H}_{\mathrm{ATS}} + \hat{H}_d,\qquad \begin{cases}
\hat{H}_0 &= \omega_{a,0}\hat{a}^\dagger \hat{a} + \omega_{b,0} \hat{b}^\dagger \hat{b}\\
\hat{H}_{ATS} &= -2 E_J \sin(\epsilon(t)) \sin(\hat{\varphi}) +2 \Delta E_J \cos(\epsilon(t)) \cos(\hat{\varphi}),\\
\hat{H}_d &= 2 \epsilon_d \cos(\omega_d t) \left(\hat{b} + \hat{b}^\dagger\right).
\end{cases}
\end{aligned}
$$
There are two big things I can do here to save on computational complexity. 
1. First, I can calculate the values of $\epsilon(t)\forall t\in\left[ 0,T+\frac{\pi}{2} \right]$. I use it twice so that is reduced. Cosine and sin are related by just a phase shift, so I only need to calculate cosine (crop the end), then crop the beginning for sin.

2. We have sines and cosines for operators, so it seems a good idea to use taylor and approximate it to $n$. In that case, we could make a graph of the accuracy of taylor as a function of $n$ for our current state.


Single photon loss is modeled by the annihilation operator
De-phasing is modeled by the number operator.
