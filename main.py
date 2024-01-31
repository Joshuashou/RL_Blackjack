#Runs the Blackjack Reinforcement Learning Script
import os
import numpy as np

#from Environment import Game
from Environment import game

if __name__ == "__main__":
    print("Starting Monte Carlo Blackjack Simulation !")

    epsilon = 0.1
    alphas = [1.0/1000, 1.0/3000, 1.0/5000]
    iterations = 10000000


    for alpha in alphas:
        simulation = game.Blackjack_MC(epsilon, alpha, iterations)

        simulation.run_MC()

        # Save Results To Simulations Folder
        save_string = 'Epsilon{:.2f}_Alpha{:.5f}_Iterations{}'.format(epsilon, alpha, iterations)

        np.save('Simulations/' + save_string, simulation.policy_values_at_intervals)