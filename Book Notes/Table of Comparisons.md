
| Parameter         | Symbol | Scope / Algorithm | Range / Default | Description                                                                                                                                   |
| ----------------- | ------ | ----------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Discount Factor   | γ      | Global            | 0.1 – 0.99      | Determines the importance of future rewards. Higher values (e.g. 0.99) encourage long-term planning; lower values focus on immediate rewards. |
| Training Episodes | N      | Model-Free        | 100 – 50,000    | Total number of episodes the agent interacts with the environment to learn a policy.                                                          |
| Learning Rate     | α      | TD / Q-Learning   | 0.01 – 1.0      | Controls how much new information overrides old information. α = 0 means no learning; α = 1 uses only the latest information.                 |
| Epsilon           | ε      | ε-Greedy          | 0.0 – 1.0       | Controls exploration vs. exploitation. Probability of taking a random action to explore new states.                                           |
| Convergence Theta | θ      | Model-Based (DP)  | 1e-6 (default)  | Stopping threshold for Value / Policy Iteration. Training stops when ΔV < θ.                                                                  |

