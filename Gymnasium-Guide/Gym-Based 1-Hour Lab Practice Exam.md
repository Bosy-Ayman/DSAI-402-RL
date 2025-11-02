Perfect! I’ll make a **1-hour Gym-focused practice exam** with **questions and ready-to-run Python code**. It’s fully general so you can **swap in any small Gym environment** like `FrozenLake-v1`, `Taxi-v3`, or a Gridworld your professor might give. It also covers all the **concepts from your assignments**.


**Duration:** 1 hour  
**Allowed Documentation:** Gymnasium, Python, matplotlib

---

## **Question 1 – Gym Environment Basics (15 points, 10 min)**

You are given a Gym environment (e.g., `FrozenLake-v1`).

**Tasks:**

1. Print the number of **states** and **actions**.
    
2. Reset the environment and print the **initial state**.
    
3. Take **one step using a random action** and print `(next_state, reward, done, info)`.
    

---

### **Answer / Code**

```python
import gymnasium as gym

# Replace with actual env if needed
env = gym.make("FrozenLake-v1", is_slippery=False)  

# 1. Number of states and actions
print("Number of states:", env.observation_space.n)
print("Number of actions:", env.action_space.n)

# 2. Reset environment
state, info = env.reset()
print("Initial state:", state)

# 3. Take one random action
action = env.action_space.sample()
next_state, reward, done, truncated, info = env.step(action)
print("Step result:", next_state, reward, done, info)
```

---

## **Question 2 – Naive Policy Simulation (20 points, 15 min)**

Define a simple policy for the environment and **simulate 20 steps**, recording states and rewards.

**Tasks:**

1. Implement `naive_policy(state)` that always chooses action `0`.
    
2. Simulate **20 steps** and print trajectory and rewards.
    
3. Count how many times each state was visited.
    

---

### **Answer / Code**

```python
import numpy as np
from collections import Counter

# Naive policy: always pick action 0
def naive_policy(state):
    return 0

# Simulation
steps = 20
state, info = env.reset()
trajectory = []
rewards = []

for _ in range(steps):
    action = naive_policy(state)
    next_state, reward, done, truncated, info = env.step(action)
    trajectory.append(next_state)
    rewards.append(reward)
    state = next_state
    if done:
        state, info = env.reset()  # reset if episode ends

print("Trajectory:", trajectory)
print("Rewards:", rewards)

# Count state visits
state_counts = Counter(trajectory)
print("State visit counts:", state_counts)
```

---

## **Question 3 – 1-Step Policy Evaluation (20 points, 15 min)**

Compute a **1-step value function** under the naive policy with γ = 0.9.

**Tasks:**

1. Initialize `V[s] = 0` for all states.
    
2. For each state, compute:
    
    ```python
    V[s] = reward + gamma * V[next_state]
    ```
    
    using **1-step simulation**.
    

---

### **Answer / Code**

```python
gamma = 0.9
num_states = env.observation_space.n
V = np.zeros(num_states)

# One-step policy evaluation
for s in range(num_states):
    # Reset to the state s
    env.reset()
    env.env.s = s  # set internal state (works for FrozenLake)
    a = naive_policy(s)
    next_s, reward, done, truncated, info = env.step(a)
    V[s] = reward + gamma * 0  # 1-step, future V assumed 0

print("1-step Value function:", V)
```

---

## **Question 4 – Reward Modification (15 points, 10 min)**

Add a constant `c = 5` to all rewards and compare value of the start state.

---

### **Answer / Code**

```python
c = 5
V_modified = np.zeros(num_states)

for s in range(num_states):
    env.reset()
    env.env.s = s
    a = naive_policy(s)
    next_s, reward, done, truncated, info = env.step(a)
    reward += c
    V_modified[s] = reward + gamma * 0

print("Modified value function:", V_modified)
print("Original vs modified start state value:", V[0], V_modified[0])
```

---

## **Question 5 – Visualization (10 points, 10 min)**

1. Plot **state visit counts** as a bar chart.
    
2. Plot **trajectory of states** as a line plot.
    

---

### **Answer / Code**

```python
import matplotlib.pyplot as plt

# Bar chart of state visits
plt.figure(figsize=(8,4))
plt.bar(state_counts.keys(), state_counts.values(), color='skyblue')
plt.xlabel("State")
plt.ylabel("Visit Counts")
plt.title("State Visit Counts")
plt.show()

# Line plot of trajectory
plt.figure(figsize=(8,4))
plt.plot(trajectory, marker='o', color='green')
plt.xlabel("Step")
plt.ylabel("State")
plt.title("State Trajectory")
plt.show()
```

---

