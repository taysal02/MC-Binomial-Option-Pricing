# Binomial Tree Option Pricing with Monte Carlo Simulations

This project implements a Monte Carlo simulation to price options using the binomial tree model, as introduced in Chapter 2, "Probability Theory on Coin Toss Space," of *Stochastic Calculus for Finance I*. The binomial tree model is a discrete-time model used to approximate the dynamics of financial assets and to compute option prices under the no-arbitrage condition.

## Overview

The goal of this project is to simulate multiple paths of an asset's price over time using a binomial tree, where the asset's price can either move up or down at each time step based on probabilities derived from the asset's volatility and risk-free rate. These simulated paths are then used to calculate the price of European call or put options via Monte Carlo methods.

## Key Features

- **Monte Carlo Simulation**: Used to simulate multiple paths of asset prices, providing an estimate of the option's expected payoff.
- **Binomial Tree Model**: A simple but effective model for representing price movements in discrete time, widely used in financial engineering.
- **Option Pricing**: Prices European call or put options based on the simulated asset paths.
- **Visualization**: Graphs the first few simulated asset price paths for visual inspection.

## Methodology

- **Binomial Tree Dynamics**: At each time step, the asset price can either increase by a factor of \( u \) or decrease by a factor of \( d \), based on a binomial distribution. The probability of the price moving up or down is derived using the risk-free rate and volatility of the asset.

- **Monte Carlo Simulation**: The option price is estimated by simulating multiple price paths and averaging the discounted payoffs for each path.

- **Probability Theory**: The approach builds upon the fundamental probability theory used in Chapter 2 of *Stochastic Calculus for Finance I*, where each asset price evolution is treated as a series of independent coin tosses, each resulting in either an "up" or "down" movement.
