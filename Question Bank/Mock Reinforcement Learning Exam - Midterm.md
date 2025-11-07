# Based on the older exam style

Based on the analysis of Dr. Mohamed Ghalwash's teaching style, which emphasizes **application, deep understanding, and numerical problem-solving** (as confirmed by the former student and the content of your RL lectures), I've designed a mock Reinforcement Learning exam.

This exam features **5 questions** covering the core topics: MDP fundamentals, Bellman equations, Dynamic Programming (Policy Evaluation), and Model-Free Learning (Monte Carlo).

---

## Question 1: Core Concepts & Bellman Fundamentals (12 Points)

### 1.1 Definitions and Comparisons (6 points)

Briefly explain the following points, highlighting the essential differences:

* **a. Policy $(\pi)$:** What is its formal definition and role in an MDP? 
* **b. State-Value Function $v_{\pi}(s)$ vs. Action-Value Function $q_{\pi}(s,a)$:** What does each function estimate? 
* **c. Model-Based vs. Model-Free RL:** What is the critical distinction regarding the environment's transition and reward information? 
### 1.2 Bellman Equation Analysis (6 points)

The Bellman Expectation Equation for the state-value function $v_{\pi}(s)$ is given by:

$$v_{\pi}(s)=\sum_{a}\pi(a|s)\sum_{s^{\prime}}p(s^{\prime}|s,a)[r(s,a,s^{\prime})+\gamma v_{\pi}(s^{\prime})]$$

Identify and explain the role of each of the following three components in the context of calculating $v_{\pi}(s)$:

1.  The term representing the agent's **action choice**.
2.  The term representing the **environment's reaction**
3.  The term representing the **future expected value**.

---

## Question 2: Optimal Policy and Dynamic Programming (10 Points)

### 2.1 Optimality Equations (5 points)

* **a.** Define the concept of an **Optimal Policy ($\pi^{*}$)**. 
* **b.** Write the formal mathematical expression for the **Bellman Optimality Equation** for the **Action-Value Function** $q_{*}(s,a)$.

### 2.2 Value Iteration Mechanics (5 points)

The core update in **Value Iteration** is: $v_{k+1}(s) = \max_{a} q_{\pi}(s,a)$.
Explain the fundamental principle behind Value Iteration and why this single update step is guaranteed to converge to the optimal value function $v_{*}(s)$ without needing separate, iterative policy evaluation.

---

## Question 3: Dynamic Programming - Policy Evaluation (18 Points)

Consider a small $3 \times 3$ Grid World where the task is **undiscounted ($\gamma=1$)** and the reward for every transition is $R_t = -1$. The corner states $(0,0)$ and $(2,2)$ are terminal states with $v(s)=0$.

Assume the current policy $\pi$ is the **Random Policy**: any of the possible actions (Up, Down, Left, Right) is chosen with equal probability (if an action leads outside the grid, the agent stays in the same cell).

| (0,0) Terminal | (0,1) | (0,2) |
| :---: | :---: | :---: |
| (1,0) | (1,1) | (1,2) |
| (2,0) | (2,1) | (2,2) Terminal |

**Required:**

1.  **a. Initial Value (2 points):** Write the initial value function matrix $\mathbf{v_0}$ where $v_0(s)=0$ for all states.
2.  **b. Iterative Evaluation (12 points):** Use the **Iterative Policy Evaluation** algorithm to calculate the state values $v_k(s)$ for all non-terminal states after the **first iteration ($k=1$)** and after the **second iteration ($k=2$)**. (Assume deterministic transitions: the action chosen leads directly to the intended next cell).
3.  **c. Policy Improvement (4 points):** Based on your calculated $v_2(s)$ matrix, what is the best (greedy) action to take from the state **(1,1)** to achieve immediate policy improvement?

---

## Question 4: Model-Free - Monte Carlo Prediction (16 Points)

You are using the **First-Visit Monte Carlo Prediction** method to estimate state values $V(s)$ for three states ($S_0, S_1, S_2$) with a discount factor $\gamma=1$.

The following episodes are sampled:
* **Episode 1:** $S_0, 2, S_1, 5, S_0, 3, S_2, 1$ 
* **Episode 2:** $S_1, 4, S_0, 1, S_2, 3$ 
* **Episode 3:** $S_0, 4, S_0, 1, S_1, 2, S_0, 1, S_2, 2$ 

