
### 1. The Mathematical Foundation

At the heart of Monte Carlo is the **Law of Large Numbers**: if you observe an event enough times, the average of your observations will converge to the true expected value.

#### A. The Return ($G_t$)

The goal of the agent is to maximize the expected cumulative reward. We call the total discounted reward from time step $t$ onwards the **Return**, denoted as $G_t$.

$$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots + \gamma^{T-1} R_T$$

- $R$: Immediate reward received at a step.
    
- $\gamma$ (Gamma): Discount factor ($0 \le \gamma \le 1$). It makes immediate rewards more valuable than distant ones.
    
- $T$: The final time step of the episode.
    

#### B. The Value Function ($Q$)

We want to know the "value" of taking a specific action $a$ in a specific state $s$. This is the **Action-Value Function**, $Q(s, a)$.

Mathematically, $Q(s, a)$ is the **expected return** starting from state $s$, taking action $a$, and following policy $\pi$ thereafter:

$$Q_{\pi}(s, a) = \mathbb{E}_{\pi}[G_t \mid S_t = s, A_t = a]$$

#### C. The Update Rule

Since we cannot calculate the true expectation $\mathbb{E}$ (which would require knowing the future probabilities perfectly), we approximate it by averaging the returns we have actually seen.

$$Q(s, a) \approx \frac{\text{Sum of Returns observed for } (s,a)}{\text{Number of times } (s,a) \text{ was visited}}$$

In code, this is often just `mean(returns_list)`.

---

### 2. The Algorithm: The "Back-Propagation" Logic

The algorithm works in a loop unlike standard programming. It generates data forward, but learns backward.

1. **Generate:** Play a full game (Episode) from Start to Finish using the current policy (usually $\epsilon$-greedy).
    
2. **Calculate $G$:** Once the game ends, start from the last step and walk backwards.
    
    - The reward at the very end is just $R_T$.
        
    - The reward one step before that is $R_{T-1} + \gamma R_T$.
        
3. **Update:** Store these calculated returns in a list for every state-action pair visited.
    
4. **Improve:** Update the policy (choose the action with the highest average return).
    

---

### 3. Connecting Math to Code

Here is a simplified, annotated Python implementation. I have removed the environment setup to focus purely on the **Monte Carlo logic** and how it maps to the math above.

Python

```python
import numpy as np

# 1. The Setup (Variables needed for the math)
gamma = 0.9  # The discount factor in the G_t equation
returns_sum = defaultdict(float)
returns_count = defaultdict(float)
Q = defaultdict(lambda: np.zeros(len(actions)))

def monte_carlo_update(episode):
    # episode is a list of tuples: [(state, action, reward), ...]
    
    # Initialize G (The Return) to 0 before looping back
    G = 0 
    
    # We need to track visited pairs to implement "First-Visit" logic
    # Math: We only average the return of the *first* time we saw state 's' in this episode
    visited_in_episode = set()
    
    # Loop Backwards: from T-1 down to 0
    # This efficiently calculates G_t = R_{t+1} + gamma * G_{t+1}
    for t in range(len(episode) - 1, -1, -1):
        state, action, reward = episode[t]
        state_action = (state, action)
        
        # MATH: The Recursive Definition of Return
        # G_t = R_{t+1} + gamma * G_{t+1}
        G = reward + gamma * G
        
        # Check for First-Visit
        # We look ahead in the episode to see if this (s,a) appeared previously
        # (A simpler way is to check if it appears in the slice episode[:t])
        first_visit = True
        for i in range(t):
            if episode[i][0] == state and episode[i][1] == action:
                first_visit = False
                break
        
        if first_visit:
            # MATH: Update the average
            # We are incrementally updating the mean here to avoid storing infinite lists
            returns_sum[state_action] += G
            returns_count[state_action] += 1
            
            # Q(s,a) = Sum(G) / Count(s,a)
            Q[state][action] = returns_sum[state_action] / returns_count[state_action]

```

### 4. Direct Translation Table

|**Concept**|**Math Notation**|**Code Implementation**|
|---|---|---|
|**Return**|$G_t = R_{t+1} + \gamma G_{t+1}$|`G = reward + gamma * G`|
|**Value Est.**|$Q(s,a) \approx \text{avg}(G)$|`returns_sum[...] / returns_count[...]`|
|**Policy**|$\pi(s) = \text{argmax}_a Q(s,a)$|`best_action = np.argmax(Q[state])`|
|**Exploration**|$\epsilon$-greedy|`if random() < epsilon: random_action`|

### 5. Why "First-Visit"? (A Technical Nuance)

You will often see "First-Visit MC" vs "Every-Visit MC".

- **Problem:** If the agent runs in a circle—State A $\to$ State B $\to$ State A—in a single episode, it visits State A twice.
    
- **The Math:** Ideally, we want our samples of $G$ to be independent and identically distributed (I.I.D) to satisfy the Law of Large Numbers correctly.
    
- **The Code:**
    
    - **First-Visit:** Only counts the return from the _first_ time A was visited. (Unbiased, theoretical standard).
        
    - **Every-Visit:** Counts the return for _both_ visits. (Slightly biased initially, but converges to the same result and is often easier to code).
        

### Summary of Pros & Cons

- **Pro:** It is **unbiased**. It learns the true value directly from experience without bootstrapping (making estimates based on other estimates).
    
- **Con:** It has **high variance**. One lucky episode can give a high reward, and one unlucky one can give a low reward. It takes many episodes (thousands) for the average to settle down.
