### 1. The Core Problem: Scaling Up to High Dimensions

**Classical Q-Learning (Lecture 9 Recap):**

- **Mechanism:** Uses a **Q-Table** (Lookup Table) to explicitly store values for every unique state-action pair $(s,a)$.
    
- **The Limitation (The Curse of Dimensionality):** While effective for small grid worlds, tabular methods fail in high-dimensional environments. For example, a simple Atari game screen ($84 \times 84$ pixels) generates a state space larger than the number of atoms in the observable universe. Storing a table of this magnitude is computationally impossible.
    

**The DQN Solution:**

- **Function Approximation:** Instead of memorizing values, we use a **Neural Network** to _approximate_ the Q-function. The network learns to generalize from seen states to unseen ones by identifying underlying features (e.g., "enemy on left" vs. specific pixel values).
    
- **Input:** The raw state $S$ (typically a stack of 4 consecutive image frames to capture motion/velocity).
    
- **Output:** A vector of Q-values, one for each possible action (e.g., Left, Right, Fire).
    
- **Goal:** Optimize the network weights $\theta$ to minimize the error between the predicted Q-value and the optimal Q-value: $Q(s,a;\theta) \approx Q^*(s,a)$.
    

### 2. The Stability Challenge

Naive implementations of Q-Learning with Deep Neural Networks are notoriously unstable. This instability arises from fundamental differences between Reinforcement Learning and Supervised Learning:

|Problem|Cause|Solution|
|---|---|---|
|**Moving Targets (Non-Stationarity)**|In Supervised Learning, the target labels are fixed. In RL, the target depends on the network's own weights ($y \approx Q(s', a'; \theta)$). When we update $\theta$ to improve the prediction for $s_t$, we effectively change the target for $s_{t+1}$ simultaneously. This creates a feedback loop where the network chases a constantly shifting target, leading to oscillation or divergence.|**Target Network**|
|**Correlated Data (Violation of i.i.d.)**|Deep Learning assumes data samples are Independent and Identically Distributed (i.i.d.). In RL, sequential frames are highly correlated (state $s_{t+1}$ is very similar to $s_t$). Training on consecutive samples causes the network to "overfit" to the current trajectory and forget earlier experiences, leading to catastrophic forgetting.|**Experience Replay**|

### 3. Key Components of DQN

#### A. Experience Replay (The Memory Bank)

- **Mechanism:** The agent maintains a **Replay Memory** $D$ (a circular buffer) with a capacity of $N$ transitions. It stores raw experiences: $(s_t, a_t, r_{t+1}, s_{t+1})$.
    
- **Training Process:** Instead of training on the latest experience immediately, the network samples a **random mini-batch** (e.g., 32 or 64 transitions) from $D$.
    
- **Benefit:**
    
    1. **Decorrelation:** Random sampling breaks the temporal correlation between consecutive steps, restoring the i.i.d. property required for stable gradient descent.
        
    2. **Data Efficiency:** Each experience can be reused multiple times for weight updates, rather than being discarded immediately after one use.
        

#### B. Target Network (The Stable Anchor)

- **Policy Network (**$Q$ **with weights** $\theta$**):** The "active" network. It is used to select actions during gameplay and predict $Q(s, a)$ during training. Its weights are updated at every training step.
    
- **Target Network (**$\hat{Q}$ **with weights** $\theta^-$**):** A "frozen" clone of the policy network. It is used **exclusively** to calculate the target value $y_t$. It provides a fixed horizon for the policy network to learn against.
    
- **Sync Mechanism:** The weights $\theta^-$ are not learned via gradient descent. Instead, they are periodically hard-copied from the policy network ($\theta^- \leftarrow \theta$) every $C$ steps (e.g., every 1,000 or 10,000 steps).
    

### 4. Mathematical Formulation

**The Loss Function (Mean Squared Error):**

We treat this as a regression problem where we minimize the squared difference between our target and our prediction:

