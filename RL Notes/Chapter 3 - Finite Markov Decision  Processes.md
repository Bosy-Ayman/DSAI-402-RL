
## 🧠 I. The MDP Framework: Key Concepts

An MDP formalizes the problem of an agent learning from interaction to achieve a goal. It moves beyond simple _bandit problems_ by introducing an **associative aspect**: the agent must learn to choose different actions in different situations (states).

- **Sequential Decisions:** Actions influence not just the immediate reward but also all subsequent states and future rewards.
    
- **Delayed Reward:** The agent must handle the trade-off between immediate gains and long-term consequences.
    
- **State-Dependent Values:** Instead of just estimating the value of an action ($q^*(a)$), in an MDP, we estimate:
    
    - **State-Value $v^*(s)$:** How good is it to be in state $s$?
        
    - **Action-Value $q^*(s, a)$:** How good is it to take action $a$ in state $s$?
        
- **Finite MDP:** The sets of states ($\mathcal{S}$), actions ($\mathcal{A}$), and rewards ($\mathcal{R}$) are all **finite**.
    

---

## 🔄 II. The Agent-Environment Interface

The problem is framed as an interaction loop between two components: the **Agent** (the learner and decision-maker) and the **Environment** (everything outside the agent).

### The Interaction Cycle

This interaction occurs in a sequence of discrete time steps ($t = 0, 1, 2, \dots$).

1. **At time $t$:** The agent receives the environment's **State ($S_t$)**.
    
2. The agent selects an **Action ($A_t$)**.
    
3. **One time step later:** The environment responds with a numerical **Reward ($R_{t+1}$)** and a new **State ($S_{t+1}$)**.
    
4. This creates a **trajectory** (or sequence) of experience: $S_0, A_0, R_1, S_1, A_1, R_2, \dots$
    

### The Agent-Environment Boundary

This is a critical, abstract concept:

- The boundary is **not physical**. It's the limit of the agent's **absolute control**.
    
- The agent's motors, sensors, and even its own body are typically considered part of the **environment**.
    
- The **reward computation** is _always_ part of the environment, as it defines the goal and cannot be changed by the agent.
    

### The Markov Property

This is the fundamental assumption of an MDP:

> **The future depends only on the present.** The probability of the next state ($S_{t+1}$) and reward ($R_{t+1}$) depends _only_ on the current state ($S_t$) and action ($A_t$), not on the entire history of past states and actions.

The state $S_t$ must be a **sufficient summary of the past**. If the agent knows $S_t$, it doesn't need to know how it got there.

### The Dynamics Function ($p$)

The environment's behavior is fully defined by its dynamics function $p$:

$$p(s', r \mid s, a) \doteq \text{Pr}\{S_t=s', R_t=r \mid S_{t-1}=s, A_{t-1}=a\}$$

This function gives the probability of transitioning to state $s'$ and receiving reward $r$, given that you were in state $s$ and took action $a$.

---

## 🎯 III. Goals, Rewards, and Returns

### The Reward Hypothesis

This is the central idea of how goals are formalized in RL:

> **"That all of what we mean by goals and purposes can be well thought of as the maximization of the expected value of the cumulative sum of a received scalar signal (called reward)."**

- **What, Not How:** The reward signal must communicate **what** the agent should achieve (e.g., "win the game"), not **how** it should achieve it (e.g., "capture the opponent's queen"). A poorly designed reward (a "subgoal") can lead to unintended, suboptimal behavior.
    

### The Return ($G_t$)

The **Return ($G_t$)** is the formal definition of the cumulative future reward that the agent tries to maximize. Its formula depends on the task type.

| **Task Type**        | **Description**                                                                            | **Return Formula (Gt​)**                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| **Episodic Tasks**   | Problems that have a natural end (e.g., a game, a maze). Each end is a **terminal state**. | **Simple Sum:** $G_t = R_{t+1} + R_{t+2} + \dots + R_T$ (where $T$ is the final time step). |
| **Continuing Tasks** | Problems that go on forever (e.g., a climate control system, a long-living robot).         | **Discounted Sum:** $G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$                          |

### Discounting ($\gamma$)

- The **discount rate ($\gamma$)** is a number between 0 and 1.
    
- It defines the **present value of future rewards**. A reward received $k$ steps in the future is worth only $\gamma^{k-1}$ times what it would be worth immediately.
    
- **If $\gamma = 0$:** The agent is "myopic" and only cares about the immediate reward $R_{t+1}$.
    
- **If $\gamma \rightarrow 1$:** The agent is "farsighted" and values future rewards almost as much as immediate ones.
    
- **Key Recursive Relationship:** $G_t = R_{t+1} + \gamma G_{t+1}$. This formula is the foundation for the Bellman equations.
    

---

## 🤖 IV. Example: The Recycling Robot (MDP)

This example illustrates the components of a finite MDP.

- **Agent:** A robot collecting soda cans.
    
- **States ($\mathcal{S}$):** $\{\text{high, low}\}$ (battery level).
    