**Required:**

1.  **a. Tracking Calculations (12 points):** Complete the table below by calculating the Return ($G$) for the **first visit** of each state and the updated value $V(s)$ after each episode.

| Episode | State | Return ($G$) (First Visit) | Returns Array Before Episode | $V(s)$ After Episode |
| :-----: | :---: | :------------------------: | :--------------------------: | :------------------: |
|    1    | $S_0$ |                            |             {0}              |                      |
|    1    | $S_1$ |                            |             {0}              |                      |
|    1    | $S_2$ |                            |             {0}              |                      |
|  **2**  | $S_0$ |                            |             {11}             |                      |
|  **2**  | $S_1$ |                            |             {9}              |                      |
|  **2**  | $S_2$ |                            |             {1}              |                      |
|  **3**  | $S_0$ |                            |           {11, 4}            |                      |
|  **3**  | $S_1$ |                            |            {9, 8}            |                      |
|  **3**  | $S_2$ |                            |            {1, 3}            |                      |

2.  **b. Action-Value Estimation (4 points):** Explain how the Monte Carlo approach is adapted to estimate the **Action-Value function $q_{\pi}(s,a)$** instead of $v_{\pi}(s)$ without a model. 

---

## Question 5: Exploration vs. Exploitation & The Greedy Problem (14 Points)

### 5.1 The Exploration-Exploitation Dilemma (5 points)

Explain the **Exploration-Exploitation dilemma** in Reinforcement Learning. Why is this challenge particularly pronounced in the Model-Free setting? 

### 5.2 Not Greedy Example Analysis (9 points)

Consider the following decision tree: 

| Path | Reward Sequence | Total Return ($\gamma=1$) |
| :---: | :---: | :---: |
| Start $\rightarrow$ S | +1 | $\mathbf{1}$ |
| Start $\rightarrow$ T $\rightarrow$ K | +3, -20 | $\mathbf{-17}$ |
| Start $\rightarrow$ H $\rightarrow$ E | +2, -15 | $\mathbf{-13}$ |

1.  **a.** If the agent is **greedy based only on the immediate reward** from the Start State, which action would it choose (S, T, or H)? (3 points)
2.  **b.** What is the **Optimal Policy** (the action from the Start State that maximizes the total return) and what is the key lesson this example teaches about making decisions in RL? (6 points)

---

## 🔑 Answer Key

## 💡 Question 1: Core Concepts & Bellman Fundamentals

### 1.1 Definitions and Comparisons

* **a. Policy $(\pi)$:** A **stochastic rule**  that maps states to the **probabilities of selecting each possible action**. It defines the agent's behavior.
* **b. State-Value Function $v_{\pi}(s)$ vs. Action-Value Function $q_{\pi}(s,a)$:**
    * $v_{\pi}(s)$ estimates the **expected return when starting in state $s$** and following policy $\pi$ thereafter.
    * $q_{\pi}(s,a)$ estimates the **expected return when performing action $a$ in state $s$** and following policy $\pi$ thereafter].
* **c. Model-Based vs. Model-Free RL:**
    * **Model-Based** methods **require knowledge** of the environment's model (transition probabilities $p(s'|s,a)$ and reward function $r(s,a,s')$) to systematically evaluate and improve a policy.
    * **Model-Free** methods learn without a model, approximating expected values by **averaging observed returns from sampled experience** (trial and error).

### 1.2 Bellman Equation Analysis

$$v_{\pi}(s)=\mathbf{\sum_{a}\pi(a|s)}\mathbf{\sum_{s^{\prime}}p(s^{\prime}|s,a)}\mathbf{[r(s,a,s^{\prime})+\gamma v_{\pi}(s^{\prime})]}$$
1.  **Agent's action choice:** $\sum_{a}\pi(a|s)$
    * **Role:** This is the outer summation over all possible actions $a$, weighted by the probability $\pi(a|s)$ that the **agent** chooses that action according to its current policy $\pi$.
2.  **Environment's reaction:** $\sum_{s^{\prime}}p(s^{\prime}|s,a)$
    * **Role:** This is the inner summation over all possible next states $s'$, weighted by the transition probability $p(s'|s,a)$, which defines the **environment's dynamics** (i.e., where the agent lands after taking action $a$).
