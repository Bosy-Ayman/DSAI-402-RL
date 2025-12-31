# Assignment 1 

## Reading 

- Read Chapter 1 and 2 from the supplementary book

- Read Chapter 1 from the main book

## Paper-based 

1. A financial analyst is studying a currency exchange rate that changes daily between three states: appreciating, depreciating, or stable. If the exchange rate appreciates on a given day, there is a 25% chance it will continue to appreciate the next day, a 40% chance it will stabilize, and a 35% chance it will depreciate. If the rate depreciates on a particular day, the next day it has a 30% chance to appreciate, 50% chance to depreciate again, and 20% chance to remain stable. When the rate is stable, it is equally likely to appreciate or depreciate the next day.
    - Model this scenario as a Markov chain and write the transition probability matrix

2. A city has four bus stops labeled 1, 2, 3, and 4. Passengers travel between these stops with the following probabilities:
	- From stop 1, passengers go to stop 2 with 35% probability, to stop 3 with 40%, and remain at stop 1 with 25%.
	- From stop 2, 55% travel to stop 1, and 45% go to stop 4.
	- From stop 3, 20% go to stop 2, 60% stay at stop 3, and 20% go to stop 4.
	- From stop 4, 30% travel to stop 1, 30% to stop 2, 20% to stop 3, and 20% remain at stop 4.

    - Perform the following tasks
        - Write the transition matrix T
        - What is the probability that a passenger currently at stop 3 will travel to stop 4 next?
    	- What is the probability that a passenger currently at stop 3 will reach stop 4 after two stops?
    	- What is the probability that a passenger currently at stop 3 will stay at stop 3 and not travel to any other stop next?


## Implementation 

- Define a transition probability matrix 
- Start from a chosen initial state, simulate the Markov chain for a large number of transitions 
- Record the state at each step of the simulation
- Use the library [networkx](https://networkx.org/) to plot the transition matrix as a graph 
