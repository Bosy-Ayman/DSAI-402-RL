
## 1. Summary of Reading (Sutton & Barto, 4.1-4.3)

### Section 4.1: Policy Evaluation (The "Prediction" Problem)

- **Goal:** To answer the question: "If I follow a specific policy $\pi$, how good is it?"
    
- **What it does:** It computes the **state-value function (**$v_{\pi}$**)** for a _fixed_ policy.
    
- **Method:** It uses **Iterative Policy Evaluation**. This algorithm turns the Bellman _expectation_ equation into an update rule.
    
    - You start with an arbitrary value function, $v_0$ (e.g., all zeros).
        
    - You repeatedly sweep through every state $s$ and update its value based on the values of its successor states, averaged by the policy $\pi$.
        
    - **The Update Rule:** $v_{k+1}(s) \leftarrow \sum_{a} \pi(a \mid s) \sum_{s', r} p(s', r \mid s, a) \left[ r + \gamma v_k(s') \right]$
        
    - You repeat this until the value function stops changing (it converges to the true $v_{\pi}$).
        

### Section 4.2: Policy Improvement

- **Goal:** To answer the question: "Now that I know the value $v_{\pi}$ of my current policy, how can I find a _better_ policy $\pi'$?"
    
- **Method:** You act **greedily** with respect to the value function $v_{\pi}$.
    
- **How it works:**
    
    1. For any state $s$, you look one step ahead. For _every_ action $a$, you calculate its value: $q_{\pi}(s, a) = \sum_{s', r} p(s', r \mid s, a) \left[ r + \gamma v_{\pi}(s') \right]$.
        
    2. You create a new, greedy policy $\pi'$ that simply chooses the action $a$ that gives the **maximum** $q_{\pi}(s, a)$.
        
    3. **Policy Improvement Theorem:** This is the key guarantee. It proves that this new greedy policy $\pi'$ is **guaranteed** to be as good as, or better than, the original policy $\pi$.
        

### Section 4.3: Policy Iteration

- **Goal:** To find the single **optimal policy (**$\pi^*$**)**.
    
- **Method:** This algorithm simply alternates between the two previous steps until the policy is perfect and stops changing.
    
- **The Algorithm Loop (called Generalized Policy Iteration or GPI):**
    
    $\pi_0 \xrightarrow{\text{E}} v_{\pi_0} \xrightarrow{\text{I}} \pi_1 \xrightarrow{\text{E}} v_{\pi_1} \xrightarrow{\text{I}} \pi_2 \dots \rightarrow \pi^*$
    
    1. **Initialize:** Start with a random policy $\pi_0$.
        
    2. **Policy Evaluation (E):** Compute the value function $v_{\pi_k}$ for the current policy.
        
    3. **Policy Improvement (I):** Create a new, better policy $\pi_{k+1}$ by acting greedily with respect to $v_{\pi_k}$.
        
    4. **Repeat:** Go back to Step 2. If the policy did not change during the improvement step (it's "stable"), then you are finished and have found the optimal policy $\pi^*$.
        

## 2. How to Compute the Value Function (for "Slide 8")

I cannot see your lecture slide, but the problem "Compute the value function for the start state" is a **Policy Evaluation** problem (Section 4.1).

To solve this, you need to:

1. **Identify the Policy (**$\pi$**):** The slide must specify what policy the agent is following (e.g., "a random policy" means $\pi(a|s)$ is uniform for all actions).
    
2. **Identify the Dynamics (**$p, r, \gamma$**):** You need the transition probabilities ($p$), the rewards ($r$) for each transition, and the discount factor ($\gamma$).
    
3. **Set up the Bellman Equations:** Write down the Bellman expectation equation for _every_ state. You will get a system of linear equations.
    

**Example:** For a simple 2-state problem (states $s_1, s_2$) and a policy $\pi$:

- $v_{\pi}(s_1) = \sum_{a} \pi(a \mid s_1) \sum_{s', r} p(s', r \mid s_1, a) \left[ r + \gamma v_{\pi}(s') \right]$
    
- $v_{\pi}(s_2) = \sum_{a} \pi(a \mid s_2) \sum_{s', r} p(s', r \mid s_2, a) \left[ r + \gamma v_{\pi}(s') \right]$
    

You can solve this system of equations (e.g., using algebra) to find the exact values for $v_{\pi}(s_1)$ and $v_{\pi}(s_2)$. The value for the "start state" will be one of these.

## 3. Hanoi Tower using Gymnasium API

The pseudocode you provided (`env.states`, `env.transitions`) implies a tabular environment where the full model (the "rules" of the game) is known. The standard Gymnasium API (`env.step()`) is for "model-free" learning.

However, many `gymnasium` environments _do_ provide the full model in a hidden variable, often `env.P`. The `hanoi-v0` environment from `gym_hanoi` is one such example.

Let's assume a standard **3-disk, 3-peg** Hanoi problem.

- **How many states?** A state is defined by the location (which peg) of each disk. Each of the 3 disks can be on 1 of 3 pegs.
    
    - **Calculation:** $3 \times 3 \times 3 = 3^3 = \mathbf{27 \text{ states}}$
        
    - _Example state:_ `(0, 0, 0)` means all disks are on peg 0. The goal state is `(2, 2, 2)`.
        
- **How many actions?** An action is a move from one peg to another peg.
    
    - **Possible Moves:** (from 0 to 1), (from 0 to 2), (from 1 to 0), (from 1 to 2), (from 2 to 0), (from 2 to 1).
        
    - **Total:** $\mathbf{6 \text{ actions}}$
        
    - _Note:_ Most actions will be _invalid_ in a given state (e.g., trying to move a large disk onto a small one). The environment's dynamics will handle this, usually by returning the same state and a negative reward.