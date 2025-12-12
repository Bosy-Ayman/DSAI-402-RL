Here are **3 Full Exams** strictly covering **First Visit MC, Every Visit MC, Epsilon-Greedy, and TD(0)**.

Each exam includes the environment code, theory questions, and coding tasks.

-----

# 🦇 EXAM 1: The Detective (First-Visit Focus)

**Time:** 75 Minutes | **Total Marks:** 100

### Part 0: Environment Setup

*(Run this code block first. Do not modify it.)*

```python
import gymnasium as gym
import numpy as np
from collections import defaultdict

class GothamPatrolEnv(gym.Env):
    """
    A 5-step patrol route.
    [Start] [1] [2] [3] [End]
    Reward: +10 at End, -1 otherwise.
    Actions: 0=Left, 1=Right.
    """
    def __init__(self):
        self.state = 0
        self.action_space = gym.spaces.Discrete(2)
    
    def reset(self):
        self.state = 0
        return self.state
        
    def step(self, action):
        if action == 1: self.state += 1
        else: self.state = max(0, self.state - 1)
        
        done = (self.state == 4)
        reward = 10 if done else -1
        return self.state, reward, done, {}
```

### Part 1: Theory (20 Marks)

1.  **First-Visit vs. Every-Visit:** In a single episode, Batman visits state `A`, leaves, and comes back to state `A` later.
      * Which method uses *both* returns to update $V(A)$?
      * Which method ignores the second return?
2.  **TD(0):** Why is TD(0) called a "bootstrapping" method?

### Part 2: Coding (80 Marks)

**Task 1: Epsilon-Greedy (20 Marks)**
Implement the function to choose an action.

```python
def get_action_epsilon_greedy(Q, state, epsilon):
    # TODO: Generate random float.
    # If < epsilon: return random action (0 or 1)
    # Else: return index of max value in Q[state]
    pass
```

**Task 2: First-Visit Monte Carlo (30 Marks)**
Implement the logic to calculate returns for **First-Visit only**.

```python
def mc_first_visit(env, episodes=100, gamma=0.9):
    V = defaultdict(float)
    returns = defaultdict(list)
    
    for _ in range(episodes):
        episode = [] # Assume this is populated with (state, action, reward)
        # ... (Code to run episode hidden for brevity) ...
        
        # YOUR CODE HERE:
        # 1. Loop backwards through episode
        # 2. Calculate G = R + gamma * G
        # 3. If state NOT in visited list:
        #    - Add G to returns[state]
        #    - Update V[state]
        pass
    return V
```

**Task 3: TD(0) Update (30 Marks)**
Implement the TD(0) update loop.

```python
def td_zero_update(env, alpha=0.1, gamma=0.9, episodes=100):
    V = defaultdict(float)
    
    for _ in range(episodes):
        state = env.reset()
        done = False
        while not done:
            action = env.action_space.sample() # Random policy
            next_state, reward, done, _ = env.step(action)
            
            # YOUR CODE HERE:
            # 1. Calculate Target = R + gamma * V[next_state] (Handle terminal!)
            # 2. Update V[state] += alpha * (Target - V[state])
            pass
            state = next_state
    return V
```

-----

-----

# ⚔️ EXAM 2: The Strategist (Every-Visit Focus)

**Time:** 75 Minutes | **Total Marks:** 100

### Part 0: Environment Setup

*(Use the same `GothamPatrolEnv` code as Exam 1)*

### Part 1: Theory (20 Marks)

1.  **Every-Visit Bias:** Does Every-Visit Monte Carlo produce a biased estimate of $V(s)$? Explain why or why not.
2.  **Epsilon-Greedy:** What is the specific purpose of the `epsilon` parameter? What happens to the "Exploration vs Exploitation" balance if you increase epsilon from 0.1 to 0.9?

### Part 2: Coding (80 Marks)

**Task 1: Every-Visit Monte Carlo (40 Marks)**
Calculate returns for **every** time a state is visited.

```python
def mc_every_visit(env, episodes=100, gamma=0.9):
    V = defaultdict(float)
    returns = defaultdict(list)
    
    for _ in range(episodes):
        episode = [] # Assume populated
        
        # YOUR CODE HERE:
        # 1. Loop backwards
        # 2. Calculate G
        # 3. ALWAYS append G to returns[state] (Do not check if visited!)
        # 4. Update V
        pass
    return V
```

