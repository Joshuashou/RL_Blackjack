#Runs the Blackjack Reinforcement Learning Script
import os
import numpy as np

#from Environment import Game
from Environment import game

if __name__ == "__main__":
    print("Starting Monte Carlo Blackjack Simulation !")

    epsilon = 0.1
    alpha = 1.0/3000
    iterations = 10000000

    simulation = game.Blackjack_MC(0.1, 1.0/3000, 1000000)

    simulation.run_MC()
    

    #Save Results To Simulations Folder
    Save_String = 'Epsilon' + str(epsilon) + 'Alpha' + str(alpha) + 'Iterations' + str(iterations)

    np.save('Simulations/' + Save_String, simulation.policy_values)