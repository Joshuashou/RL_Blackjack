# Optimal Blackjack Actions with Monte Carlo Reinforcement Learning Methods. 

## Table of Contents
- [Introduction](#introduction)
- [Files](#files)
- [Results](#results)

## Introduction

This is my project using Monte Carlo Reinforcement Learning methods to find the optimal State Action pairs for Blackjack. 

Currently, actions are limited to HIT and STAND, looking to add Doubling and Splitting soon. 

The algorithm simulates 10 million hands of blackjack, and uses the outcome to update state action value pairs for all states of player hand value and dealer hand value visited. The action chosen at each step is the optimal value, with an exploration probability of 10% to explore the alternative pathway. The update step size is 1/3000, 1/5000, and 1/1000. 

## Files

Environment folder contains Hand.py and game.py, which set up the Blackjack game structure and values. 

main.py runs the simulations with given step size, sample size, and exploration probability values. 

Simulations folder contains raw .npy matrices with trained state action values through different stages of iterations. 

Results contains post training state action value heat maps for visualizations. As well as optimal strategies at each state. 


## Results

Here are the results and strategies for Usable(hard) and Non Usable Ace(soft) for Exploration probability of 10% and Step size of 1/5000, as well as their actual state action values. 

<img width="400" alt="Hard Optimal State Action Pairs (0 1, 1:5000, 10M)" src="https://github.com/Joshuashou/RL_Blackjack/assets/81851383/7a8c127c-e974-4faa-885e-cc4ff88ee806">
<img width="400" alt="Soft Optimal State Action Pairs (0 1, 1:5000, 10M)" src="https://github.com/Joshuashou/RL_Blackjack/assets/81851383/c767bbfe-03f1-4409-90cc-415e23e39558">



<img width="400" alt="Hard Hit State Action Values (0 1, 1:5000, 10M)" src="https://github.com/Joshuashou/RL_Blackjack/assets/81851383/02367454-330f-44f4-a34e-c0a9e93d934b">

<img width="400" alt="Hard Stand State Action Values (0 1, 1:5000, 10M)" src="https://github.com/Joshuashou/RL_Blackjack/assets/81851383/afd3a07c-c7a5-4364-96b7-6275bb62eb50">

<img width="400" alt="Soft Hit State Action Values (0 1, 1:5000, 10M)'" src="https://github.com/Joshuashou/RL_Blackjack/assets/81851383/d005673e-2374-41f2-b033-b9671f94b2b8">

<img width="400" alt="Soft Stand State Action Values (0 1, 1:5000, 10M)" src="https://github.com/Joshuashou/RL_Blackjack/assets/81851383/737b2bcc-6a3c-4745-af2b-89d651f977ad">


