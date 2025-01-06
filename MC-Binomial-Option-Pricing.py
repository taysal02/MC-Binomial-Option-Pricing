#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:54:07 2025

@author: Tayyib Salawu
"""
import numpy as np
import matplotlib.pyplot as plt

def MCbinomialtree(S0, K, T, r, sigma, N, M, put_call):
    dt = T/N
    u = np.exp(sigma * np.sqrt(dt))
    d = np.exp(-sigma * np.sqrt(dt))
    p = (np.exp(dt * r) - d) / (u - d)
    
    option_price = []
    simulations = []
    for _ in range(M):
        S = np.zeros(N+1)
        S[0] = S0
        
        for i in range(1, N+1):
            cointoss = np.random.binomial(1, p)
            S[i] = S[i-1] * (u if cointoss else d)
        simulations.append(S)
        
        if put_call == 'call':
            profit = max(S[-1] - K, 0)
        elif put_call == 'put':
            profit = max(K - S[-1], 0)
            
        option_price.append(np.exp(-r * T) * profit)
        
    return np.mean(option_price), simulations

# Parameters
S0 = 100        # Initial stock price
K = 100         # Strike price
T = 1           # Time to maturity (1 year)
r = 0.05        # Risk-free rate (5%)
sigma = 0.2     # Volatility (20%)
N = 50          # Number of time steps
M = 1000        # Number of Monte Carlo simulations
put_call = 'call'  # Option type ('call' or 'put')

# Compute the option price
option_price, simulations = MCbinomialtree(S0, K, T, r, sigma, N, M, put_call)

# Print the option price
print(f"Option Price ({put_call}): {option_price:.4f}")

# Print the simulations
print("\nSimulations:")
for i, sim in enumerate(simulations):
    print(f"Simulation {i + 1}: {sim}")


plt.figure(figsize=(10, 6))
for sim in simulations:  # Plot the first 10 simulations (you can change this number)
    plt.plot(sim, lw=1)  # lw (line width) can be adjusted for better visuals

plt.title(f"Simulations of Stock Price Paths for {put_call} Option")
plt.xlabel('Time Steps')
plt.ylabel('Stock Price')
plt.grid(True)
plt.show()