3.  **Future expected value:** $\gamma v_{\pi}(s^{\prime})$
    * **Role:** This represents the discounted value of the resulting next state $s'$. It incorporates the **long-term perspective** into the current state's value, embodying the definition of accumulated (discounted) reward.

---

## 💡 Question 2: Optimal Policy and Dynamic Programming

### 2.1 Optimality Equations

* **a. Optimal Policy ($\pi^{*}$):** A policy $\pi^{\prime}$ is defined to be better than or equal to a policy $\pi$ if its expected return is greater than or equal to that of $\pi$ for all states. The optimal policy $\pi^{*}$ is the one that is better than or equal to all other policies.
* **b. Bellman Optimality Equation for $q_{*}(s,a)$:**
    $$q_{*}(s,a) = \sum_{s^{\prime}} p(s^{\prime}|s,a) [r(s,a,s^{\prime}) + \gamma \max_{a^{\prime}} q_{*}(s^{\prime}, a^{\prime})]$$

### 2.2 Value Iteration Mechanics

* **Principle:** Value Iteration solves for the optimal value function $v_{*}(s)$ by iteratively applying the Bellman Optimality Update (the $\max_{a}$ operator).
* **Why it converges quickly:** It combines the two separate stages of Policy Iteration (Policy Evaluation and Policy Improvement) ==into a single step==. By taking the $\max_{a}$ at every step, it is performing an ==implicit policy improvement,== allowing it to converge directly to the optimal value function $v_{*}(s)$ much faster than Policy Iteration, which might require many sweeps of evaluation before a single improvement. 

---

## 💡 Question 3: Dynamic Programming - Policy Evaluation

**Given:** $\gamma=1$, $R_t = -1$, $\pi(a|s)=0.25$ (Random Policy).

### 3.1 Initial Value ($k=0$)

$$\mathbf{v_0} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

### 3.2 Iterative Evaluation

The update equation is $v_{k+1}(s) = \sum_{a} \pi(a|s) [R + \gamma v_k(s^{\prime}_{a})] = 0.25 \sum_{a \in \{N,S,E,W\}} [-1 + v_{k}(s^{\prime}_{a})]$.

#### Iteration 1 ($k=1$):

