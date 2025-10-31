
## 1️⃣ What Gym/Gymnasium is

Gym (and Gymnasium, the maintained fork) is a **toolkit for reinforcement learning (RL)**. It gives you:

- **Environments**: Simulations where an agent interacts (e.g., CartPole, FrozenLake, LunarLander).
    
- **Standard API**: Every environment works in the same way, so RL algorithms can be applied to any environment without changes.
    

The documentation shows **how to create, interact, and train agents** on environments.

---

## 2️⃣ Environment Basics (from the docs)

### Key Concepts:

1. **`Env` class**
    
    - Every environment inherits from `gym.Env`.
        
    - You must implement these functions:
        
        - `reset()`: Starts a new episode, returns initial observation.
            
        - `step(action)`: Applies an action, returns `(next_state, reward, done, truncated, info)`.
            
        - `render()`: Optional, prints or visualizes the environment.
            
2. **Spaces**
    
    - **`observation_space`**: What the agent can "see".  
        Example: `MultiDiscrete([3]*n_disks)` → each disk can be on peg 0,1,2.
        
    - **`action_space`**: What actions the agent can take.  
        Example: `Discrete(6)` → six possible moves for 3 pegs.
        

---

### Example from Documentation:

```python
import gymnasium as gym
from gymnasium import spaces

class MyEnv(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=0, high=1, shape=(1,))
    
    def reset(self):
        self.state = 0
        return self.state, {}
    
    def step(self, action):
        self.state += action
        reward = 1 if self.state >= 10 else 0
        done = self.state >= 10
        return self.state, reward, done, False, {}
```

✅ Compare with your `HanoiEnv`:

| Gym Tutorial                                                    | Your HanoiEnv                                           |
| --------------------------------------------------------------- | ------------------------------------------------------- |
| `action_space = spaces.Discrete(2)`                             | `action_space = spaces.Discrete(6)`                     |
| `observation_space = spaces.Box(...)`                           | `observation_space = spaces.MultiDiscrete([3]*n_disks)` |
| `step(action)` returns `(state, reward, done, truncated, info)` | Same signature in your `HanoiEnv`                       |
| `reset()` sets initial state                                    | `reset()` sets all disks on peg 0                       |

---

## 3️⃣ Policy Evaluation / Improvement

Gym’s docs don’t enforce **how you implement policy iteration**, but they have RL tutorials:

- **Policy Evaluation**: Compute the value of following a policy for all states.
    
- **Policy Improvement**: Choose the best action in each state to maximize expected value.
    
- They usually use **simple examples like FrozenLake**.
    

Your code does the **same idea** but applies it to Tower of Hanoi:

```python
V[s] = r + gamma * V[next_s]   # policy evaluation
best_a = argmax_a(r + gamma * V[next_s])   # policy improvement
```

This is **classic value iteration / policy iteration**, explained in the RL tutorials.

---

## 4️⃣ Documentation Structure

The official Gymnasium docs are divided into:

1. **Installation & Basics**
    
    - How to install Gymnasium and interact with environments (`reset()`, `step()`, `render()`).
        
2. **API Reference**
    
    - Details of `Env`, `Space`, `Observation`, `Action`, `Reward`.
        
3. **Creating Custom Environments**
    
    - Guides you to implement your own `Env` class.
        
    - Shows how to define `observation_space`, `action_space`, `reset()`, `step()`.
        
4. **Training RL Agents**
    
    - Tutorials for policy iteration, value iteration, Q-learning, etc.
        
    - Uses simple environments like FrozenLake to demonstrate RL concepts.
        
