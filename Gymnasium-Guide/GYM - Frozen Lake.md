It’s a classic environment from **OpenAI Gym / Gymnasium**.  
The agent moves on a frozen lake made of tiles:  
some are **frozen (safe)** and some are **holes (fall = lose)**.

Goal → start at `S`, reach goal `G`, avoid holes `H`

![[Pasted image 20251031140735.png]]
## 🧩 What kind of Environment is it?

### 1️⃣ **Environment type: Stochastic**

✅ **It’s stochastic (non-deterministic).**

- Even if you choose an action (like "RIGHT"),  
    the agent **might slip** and move in another direction instead.

For example:

- Action = “RIGHT”
    
- Actual move:
    
    - 80% → RIGHT
        
    - 10% → UP
        
    - 10% → DOWN
        

That means the **same action in the same state** can lead to **different next states**.

So it’s **a stochastic environment**.

### 2️⃣ **Policy type: You choose**

The **policy** depends on your algorithm.

- If you use **deterministic policy**, it always picks one best action per state.
    
- If you use **stochastic policy** (e.g., during exploration), it picks actions randomly with certain probabilities.

So the **environment** itself is **stochastic**,  
but the **policy** can be **deterministic or stochastic** — depending on what you’re using.
### 3️⃣ **Observation & Action Spaces**

| Element          | Description                                   |
| ---------------- | --------------------------------------------- |
| **State space**  | Discrete — each tile is a state.              |
| **Action space** | Discrete — 4 actions (LEFT, DOWN, RIGHT, UP). |
| **Rewards**      | +1 when reaching the goal, 0 otherwise.       |
## 🧠 Summary

| Property     | Type                                   | Description                                         |
| ------------ | -------------------------------------- | --------------------------------------------------- |
| Environment  | **Stochastic**                         | Slippery — actions don’t always go where you expect |
| State space  | **Discrete**                           | Each tile on the grid                               |
| Action space | **Discrete**                           | 4 directions                                        |
| Policy       | **Can be deterministic or stochastic** | You decide based on the algorithm                   |
we can actually **make FrozenLake deterministic** by setting:

```python

import gymnasium as gym env = gym.make("FrozenLake-v1", is_slippery=False)
```


Then it becomes **deterministic**:

- “RIGHT” always moves right.
    
- “DOWN” always moves down.

So you can switch between:

- `is_slippery=True` → **stochastic**

- `is_slippery=False` → **deterministic**
---

### Needed Libraries:
Numpy - gymnasium 

```python
  pip install "gymnasium[toy-text]"
  pip install numpy
  pip install gymnasium

```

## Imports
```python
import numpy as np

import gymnasium as gym  

```

## Environment

```Python

env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human")

```


---
# [1] Policy Iteration

```python

class PolicyIteration:

  def __init__(self, env, discount_factor=0.9, theta=1e-6, max_iterations=1000):

    self.env = env

    self.discount_factor = discount_factor

    self.theta = theta                   # small threshold for stopping policy evaluation

    self.max_iterations = max_iterations

    self.num_states = env.observation_space.n

    self.num_actions = env.action_space.n

  

    # initialize policy and value table

    self.policy = np.zeros(self.num_states, dtype=int)  # all actions = 0 initially

    self.value_table = np.zeros(self.num_states)         # start with all zeros

  

  # 2️⃣ Policy Evaluation

  def policy_evaluation(self):

    for i in range(self.max_iterations):

      delta = 0  # check change amount to know when to stop

      for state in range(self.num_states):

        action = self.policy[state]

        value = 0

        for prob, next_state, reward, done in self.env.P[state][action]:

          value += prob * (reward + self.discount_factor * self.value_table[next_state])

        delta = max(delta, abs(self.value_table[state] - value))

        self.value_table[state] = value

      if delta < self.theta:

        break


  # 3️⃣ Policy Improvement

  def policy_improvement(self):

    policy_stable = True

    for state in range(self.num_states):

      old_action = self.policy[state]

      action_Q = np.zeros(self.num_actions)

  

      # compute Q(s,a) for each action

      for action in range(self.num_actions):

        for prob, next_state, reward, done in self.env.P[state][action]:

          action_Q[action] += prob * (reward + self.discount_factor * self.value_table[next_state])

  

      # choose best action

      best_action = np.argmax(action_Q)

      self.policy[state] = best_action

  

      if old_action != best_action:

        policy_stable = False

  

    return policy_stable

  

```



```python

  def run(self):
    iteration = 0

    while True:

      iteration += 1

      self.policy_evaluation()

      stable = self.policy_improvement()

      if stable:

        print(f"✅ Policy converged after {iteration} iterations")

        break

  

    print("\n✅ Final Value Table:")

    print(self.value_table)

    print("\n✅ Optimal Policy:")

    print(self.policy)

    return self.policy


```

# 6️⃣ Apply Policy Iteration

```python


agent = PolicyIteration(env.unwrapped, discount_factor=0.9)

optimal_policy = agent.run()


# 7️⃣ Test the learned policy


state, info = env.reset()

done = False

path = [state]

  

print("\n🎯 Following Optimal Policy:\n")

while not done:

  action = int(optimal_policy[state])

  next_state, reward, terminated, truncated, info = env.step(action)

  done = terminated or truncated

  path.append(next_state)

  env.render()

  state = next_state

  

print("\n🏁 Path of visited states:")

print(path)

```


# [2] Value Iteration


```python

class ValueIteration:

  def __init__(self, env, n_iteration, discount_factor):

    self.env = env

    self.n_iteration = n_iteration

    self.discount_factor = discount_factor

    self.num_states = env.observation_space.n

    self.num_actions = env.action_space.n

    self.value_table = np.zeros(self.num_states)

    self.optimal_policy = np.zeros(self.num_states, dtype=int)

  

  def get_optimal_value(self):

    for i in range(self.n_iteration):

      new_value_table = np.copy(self.value_table)

      for state in range(self.num_states):

        action_Q = np.zeros(self.num_actions)

        for action in range(self.num_actions):

          transitions = self.env.P[state][action]

          q_sum = 0

          for prob, next_state, reward, done in transitions:

            q_sum += prob * (reward + self.discount_factor * self.value_table[next_state])

          action_Q[action] = q_sum

        new_value_table[state] = np.max(action_Q)

      self.value_table = new_value_table

  

    print("✅ Optimal Value Table:")

    print(self.value_table)

  

  def get_optimal_policy(self):

    for state in range(self.num_states):

      action_Q = np.zeros(self.num_actions)

      for action in range(self.num_actions):

        transitions = self.env.P[state][action]

        q_sum = 0

        for prob, next_state, reward, done in transitions:

          q_sum += prob * (reward + self.discount_factor * self.value_table[next_state])

        action_Q[action] = q_sum

      self.optimal_policy[state] = np.argmax(action_Q)

  

    print("✅ Optimal Policy:")

    print(self.optimal_policy)

    return self.optimal_policy

  
```


``` python


# 5️⃣ Apply Value Iteration (unwrap env)


agent = ValueIteration(env.unwrapped, n_iteration=1000, discount_factor=0.9)

agent.get_optimal_value()

policy = agent.get_optimal_policy()

```