$$L(\theta) = \mathbb{E}_{(s,a,r,s') \sim U(D)} \left[ (y_t - Q(s_t, a_t; \theta))^2 \right]$$

**The Target Value (**$y_t$**):**

Derived from the Bellman Equation, the target is the immediate reward plus the discounted estimated value of the next state:

$$y_t = r_{t+1} + \gamma \max_{a'} \hat{Q}(s_{t+1}, a'; \theta^-)$$

- **Crucial Detail:** The max operator selects the best action for the next state, but its value is computed using the **Target Network** parameters $\theta^-$. This prevents the "chasing your own tail" instability.
    
- **Terminal States:** If $s_{t+1}$ is a terminal state (game over), then $y_t = r_{t+1}$.
    
![[Pasted image 20260116012148.png]]
### 5. Numerical Example (Exam Prep)

**Scenario:** An agent is learning to navigate a grid world with hazards.

- **Discount Factor (**$\gamma$**):** $0.9$ (Values future rewards highly).
    
- **Transition Detail:**
    
    - **State** $S_{current}$**:** "Edge of Cliff"
        
    - **Action** $A$**:** "Jump"
        
    - **Reward** $R$**:** $+2$ (Small positive reward for clearing a gap)
        
    - **State** $S_{next}$**:** "Safe Platform"
        

**Step 1: Get Current Prediction (Policy Network** $\theta$**)**

- We query the active network for the Q-value of jumping from the cliff.
    
- **Prediction:** $Q(S_{current}, \text{Jump}; \theta) = 4.5$
    

**Step 2: Get Future Value (Target Network** $\theta^-$**)**

- We query the frozen network for the value of the _next_ state ("Safe Platform").
    
- **Outputs:**
    
    - $Q(S_{next}, \text{Wait}; \theta^-) = 3.0$
        
    - $Q(S_{next}, \text{Move Forward}; \theta^-) = 6.0$ (Max value)
        
- **Max Future Q:** $6.0$
    

**Step 3: Calculate Target (**$y$**)**

This represents the "true" value we want the network to learn.

$$y = R + \gamma \times \text{MaxFutureQ}$$$$y = 2 + (0.9 \times 6.0)$$$$y = 2 + 5.4 = \mathbf{7.4}$$

**Step 4: Calculate Loss (TD Error)**

$$\text{Loss} = (y - \text{Prediction})^2$$$$\text{Loss} = (7.4 - 4.5)^2 = (2.9)^2 = \mathbf{8.41}$$

- **Interpretation:** The network predicted 4.5, but the actual return (based on the Bellman update) is 7.4. The positive error (+2.9) means the network underestimated the value.
    
- **Update:** Backpropagation will adjust the weights $\theta$ to increase the output for $(S_{current}, \text{Jump})$ next time, reducing this error.
    

### 6. Full Algorithm Summary

1. **Initialization:**
    
    - Initialize Replay Memory $D$ with capacity $N$.
        
    - Initialize Policy Network $\theta$ with random weights.
        
    - Initialize Target Network $\theta^-$ by copying weights: $\theta^- \leftarrow \theta$.
        
2. **Training Loop (Episode 1 to** $M$**):**
    
    - **Action Selection:** With probability $\epsilon$, choose a random action $a_t$ (exploration); otherwise select $a_t = \text{argmax}_a Q(s_t, a; \theta)$ (exploitation).
        
    - **Interaction:** Execute $a_t$ in the emulator, observe reward $r_t$ and image $x_{t+1}$ (preprocess to $s_{t+1}$).
        
    - **Storage:** Store transition $(s_t, a_t, r_t, s_{t+1})$ in $D$.
        
    - **Sampling:** Sample a random mini-batch of transitions from $D$.
        
    - **Target Calculation:** For each transition in the batch:
        
        - If terminal: $y_j = r_j$
            
        - Else: $y_j = r_j + \gamma \max_{a'} \hat{Q}(s_{j+1}, a'; \theta^-)$
            
    - **Optimization:** Perform a Gradient Descent step on $(y_j - Q(s_j, a_j; \theta))^2$.
        
    - **Sync:** Every $C$ steps, reset $\theta^- = \theta$.