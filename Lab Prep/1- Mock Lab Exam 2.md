Here is a **1 Hour 15 Minute All-Coding Exam**.

**Instructions:**

- **Context:** You are building the AI for the "Bat-Computer." Batman needs to learn the optimal path through Gotham without a map (Model-Free Learning).
    
- **Setup:** The `BatmanStealthEnv` class is provided for you. You do not need to rewrite it, just use it.
    
- **Grading:** Points are awarded for correct logic, correct use of NumPy, and handling edge cases (like terminal states).
    

---

# Exam 2: Model-Free Reinforcement Learning

Duration: 75 Minutes

Total Points: 100

### Provided Code (Do Not Modify)

_Assume this code is already imported and available._

```python
import numpy as np
import gymnasium as gym
from collections import defaultdict

class BatmanStealthEnv(gym.Env):
    # A simplified 1D grid world: [Start, 0, 0, 0, Exit]
    # Actions: 0=Left, 1=Right
    # Rewards: +10 at Exit, -1 per step otherwise
    def __init__(self):
        self.size = 5
        self.state = 0
        self.action_space = gym.spaces.Discrete(2)
        
    def reset(self):
        self.state = 0
        return self.state
        
    def step(self, action):
        if action == 1: self.state += 1
        else: self.state = max(0, self.state - 1)
        
        done = (self.state == self.size - 1)
        reward = 10 if done else -1
        return self.state, reward, done, {}
```

---

### Task 1: The Simulator (Generate Episode)

**(20 Points)**

Batman needs to run simulations before he goes out. Write a function that runs **one full episode** using a given policy and returns the history of what happened.

**Requirements:**

1. Reset the environment.
    
2. Loop until `done` is True.
    
3. Record `(state, action, reward)` for every step.
    

Python

```python
def generate_episode(env, policy):
    """
    Run one episode.
    
    Parameters
    ----------
    env : gym.Env
        The environment instance.
    policy : dict
        A dictionary mapping state -> action (e.g., {0: 1, 1: 1...})
        
    Returns
    -------
    episode : list of tuples
        [(state, action, reward), (next_state, next_action, next_reward), ...]
    """
    episode = []
    state = env.reset()
    done = False
    
    # --- WRITE YOUR CODE BELOW ---
    
    
    
    
    
    
    
    
    
    
    
    # -----------------------------
    return episode
```

---

### Task 2: First-Visit Monte Carlo Prediction

**(30 Points)**

Now that we have episodes, calculate the value $V(s)$ of each state.

**Requirements:**

1. Iterate through the `episode` list **backwards** to calculate Return $G$.
    
2. Formula: $G = R_{t+1} + \gamma G_{t+1}$.
    
3. Implement **First-Visit** logic: Only add $G$ to `returns[state]` if this was the _first_ time that state appeared in the episode.
    
4. Update $V(s)$ as the mean of all returns found so far.
    

Python

```python
def mc_prediction_first_visit(env, policy, num_episodes=100, gamma=0.9):
    """
    Estimates the Value Function V(s).
    """
    returns = defaultdict(list)
    V = defaultdict(float)
    
    for i in range(num_episodes):
        # 1. Generate an episode using your function from Task 1
        episode = generate_episode(env, policy)
        
        # 2. Prepare for backward pass
        G = 0
        visited_in_this_episode = set()
        
        # --- WRITE YOUR CODE BELOW ---
        
        # Tip: Use reversed(episode)
        
        
        
        
        
        
        
        
        
        
        
        
        
        # -----------------------------
        
    return V
```

---

### Task 3: Epsilon-Greedy Action Selection

**(20 Points)**

Batman usually picks the best gadget (Exploit), but sometimes experiments (Explore). Implement the helper function for Epsilon-Greedy.

**Requirements:**

1. With probability `epsilon`, return a random action (0 or 1).
    
2. Otherwise, return the action with the highest Q-value for the current state.
    
3. If `state` is not in `Q`, default to action 0.
    

Python

```python
def epsilon_greedy(Q, state, epsilon, env):
    """
    Selects an action using Epsilon-Greedy logic.
    
    Parameters
    ----------
    Q : dict
        Q[state] is a numpy array of values for actions, e.g., np.array([0.5, 2.3])
    """
    
    # --- WRITE YOUR CODE BELOW ---
    
    
    
    
    
    
    
    
    
    # -----------------------------
```

---

### Task 4: Temporal Difference TD(0) Learning

**(30 Points)**

Waiting for the end of the episode (Monte Carlo) is too slow. Implement TD(0) to update values **step-by-step**.

**Requirements:**

1. Initialize `V` to 0.
    
2. Loop through episodes and steps.
    
3. Apply the TD Update Rule:
    
    $$V(S) \leftarrow V(S) + \alpha [R + \gamma V(S') - V(S)]$$
    
4. **Crucial:** Remember that if `done` is True, the value of the next state ($V(S')$) is effectively 0.
    


```Python
def td_zero_prediction(env, alpha=0.1, gamma=0.9, num_episodes=100):
    V = defaultdict(float)
    
    for i in range(num_episodes):
        state = env.reset()
        done = False
        
        while not done:
            # Simple random policy for this task
            action = env.action_space.sample()
            
            next_state, reward, done, _ = env.step(action)
            
            # --- WRITE YOUR CODE BELOW ---
            
            # 1. Calculate TD Target
            
            
            
            # 2. Update V[state]
            
            
            
            
            # -----------------------------
            
            state = next_state
            
    return V
```

---

---

# Solution Key (For Grading)

### Task 1 Solution

```Python
    while not done:
        action = policy.get(state, 0) # Default to 0 if not in policy
        next_state, reward, done, _ = env.step(action)
        episode.append((state, action, reward))
        state = next_state
```

### Task 2 Solution

```Python
        # Loop backwards
        for state, action, reward in reversed(episode):
            G = reward + gamma * G
            
            # Check First Visit
            if state not in visited_in_this_episode:
                visited_in_this_episode.add(state)
                returns[state].append(G)
                V[state] = np.mean(returns[state])
```

### Task 3 Solution


```Python
    if np.random.rand() < epsilon:
        return env.action_space.sample()
    else:
        if state not in Q:
            return 0
        return np.argmax(Q[state])
```

### Task 4 Solution

```Python
            # If done, next_val is 0. Else it is V[next_state]
            next_val = 0 if done else V[next_state]
            
            td_target = reward + gamma * next_val
            td_error = td_target - V[state]
            
            V[state] += alpha * td_error
```