from Environment import Hand
import numpy as np

class Blackjack_MC():
    def __init__(self, epsilon, alpha, iterations):
        num_actions = ['S', 'H'] #Add double/splitting later. 
        player_hand_values = np.arange(12, 22)
        dealer_card_values = np.arange(2, 12)


        self.epsilon = epsilon
        self.alpha = alpha
        self.iterations = iterations

        self.policy_values = np.zeros((len(player_hand_values), len(dealer_card_values), 2, len(num_actions)))/2

        # Initialize a dictionary to store policy values at intervals
        self.policy_values_at_intervals = []

        #We want to start out our policy values to be 1/2 between standing and hitting. 


    def choose_action(self, playerVal, dealerVal, usable_ace):
        action_space = 2

        current_policy = self.policy_values[playerVal-12][dealerVal - 2][usable_ace]

        optimal_policy = np.argmax(current_policy)

        optimal_probability = 1 - self.epsilon + self.epsilon / action_space
        exploration_probability = self.epsilon / action_space

        assert (optimal_probability + exploration_probability) == 1

        # Choose action based on probabilities
        action = np.random.choice([optimal_policy, 1 - optimal_policy], p=[optimal_probability, exploration_probability])

        return action


    def update_policy(self, visited_states, payoffs):

        assert (len(visited_states) == len(payoffs))

        for i in range(len(visited_states)):
           
            undiscounted_return = sum(payoffs[i:])
            playerVal, dealerVal, usable_ace, action = visited_states[i]


            if playerVal <= 21: #Don't need to update state action for busts, trivially -1
                self.policy_values[playerVal-12][dealerVal-2][usable_ace][action] += self.alpha*(undiscounted_return - self.policy_values[playerVal-12][dealerVal-2][usable_ace][action]) 

        return
        


    def run_MC(self):

        action_space = 2 #Either Stand or Hit


        #Store values at intervals. 

        # Define the intervals
        intervals = [1, 1000, 10000, 100000] + list(range(200000, self.iterations+1, 100000))

        for i in range(self.iterations): #Repeat iterations to update state values and policy iteration. 
            visited_states = []
            payoffs = [] #Corresponds to payoffs at visited states
            playerhand = Hand.Hand(player='P')
            dealerhand = Hand.Hand(player='D')

            playerVal = playerhand.value
            dealerVal = dealerhand.value

            while playerVal < 12: #Trivially we should hit before 12
                playerhand.hit()
                playerVal = playerhand.value

            action = self.choose_action(playerVal, dealerVal, playerhand.use_ace)     

            visited_states.append([playerVal, dealerVal, playerhand.use_ace, action])#Create list of states that we go through during our process of hitting. 
            payoffs.append(0)


            isBusted = False

            while action == 1: 
                #print("stuck2")
                playerhand.hit()
                playerVal = playerhand.value
                visited_states.append([playerVal, dealerVal, playerhand.use_ace, action])

                #Check if we Bust
                if playerVal > 21:
                    payoffs.append(-1) #We use this payout for GPI to adjust our policy. 

                    #UPDATE POLICIES
                    self.update_policy(visited_states, payoffs)
                    isBusted = True
                    break
                
                else:
                    payoffs.append(0)
                
                action = self.choose_action(playerVal, dealerVal, playerhand.use_ace)
            
            if isBusted:
                continue

            #Stand
            visited_states.append([playerVal, dealerVal, playerhand.use_ace, action])

            while dealerVal < 17:
                dealerhand.hit()
                dealerVal = dealerhand.value
                
            if dealerVal > 21:
                payoffs.append(1)
            else: 
                if dealerVal > playerVal:
                    payoffs.append(-1)
                elif dealerVal == playerVal:
                    payoffs.append(0)
                else:
                    payoffs.append(1)

            #UPDATE POLICIES
            self.update_policy(visited_states, payoffs)

            # Save policy values at specified intervals
            if i in intervals:
                self.policy_values_at_intervals.append(np.copy(self.policy_values))

                    
            