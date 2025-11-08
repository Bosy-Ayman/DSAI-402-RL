This exam focuses on:

- **Core Definitions:** Bellman equations and value functions.
    
- **Simple Calculation:** A direct application of the $v_{\pi}(s)$ formula from the lectures.
    
- **Algorithmic Understanding:** The "why" and "how" of Policy Iteration.
    
- **Conceptual Comparison:** The critical differences between Model-Based and Model-Free learning.
    
- **Numerical Tracing:** A multi-step calculation problem (Monte Carlo) taken directly from the lecture examples.

---
### Question 1: Foundational Concepts (12 Points)

1. **Markov Decision Process (MDP):** An MDP is formally defined by a 5-tuple. List and briefly describe **three** of these components.
    
2. **Accumulated Reward:** Write the recursive definition that relates the total accumulated (discounted) reward $G_t$ to the reward at the next time step, $R_{t+1}$, and the future accumulated reward $G_{t+1}$.
    
3. **Bellman Equation:** Write the full **Bellman Expectation Equation** for the state-value function $v_{\pi}(s)$, showing its relationship to the policy $\pi(a|s)$ and the transition probabilities $p(s'|s,a)$.
    

---

### Question 2: Value Function Calculation (14 Points)

Consider the **Vending Machine** example from Lecture 4.

- There is one start state, $s$.
    
- There are three actions: $A \to \text{Biscoff}$, $B \to \text{Doritos}$, $C \to \text{Galaxy}$.
    
- The rewards are: $R(A)=1$, $R(B)=2$, $R(C)=3$.
    
- The environment is deterministic, and the episode ends after one action.
    

1. **Calculate $v_{\pi}(s)$:** Assume the agent is following a stochastic policy $\pi$ defined as:
    
    - $\pi(A|s) = 0.2$
        
    - $\pi(B|s) = 0.3$
        
    - $\pi(C|s) = 0.5$
        
        Calculate the value of the start state, $v_{\pi}(s)$, under this policy. Show your work.
        
1. **Optimal Value:** What is the optimal value $v_{*}(s)$ for this state, and what is the optimal policy $\pi_{*}(a|s)$ that achieves it?
    
2. **Analysis:** In one sentence, explain why the $v_{\pi}(s)$ you calculated in part 1 is lower than the $v_{*}(s)$ from part 2.
    

---

### Question 3: Policy Iteration Algorithm (16 Points)

The Policy Iteration algorithm computes an optimal policy by performing a sequence of interleaved evaluations and improvements.

1. **The Loop:** Name the two main steps inside the loop of the `policy_iteration` function.
    
2. **Policy Evaluation:** How does the "Policy Evaluation" step work? What value function does it compute, and how does it use the Bellman equation to do so iteratively? 
    
3. **Policy Improvement:** How does the "Policy Improvement" step work? Explain what it compares (using $q_{\pi}(s,a)$ and $v_{\pi}(s)$) to determine if the policy should be changed.
    

---

### Question 4: Model-Based vs. Model-Free Learning (18 Points)

1. **Core Difference:** What is the single most important difference between Model-Based (Dynamic Programming) methods and Model-Free (Monte Carlo) methods regarding the environment? 
    
2. **DP Computation:** How does a Model-Based method like Value Iteration _compute_ the value function? What specific information (probabilities and rewards) does it use? 
    
3. **MC Estimation:** How does a Model-Free method like Monte Carlo _estimate_ the value function? What does it average to get its result? 
    
4. **Practicality:** Why are Model-Based (DP) methods often impractical for complex, real-world problems like robotics or financial markets, even if we have infinite computational power? 

---

### Question 5: Numerical Problem (Monte Carlo Prediction) (20 Points)

You are given three episodes sampled from an MDP, with $\gamma=1$.

- **Episode 1:** $S_0, 2, S_1, 5, S_0, 3, S_2, 1$
    
- **Episode 2:** $S_1, 4, S_0, 1, S_2, 3$
    
- **Episode 3:** $S_0, 4, S_0, 1, S_1, 2, S_0, 1, S_2, 2$
    

Using **First-Visit Monte Carlo Prediction**, calculate the estimated value $V(s)$ for states $S_0$, $S_1$, and $S_2$ after processing all three episodes.

Instructions:

Fill in the table below. Show the Return ($G$) calculated for the first visit to each state in that episode. Then, show the new $V(s)$ by averaging this new return with all previous returns for that state.

|**Episode**|**State**|**Return (G) (First Visit)**|**Returns List for State**|**New V(s) (Average)**|
|---|---|---|---|---|
|1|$S_0$||||
|1|$S_1$||||
|1|$S_2$||||
|2|$S_0$||||
|2|$S_1$||||
|2|$S_2$||||
|3|$S_0$||||
|3|$S_1$||||
|3|$S_2$||||

---

## 🔑 Answer Key

### Question 1: Foundational Concepts

1. **MDP Components:** (Any three of the following)
    
    - **States ($S$):** A finite set of states the agent can be in.
        
    - **Actions ($A$):** A finite set of actions the agent can take.
        
    - **Transition Matrix ($P$):** The probability $p(s'|s,a)$ of transitioning to state $s'$ after taking action $a$ in state $s$.
        
    - **Reward Function ($R$):** The reward $r(s,a,s')$ received after transitioning from $s$ to $s'$ via action $a$.
        
    - **Discount Factor ($\gamma$):** A value between 0 and 1 that determines the present value of future rewards.
        
2. **Accumulated Reward:** $G_{t}=R_{t+1}+\gamma G_{t+1}$.
    
3. Bellman Expectation Equation:
    
    $$v_{\pi}(s)=\sum_{a}\pi(a|s)\sum_{s^{\prime}}p(s^{\prime}|s,a)[r(s,a,s^{\prime})+\gamma v_{\pi}(s^{\prime})]$$
    
    

---

### Question 2: Value Function Calculation

1. Calculate $v_{\pi}(s)$: The value is the expected reward, which is the sum of (probability of each action) $\times$ (reward for that action).
    
    $$v_{\pi}(s) = \pi(A|s)R(A) + \pi(B|s)R(B) + \pi(C|s)R(C)$$
    
    $$v_{\pi}(s) = (0.2 \times 1) + (0.3 \times 2) + (0.5 \times 3)$$
    
    $$v_{\pi}(s) = 0.2 + 0.6 + 1.5 = \mathbf{2.3}$$
    
    
2. **Optimal Value:**
    
    - $v_{*}(s) = \mathbf{3}$.
        
    - $\pi_{*}(a|s)$ is the deterministic policy $\pi(C|s) = 1$ and 0 for all other actions.
        
3. **Analysis:** The value $v_{\pi}(s)=2.3$ is lower than $v_{*}(s)=3$ because the policy $\pi$ wastes probability (0.2 and 0.3) on suboptimal actions (A and B) instead of putting 100% probability on the optimal action (C).
### **Note:**

### 🧠 1. What is ( v_*(s) )?

By definition:   
v_*(s) =[G_t | S_t = s]  

That means:

> "The **maximum expected return** achievable from state (s), if we follow the **best possible policy**."

---

### ⚙️ 2. What is a “return” here?

The **return** (G_t) is the sum of rewards over time:  
[  
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \dots  
]

But in this **vending machine example**, the episode ends **after one action** — so there’s only **one reward**.

So:  
G_t = R_{t+1}  
That means the **value** of the state is just the **expected immediate reward**.

---

### 🍪 3. Why we maximize only on the reward?

Because:

- There’s **no next state**, no continuation, and no future discounted rewards.
    
- The environment ends right after one action.
    
- So the **only thing that matters** is which action gives the **highest immediate reward**.
    

Hence:  
[  
v_*(s) = \max_a R(a)  
]

---

### 🧩 4. In multi-step problems

If the environment continued for several steps (like in most RL tasks),  
then we would maximize the **expected return**, which includes **future rewards** and depends on both **rewards** and **transitions**:  
[ 
v__(s) = \max_a \Big[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) v__(s') \Big]  


But here, since it’s **only one step**, that big expression collapses to simply:  
[  
v_*(s) = \max_a R(s,a)  
]

---

✅ **In short:**  

We maximize only the reward because the episode has one step — no future rewards, no transitions — so the value of the state equals the best immediate reward possible.

---

### Question 3: Policy Iteration Algorithm

1. **The Loop:** The two steps are **Policy Evaluation** and **Policy Improvement**.
    
2. **Policy Evaluation:** This step computes the state-value function $v_{\pi}$ for the _current, fixed_ policy $\pi$.  It does this by iteratively applying the Bellman Expectation Equation as an update rule ($v_k \to v_{k+1}$) until the values converge for all states.
    
3. **Policy Improvement:** This step improves the policy by acting greedily with respect to the value function $v_{\pi}$ just calculated. For each state $s$, it calculates the action-value $q_{\pi}(s,a)$ for _all_ possible actions $a$. If it finds an action $a$ such that $q_{\pi}(s,a) > v_{\pi}(s)$, it updates the policy to choose this new, better action.
    

---

### Question 4: Model-Based vs. Model-Free Learning

1. **Core Difference:** Model-Based (DP) methods **require a full model** of the environment's transition probabilities ($p$) and reward function ($r$) 32, while Model-Free (MC) methods learn **without a model** directly from experience33.
    
2. **DP Computation:** DP methods _compute_ the value function by using the known $p(s'|s,a)$ and $r(s,a,s')$ to solve the Bellman equations, calculating the expected value by summing over all possibilities.
    
3. **MC Estimation:** MC methods _estimate_ the value function by running many sample episodes, observing the actual returns ($G_t$) that follow a state, and then **averaging these empirical returns**.
    
4. **Practicality:** Because in many real-world problems (like robotics or finance), the environment's dynamics are **unknown, highly complex, or constantly changing**, making it impractical or impossible to create an accurate model ($p$ and $r$) in advance.
    

---

### Question 5: Numerical Problem (Monte Carlo Prediction)

(Calculations based on `lec6` slides 37)

|**Episode**|**State**|**Return (G) (First Visit)**|**Returns List for State**|**New V(s) (Average)**|
|---|---|---|---|---|
|1|$S_0$|$2+5+3+1 = \mathbf{11}$|$\{11\}$|$11 / 1 = \mathbf{11.0}$|
|1|$S_1$|$5+3+1 = \mathbf{9}$|$\{9\}$|$9 / 1 = \mathbf{9.0}$|
|1|$S_2$|$\mathbf{1}$|$\{1\}$|$1 / 1 = \mathbf{1.0}$|
|2|$S_0$|$1+3 = \mathbf{4}$|$\{11, 4\}$|$(11+4) / 2 = \mathbf{7.5}$|
|2|$S_1$|$4+1+3 = \mathbf{8}$|$\{9, 8\}$|$(9+8) / 2 = \mathbf{8.5}$|
|2|$S_2$|$\mathbf{3}$|$\{1, 3\}$|$(1+3) / 2 = \mathbf{2.0}$|
|3|$S_0$|$4+1+2+1+2 = \mathbf{10}$|$\{11, 4, 10\}$|$(11+4+10) / 3 \approx \mathbf{8.33}$|
|3|$S_1$|$2+1+2 = \mathbf{5}$|$\{9, 8, 5\}$|$(9+8+5) / 3 \approx \mathbf{7.33}$|
|3|$S_2$|$\mathbf{2}$|$\{1, 3, 2\}$|$(1+3+2) / 3 = \mathbf{2.0}$|