**Task 2: TD(0) Manual Trace (40 Marks)**
*(Write code to solve this specific math problem)*
Batman is at State `A`.
$V(A) = 10.0$
$V(B) = 5.0$
Move: $A \rightarrow B$, Reward: $-2$.
$\gamma = 1.0$, $\alpha = 0.5$.

Write a function that calculates and prints the **TD Error** and the **New V(A)**.

```python
def calculate_manual_td():
    V_A = 10.0
    V_B = 5.0
    Reward = -2
    gamma = 1.0
    alpha = 0.5
    
    # TODO: Calculate Target
    # TODO: Calculate TD Error
    # TODO: Calculate New V_A
    pass
```

-----

-----

# ❄️ EXAM 3: The Analyst (Comparison)

**Time:** 75 Minutes | **Total Marks:** 100

### Part 0: Environment Setup

*(Use the same `GothamPatrolEnv` code as Exam 1)*

### Part 1: Theory (20 Marks)

1.  **MC vs TD Updates:**
      * MC updates $V(s)$ towards the actual Return $G$.
      * TD(0) updates $V(s)$ towards \_\_\_\_\_\_\_\_\_? (Fill in the blank).
2.  **Convergence:** Which method (MC or TD) usually converges faster on simple tasks?

### Part 2: Coding (80 Marks)

**Task 1: Returns Calculation Logic (40 Marks)**
Write a function that takes a raw episode list and returns **two** dictionaries: one for First-Visit returns and one for Every-Visit returns.

```python
def compare_mc_logic(episode, gamma=0.9):
    """
    episode: list of (state, reward) tuples.
    Example: [(0, -1), (1, -1), (0, -1), (End, 10)]
    """
    first_visit_G = {}
    every_visit_G = defaultdict(list)
    
    G = 0
    visited = set()
    
    # YOUR CODE HERE:
    # Iterate backwards.
    # Calculate G.
    # Store G in 'every_visit_G' for the current state.
    # If state not in visited, store G in 'first_visit_G' and add to visited.
    pass
    
    return first_visit_G, every_visit_G
```

**Task 2: Full TD(0) Implementation (40 Marks)**
Combine Epsilon-Greedy and TD(0) into a single training loop.

```python
def train_td_zero(env, episodes=100, alpha=0.1, gamma=0.9, epsilon=0.1):
    V = defaultdict(float) # State values
    
    for _ in range(episodes):
        state = env.reset()
        done = False
        
        while not done:
            # 1. Implement Epsilon Greedy directly here to choose action
            # (If random < eps sample, else move Right (1))
            
            next_state, reward, done, _ = env.step(action)
            
            # 2. Implement TD(0) Update for V[state]
            
            state = next_state
            
    return V
```

-----

-----

# Instructor Solution Key

### Exam 1 Solutions

**Task 1:**

```python
if np.random.rand() < epsilon: return np.random.choice([0, 1])
else: return np.argmax(Q[state])
```

**Task 2 (First Visit):**

```python
for state, action, reward in reversed(episode):
    G = reward + gamma * G
    if state not in visited:
        visited.add(state)
        returns[state].append(G)
        V[state] = np.mean(returns[state])
```

**Task 3 (TD0):**

```python
target = reward + gamma * (0 if done else V[next_state])
V[state] += alpha * (target - V[state])
```

### Exam 2 Solutions

**Task 1 (Every Visit):**

```python
for state, action, reward in reversed(episode):
    G = reward + gamma * G
    # No "if state in visited" check!
    returns[state].append(G)
    V[state] = np.mean(returns[state])
```

**Task 2 (Trace):**

```python
Target = -2 + 1.0 * 5.0  # = 3.0
Error = 3.0 - 10.0       # = -7.0
New_V = 10.0 + 0.5 * (-7.0) # = 6.5
```

### Exam 3 Solutions

**Task 1 (Logic):**

```python
for state, reward in reversed(episode):
    G = reward + gamma * G
    every_visit_G[state].append(G) # Always add
    if state not in visited:
        first_visit_G[state] = G   # Add only if first
        visited.add(state)
```

**Task 2 (Loop):**

```python
# 1. Epsilon Greedy
if np.random.rand() < epsilon: action = env.action_space.sample()
else: action = 1 # Simple policy for 1D grid

# 2. Update
target = reward + gamma * (0 if done else V[next_state])
V[state] += alpha * (target - V[state])
```