- **Actions ($\mathcal{A}$):**
    
    - $\mathcal{A}(\text{high}) = \{\text{search, wait}\}$
        
    - $\mathcal{A}(\text{low}) = \{\text{search, wait, recharge}\}$
        
- **Rewards ($\mathcal{R}$):**
    
    - $r_{\text{search}}$: Expected reward for searching.
        
    - $r_{\text{wait}}$: Expected reward for waiting.
        
    - $-3$: Penalty for battery running out (must be rescued).
        
    - $0$: For recharging.
        
- **Dynamics ($p$):** The probabilities of state transitions, e.g., $p(\text{low} \mid \text{high, search}) = 1 - \alpha$.
    

This entire system can be summarized in a table or a **transition graph**.

---

## 📜 V. Policies and Value Functions

This is how we evaluate and solve the MDP.

### Policy ($\pi$)

- A **policy ($\pi$)** is the agent's behavior.
    
- It's a mapping from states to probabilities of selecting each action: $\pi(a \mid s)$.
    

### Value Functions

Value functions estimate the expected return (how good a situation is) _if the agent follows a specific policy $\pi$_.

1. **State-Value Function ($v_{\pi}(s)$):**
    
    - **Meaning:** "What is the expected return if I start in state $s$ and follow policy $\pi$ forever?"
        
    - **Formula:** $v_{\pi}(s) \doteq \mathbb{E}_{\pi}[G_t \mid S_t=s]$
        
2. **Action-Value Function ($q_{\pi}(s, a)$):**
    
    - **Meaning:** "What is the expected return if I start in state $s$, take action $a$, and _then_ follow policy $\pi$ forever?"
        
    - **Formula:** $q_{\pi}(s, a) \doteq \mathbb{E}_{\pi}[G_t \mid S_t=s, A_t=a]$
        

### The Bellman Equation (for a policy $\pi$)

The Bellman equation provides a **recursive consistency condition** for value functions. It links the value of a state to the values of its successor states.

The Bellman equation for $v_{\pi}$ is:

$$v_{\pi}(s) = \sum_{a} \pi(a \mid s) \sum_{s', r} p(s', r \mid s, a) \left[ r + \gamma v_{\pi}(s') \right]$$

- **In simple terms:** The value of your current state ($v_{\pi}(s)$) is the _average_ (over all actions $a$ your policy might take) of the **immediate reward ($r$)** plus the **discounted value of whatever state ($s'$) you land in next**.
    

---

## 🌟 VI. Optimal Policies and Value Functions

Solving an MDP means finding the _best_ policy.

- **Optimal Policy ($\pi^*$):** A policy that achieves a higher (or equal) expected return than all other policies from all states.
    
- Optimal State-Value Function ($v^*(s)$): The maximum possible value achievable from state $s$.
    
    $$v^*(s) \doteq \max_{\pi} v_{\pi}(s)$$
    
- Optimal Action-Value Function ($q^*(s, a)$): The maximum possible value achievable by taking action $a$ in state $s$.
    
    $$q^*(s, a) \doteq \max_{\pi} q_{\pi}(s, a)$$
    

### The Bellman Optimality Equation

This is the Bellman equation for the _optimal_ value functions. It's the key to solving the MDP.

Bellman Optimality Equation for $v^*$:

$$v^*(s) = \max_{a} \sum_{s', r} p(s', r \mid s, a) \left[ r + \gamma v^*(s') \right]$$

- **The Key Difference:** Notice the **$\max_{a}$** operator. Unlike the regular Bellman equation, which averages over the policy's actions, the optimality equation states that the value of a state under an optimal policy _must_ equal the return from taking the **single best action** from that state.
    

Finding the Optimal Policy:

Once you have $v^*$ or $q^*$, finding the optimal policy is simple:

- **With $v^*$:** You must do a one-step lookahead to find the action $a$ that maximizes the term in the equation.
    
- **With $q^*$:** It's even easier. You just select the action $a$ that maximizes $q^*(s, a)$. The $q^*$ function "caches" the result of the lookahead.
    

---

## ⚠️ VII. Optimality and Approximation

In practice, it's rarely possible to _actually solve_ the Bellman Optimality Equation to find the perfect $v^*$ or $q^*$.

**Why is it so hard?**

1. **Unknown Dynamics:** You usually don't know the environment's dynamics ($p$).
    
2. **Computational Cost:** The number of states is often astronomical (e.g., $10^{170}$ in Go, $10^{20}$ in Backgammon).
    
3. **State Representation:** The Markov property might be hard to achieve perfectly.
    

**Solution: Approximation**

- **Tabular Methods:** For small problems (like the Recycling Robot), you can use tables to store $v(s)$ for every state.
    
- **Function Approximation:** For large problems, you must use a more compact representation, like a neural network, to _approximate_ the value function.
    

A key benefit of RL is that its **online nature** allows it to focus computational effort on **frequently encountered states**, making good approximations possible even in massive problems.