Since $v_0(s')=0$ for all neighbors, the sum is $-1 \times 4$ for every non-terminal state.

* $v_{1}(s) = 0.25 \times ([-1+0] \times 4) = \mathbf{-1.0}$ (for all non-terminal states).

$$\mathbf{v_1} = \begin{pmatrix} 0 & -1.0 & -1.0 \\ -1.0 & -1.0 & -1.0 \\ -1.0 & -1.0 & 0 \end{pmatrix}$$

#### Iteration 2 ($k=2$):

We use $v_1$ to calculate $v_2$.

* **State (1,1):** All 4 neighbors are non-terminal, with $v_1=-1.0$.
    * $v_{2}(1,1) = 0.25 \times 4 \times [-1 + (-1.0)] = \mathbf{-2.0}$
* **State (0,1):** (Up leads to 0, Left leads to 0, Down leads to (1,1), Right leads to (0,2)).
    * $v_{2}(0,1) = 0.25 \times ([-1+0] + [-1+0] + [-1+(-1.0)] + [-1+(-1.0)])$
    * $v_{2}(0,1) = 0.25 \times (-1 - 1 - 2 - 2) = 0.25 \times (-6) = \mathbf{-1.5}$
* **State (2,1):** (Down leads to 0, Right leads to 0, Up leads to (1,1), Left leads to (2,0)).
    * $v_{2}(2,1) = 0.25 \times ([-1+0] + [-1+0] + [-1+(-1.0)] + [-1+(-1.0)])$
    * $v_{2}(2,1) = 0.25 \times (-6) = \mathbf{-1.5}$

$$\mathbf{v_2} = \begin{pmatrix} 0 & -1.5 & -1.5 \\ -1.5 & -2.0 & -1.5 \\ -1.5 & -1.5 & 0 \end{pmatrix}$$

### 3.3 Policy Improvement (Greedy Action from (1,1))

From $v_2(1,1)=-2.0$, we check $R + v_2(s')$ for neighbors:

* **Up (0,1):** $-1 + v_2(0,1) = -1 + (-1.5) = \mathbf{-2.5}$
* **Down (2,1):** $-1 + v_2(2,1) = -1 + (-1.5) = \mathbf{-2.5}$
* **Left (1,0):** $-1 + v_2(1,0) = -1 + (-1.5) = \mathbf{-2.5}$
* **Right (1,2):** $-1 + v_2(1,2) = -1 + (-1.5) = \mathbf{-2.5}$

The best action is any action: **Up, Down, Left, or Right**, as they all yield the best next step value of $-2.5$. The policy would be improved by choosing any of these over the random policy.

---

## 💡 Question 4: Model-Free - Monte Carlo Prediction

### 4.1 Tracking Calculations

| Episode | State | Return ($G$) (First Visit) | Returns Array Before Episode |        $V(s)$ After Episode         |
| :-----: | :---: | :------------------------: | :--------------------------: | :---------------------------------: |
|    1    | $S_0$ |  $2+5+3+1 = \mathbf{11}$   |             {0}              |        $\mathbf{11/1 = 11}$         |
|    1    | $S_1$ |    $5+3+1 = \mathbf{9}$    |             {0}              |         $\mathbf{9/1 = 9}$          |
|    1    | $S_2$ |        $\mathbf{1}$        |             {0}              |         $\mathbf{1/1 = 1}$          |
|  **2**  | $S_0$ |     $1+3 = \mathbf{4}$     |            {11}              |      $\mathbf{(11+4)/2 = 7.5}$      |
|  **2**  | $S_1$ |    $4+1+3 = \mathbf{8}$    |             {9}              |      $\mathbf{(9+8)/2 = 8.5}$       |
|  **2**  | $S_2$ |        $\mathbf{3}$        |             {1}              |       $\mathbf{(1+3)/2 = 2}$        |
|  **3**  | $S_0$ | $4+1+2+1+2 = \mathbf{10}$  |           {11, 4}            | $\mathbf{(11+4+10)/3 \approx 8.33}$ |
|  **3**  | $S_1$ |    $2+1+2 = \mathbf{5}$    |            {9, 8}            |  $\mathbf{(9+8+5)/3 \approx 7.33}$  |
|  **3**  | $S_2$ |        $\mathbf{2}$        |            {1, 3}            |      $\mathbf{(1+3+2)/3 = 2}$       |

### 4.2 Action-Value Estimation

In the Model-Free setting, $q_{\pi}(s,a)$ is estimated by considering each **state-action pair $(s,a)$ as a single composite state $k$**.

* The algorithm averages the **returns ($G$) that follow the first time the specific pair $(s,a)$** is visited in an episode.
* This circumvents the need for the environment model because the value is learned directly from the observed experience $s_0, a_0, r_0, s_1, a_1, r_1, \dots$.

---

## 💡 Question 5: Exploration vs. Exploitation & The Greedy Problem

### 5.1 The Exploration-Exploitation Dilemma

* **Dilemma:** The agent must choose between:
    * **Exploitation:** Taking the action that is currently known to yield the highest reward to maximize the immediate return.
    * **Exploration:** Taking a suboptimal or untried action to discover more accurate state/action values or potentially higher rewards in the long run. 
* **Why it's pronounced in Model-Free RL:** In Model-Free learning, the true $q(s,a)$ values are initially unknown and are ==only estimations based on sampled experience==. If the agent only exploits its current best estimate (which could be inaccurate), it might never discover the truly optimal action, especially if that action has a large negative immediate reward but a large positive future reward. 

### 5.2 Not Greedy Example Analysis

| Path | Reward Sequence | Total Return ($\gamma=1$) |
| :---: | :---: | :---: |
| Start $\rightarrow$ S | +1 | $\mathbf{1}$ |
| Start $\rightarrow$ T $\rightarrow$ K | +3, -20 | $\mathbf{-17}$ |
| Start $\rightarrow$ H $\rightarrow$ E | +2, -15 | $\mathbf{-13}$ |

1.  **a. Immediate Greedy Choice:** The agent would choose the action leading to **T** (reward: 3), as it provides the highest immediate reward.
2.  **b. Optimal Policy and Lesson:**
    * **Optimal Policy:** The optimal action from the Start State is the one leading to **S**, as it yields the maximum total return of $\mathbf{1}$.
    * **Key Lesson:** This example illustrates the importance of considering the **Delayed Reward**. A choice that is locally greedy (maximizing the immediate reward) is globally poor (resulting in a total return of $-17$), while ==the optimal policy must optimize the total **accumulated reward** over time.==

