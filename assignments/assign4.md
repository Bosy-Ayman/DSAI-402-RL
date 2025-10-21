# Assignment 4

## Reading 

- Read Sections 4.1, 4.2, and 4.3 from the main book
- Compute the value function for the start state for the example in slide 8 in Lecture 4

## Implementation 

**Hanoi Tower using Gymnasium API**

- Read the Gymnasium documentation to understand how the environment, states, and actions spaces are implemented in the library

- How many states? How many actions? Implement the Hanoi tower problem using Gymnasium API

- Apply policy iteration algorithm
  - **Initialize**: Start with an arbitrary policy
  - **Policy Evaluation**: Iteratively evaluate the value function $v_\pi$ for the current policy until convergence
  - **Policy Improvement**: Update the policy by choosing the action that maximizes the expected value based on $v_\pi$
  - Repeat the evaluation and improvement until the policy stabilizes (does not change)
  
- (Bonus) Visualize the policies