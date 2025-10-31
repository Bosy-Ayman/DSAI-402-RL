### What is Dynamic Programming (DP)?

Dynamic Programming is a collection of algorithms that can find the **perfect optimal policy ($\pi^*$)** for a given problem.

However, DP has one major requirement: you must already have a **perfect model of the environment**. This means you must know the complete dynamics ($p(s', r \mid s, a)$) for every state, action, and outcome.

### Why is DP Important for Reinforcement Learning?

In real-world Reinforcement Learning, we _almost never_ have a perfect model. So, why study DP?

Because DP is the **theoretical foundation for all of reinforcement learning**. Every other method we will learn (like Monte Carlo, TD Learning) is an _approximation_ of DP that tries to achieve the same results _without_ a perfect model and with _less_ computation.

The core idea of DP is to turn the **Bellman equations** (which define optimality) into **update rules** that allow us to iteratively compute the optimal value functions.

---

## I. The Two Core Processes of DP

All DP algorithms are built by combining two basic processes:

1. **Policy Evaluation:** Finding the value of a policy.
    
2. **Policy Improvement:** Using that value to create a better policy.
    

### 1. Policy Evaluation (The "Prediction" Problem)

- **Goal:** To answer the question: "If I follow a specific policy $\pi$, what is the long-term value $v_{\pi}(s)$ for every state $s$?"
    
- **Algorithm:** **Iterative Policy Evaluation**.
    
- **How it works:**
    
    1. Start with a random guess for the value of all states ($v_0$).
        
    2. Repeatedly sweep through every state in the state space.
        
    3. In each sweep, update the value of each state $s$ using the Bellman equation as an update rule:
        
        $$v_{k+1}(s) \leftarrow \sum_{a} \pi(a \mid s) \sum_{s', r} p(s', r \mid s, a) \left[ r + \gamma v_k(s') \right]$$
        
    4. **In simple terms:** The "new value" of a state is the _average_ (weighted by your policy $\pi$) of the (immediate reward + the discounted "old value" of the next state).
        
    5. Repeat this process until the value function $v_k$ stops changing. It will converge to the true $v_{\pi}$.
    ![[Pasted image 20251027001257.png]]

### 2. Policy Improvement

- **Goal:** Now that we have the true value $v_{\pi}$ for our policy, how can we find a _better_ policy $\pi'$?
    
- **Method:** We act **greedily** with respect to $v_{\pi}$.
    
- **How it works:**
    
    1. For any state $s$, look one step ahead. For each possible action $a$, calculate what would happen if you took that action just once and then followed your old policy $\pi$ thereafter. This is the action-value $q_{\pi}(s, a)$:
        
        $$q_{\pi}(s, a) \leftarrow \sum_{s', r} p(s', r \mid s, a) \left[ r + \gamma v_{\pi}(s') \right]$$
        
    2. Create a new policy $\pi'$ that, in state $s$, simply chooses the action $a$ that gives the **maximum** $q_{\pi}(s, a)$.
        
    3. **Policy Improvement Theorem:** This new greedy policy $\pi'$ is **guaranteed** to be as good as, or better than, the original policy $\pi$.
        

---

## II. The Main DP Algorithms

These two processes are combined to create the main DP algorithms for _solving_ the MDP.

### 1. Policy Iteration (PI)

This algorithm follows a simple, repeating loop: **Evaluate $\rightarrow$ Improve $\rightarrow$ Evaluate $\rightarrow$ Improve...**

$$\pi_0 \xrightarrow{\text{Evaluate (E)}} v_{\pi_0} \xrightarrow{\text{Improve (I)}} \pi_1 \xrightarrow{\text{E}} v_{\pi_1} \xrightarrow{\text{I}} \pi_2 \dots \rightarrow \pi^*$$

1. **Initialization:** Start with a random policy $\pi_0$.
    
2. **Policy Evaluation (E):** Run iterative policy evaluation until $v_k$ fully converges to $v_{\pi_k}$.
    
3. **Policy Improvement (I):** Create a new, better policy $\pi_{k+1}$ by acting greedily with respect to $v_{\pi_k}$.
    
4. **Repeat:** Go back to Step 2. This process is guaranteed to find the optimal policy $\pi^*$ in a finite number of iterations.
    

- **Drawback:** The "Evaluation" step (Step 2) is a full iterative algorithm _inside_ another loop. It can be very slow.
    

### 2. Value Iteration (VI)

Value Iteration is a "shortcut" that makes the process much faster. It **truncates** the slow Policy Evaluation step to just **one single sweep**.

It combines one sweep of evaluation and one sweep of improvement into a **single, powerful update rule**:

$$v_{k+1}(s) \leftarrow \max_a \sum_{s', r} p(s', r \mid s, a) \left[ r + \gamma v_k(s') \right]$$

- **How it works:** This is just the **Bellman Optimality Equation** turned directly into an update rule.
    
- **Process:** You just sweep the state space, applying this update to every state, until the value function $v_k$ converges to $v^*$.
    
- **Result:** You get the optimal value function $v^*$ directly. You can then extract the optimal policy $\pi^*$ by acting greedily one last time.
    

---

## III. The Big Picture: GPI and Asynchronous DP

### 1. Generalized Policy Iteration (GPI)

GPI is the general _idea_ that underlies almost all reinforcement learning methods. It describes the interaction between two processes:

1. **Policy Evaluation:** Making the value function consistent with the current policy ($V \rightarrow v_{\pi}$).
    
2. **Policy Improvement:** Making the policy greedy with respect to the current value function ($\pi \rightarrow \text{greedy}(V)$).
    

These two processes **compete** (making the policy greedy can make the value function wrong) but ultimately **cooperate** to find a single, joint solution: the optimal policy $\pi^*$ and optimal value function $v^*$.

### 2. Asynchronous DP

- **Problem:** Standard DP (both PI and VI) requires **full sweeps** of the _entire_ state set. This is impossible for huge problems (like Backgammon, with $10^{20}$ states).
    
- **Solution:** **Asynchronous DP** methods update states **in any order** and do not use sweeps. They can update a single state, then another, then the first one again, using whatever values are available at that moment.
    
- **Benefit:** This allows the algorithm to **focus computation on relevant states** (e..g, states the agent actually visits) and makes it possible to run DP in real-time.
    

### 3. Efficiency vs. The Curse of Dimensionality

- DP is actually very efficient (polynomial time in states/actions), which is exponentially faster than a brute-force search of all possible policies.
    
- The _real_ problem is the **Curse of Dimensionality**: the number of _states_ itself often grows exponentially. This is a fundamental challenge of the problem, not a flaw of DP.
---

### **Gridworld Example: From DP (Model-Based) to TD (Model-Free)**

This example will walk through the core concepts of Reinforcement Learning using a simple Gridworld. We'll show how an agent learns the best path, first using **Dynamic Programming (DP)** (where the agent knows all the rules) and then using **Temporal-Difference (TD) Learning** (where the agent learns from experience).

#### **1. The Environment Setup**

We have a simple world with 4 states and 1 goal:

* **States ($S$):** {S1, S2, S3, S4}
* **Terminal State:** Goal (The episode ends)
* **Actions ($A$):** {Right, Down}
* **Transitions (Deterministic):**
    * S1 $\rightarrow$ Right $\rightarrow$ S2
    * S1 $\rightarrow$ Down $\rightarrow$ S3
    * S2 $\rightarrow$ Right $\rightarrow$ **Goal**
    * S2 $\rightarrow$ Down $\rightarrow$ S4
    * S3 $\rightarrow$ Right $\rightarrow$ S4
* **Rewards ($R$):**
    * +10 for the action S2 $\rightarrow$ **Goal**.
    * 0 for all other actions.
* **Discount Factor ($\gamma$):** $0.9$ (Future rewards are 90% as valuable as
    immediate ones).

---

#### **2. Core Definitions: V-function and Q-function**

* **State-Value Function $v_{\pi}(s)$:** "How good is it to be *in* state $s$ and follow policy $\pi$?"
    * $v_{\pi}(s) = \mathbb{E}_{\pi}[G_t \mid S_t=s]$ (The expected total future reward from state $s$)
* **Action-Value Function $q_{\pi}(s, a)$:** "How good is it to take action $a$ from state $s$ and *then* follow policy $\pi$?"
    * $q_{\pi}(s, a) = \mathbb{E}_{\pi}[G_t \mid S_t=s, A_t=a]$ (The expected total future reward from that specific action)
* **The Connection:** The value of a state is the weighted average of the Q-values for all actions you might take from that state, according to your policy.
    * $v_{\pi}(s) = \sum_a \pi(a|s) \cdot q_{\pi}(s,a)$

---

#### **3. Method 1: Policy Iteration (Model-Based DP)**

This is the process of finding the optimal policy ($\pi^*$) when you **know all the rules** (the model). It's a two-step loop:

**Step 3a: Start with a Random Policy ($\pi_0$)**

* **Policy:** The agent doesn't know what to do, so it acts randomly.
    * $\pi(\text{Right}|s) = 0.5$
    * $\pi(\text{Down}|s) = 0.5$
* **Initial Values:** We guess all state values are 0. $V(s)=0$ for all $s$.

**Step 3b: Policy Evaluation (Find the value of $\pi_0$)**

We use the Bellman expectation update to find the *true* value of this random policy.

* **Formula:** $v(s) \leftarrow \sum_a \pi(a|s) \left[ R + \gamma v(s') \right]$
* **Update S2:** (50% chance of Right, 50% chance of Down)
    * $v(S2) \leftarrow 0.5 \cdot (\text{Reward for Right} + \gamma \cdot v(\text{Goal})) + 0.5 \cdot (\text{Reward for Down} + \gamma \cdot v(S4))$
    * $v(S2) \leftarrow 0.5 \cdot (10 + 0.9 \cdot 0) + 0.5 \cdot (0 + 0.9 \cdot 0) = \mathbf{5}$
* **Update S1 (using new $v(S2)$):**
    * $v(S1) \leftarrow 0.5 \cdot (\text{Reward for Right} + \gamma \cdot v(S2)) + 0.5 \cdot (\text{Reward for Down} + \gamma \cdot v(S3))$
    * $v(S1) \leftarrow 0.5 \cdot (0 + 0.9 \cdot 5) + 0.5 \cdot (0 + 0.9 \cdot 0) = \mathbf{2.25}$
* **Final Values (after many iterations):** The values would converge to:
    * $v_{\pi_0}(S1) \approx 2.25$
    * $v_{\pi_0}(S2) \approx 5.0$
    * $v_{\pi_0}(S3) = 0$
    * $v_{\pi_0}(S4) = 0$

**Step 3c: Policy Improvement (Find a better policy, $\pi_1$)**

Now that we have the values $v_{\pi_0}$, we can improve our policy by acting greedily.

* **Method:** For each state, we calculate the Q-value for *each* action and pick the best one.
* **Calculations for S1:**
    * $q(S1, \text{Right}) = (R + \gamma \cdot v(S2)) = 0 + 0.9 \cdot 5.0 = \mathbf{4.5}$
    * $q(S1, \text{Down}) = (R + \gamma \cdot v(S3)) = 0 + 0.9 \cdot 0 = 0$
    * **Better Action:** Right (4.5 > 0)
* **Calculations for S2:**
    * $q(S2, \text{Right}) = (R + \gamma \cdot v(\text{Goal})) = 10 + 0.9 \cdot 0 = \mathbf{10}$
    * $q(S2, \text{Down})  = (R + \gamma \cdot v(S4)) = 0 + 0.9 \cdot 0 = 0
    * **Better Action:** Right (10 > 0)
* **New Policy ($\pi_1$):**
    * From S1: Go **Right**
    * From S2: Go **Right**
    * (And from S3/S4: Go Right)

This new policy $\pi_1$ is a clear improvement. Since this policy is now stable (evaluating it would give the same greedy actions), we have found the **optimal policy ($\pi^*$)**.

---

#### **4. Method 2: TD Learning (Model-Free)**

Now, let's assume the agent **does not know the rules**. It has to learn by *experiencing* the world (sampling).

* **TD(0) Update Rule:** $V(S_t) \leftarrow V(S_t) + \alpha[R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]$
* Let's use the same starting values from our Policy Evaluation: $V(S1)=2.25$ and $V(S2)=5$.
* We'll use a learning rate of $\alpha = 0.3$.

**Example: A Single Experience**

1.  Agent is in state **$S_t = S1$**.
2.  It takes action $A_t = \text{Right}$.
3.  It observes the result: **$R_{t+1} = 0$** and **$S_{t+1} = S2$**.
4.  Now, the agent performs the TD update for $V(S1)$.

* **TD Target:** (The "truth" based on this sample)
    * $R_{t+1} + \gamma V(S_{t+1}) = 0 + 0.9 \cdot 5 = \mathbf{4.5}$
* **TD Error:** (The amount of "surprise")
    * $\text{TD Target} - V(S_t) = 4.5 - 2.25 = \mathbf{2.25}$
* **Update $V(S1)$:** (Nudge the old value toward the new target)
    * $V(S1) \leftarrow V(S1) + \alpha \cdot (\text{TD Error})$
    * $V(S1) \leftarrow 2.25 + 0.3 \cdot (2.25) = 2.25 + 0.675 = \mathbf{2.925}$

**Conclusion:** The agent learned from this single experience, *without* knowing the model, and its value for S1 became more accurate (it moved from 2.25 closer to the true value of 4.5).

---

#### **5. Core Concepts: Quick Summary**

* **Model vs. Policy:**
    * **Model ($p(s'|s,a)$):** "How does the world work?" (Learned in Model-Based RL)
    * **Policy ($\pi(a|s)$):** "How should I act?" (Learned in all RL)
* **Adding a Constant to Rewards:** If you add a constant $c$ to every single reward ($R' = R + c$), the optimal policy **will not change**.
    * Why? The value of *every* state will increase by the same amount ($v' = v + \frac{c}{1-\gamma}$).
    * The *relative difference* between actions remains the same, so the greedy choice is unchanged.
* **Summary Table:**

| Method                                                                | Learns World Model? ($p$) | Learns Policy? ($\pi$) | Uses Samples?  |
| :-------------------------------------------------------------------- | :------------------------ | :--------------------- | :------------- |
| **Policy Iteration**                                                  | ✅ (Needs it)              | ✅                      | ❌ (Uses model) |
| **Value Iteration** دايمًا بفرض إنّي هاخد أفضل فعل حتى لو لسه مش واثق | ✅ (Needs it)              | ✅                      | ❌ (Uses model) |
| **TD Learning**                                                       | ❌ (Model-Free)            | ✅                      | ✅              |
| **Model-Based RL**                                                    | ✅ (Learns it)             | ✅                      | ✅              |
|                                                                       |                           |                        |                |
|                                                                       |                           |                        |                |
|                                                                       |                           |                        |                |

---

| Policy Iteration                        | Value Iteration                        |
| :-------------------------------------- | :------------------------------------- |
| واحد بيخطط الأول كويس وبعدين ياخذ قرار  | واحد بياخذ قرارات بسرعة ويتعلم من غلطه |
| Policy Evaluation ثم Policy Improvement | الاثنين معاً في نفس الوقت              |
