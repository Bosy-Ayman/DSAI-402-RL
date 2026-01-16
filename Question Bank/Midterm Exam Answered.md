# Question 1 : MC
not solved yet



# Question 2 : Markov Decision Process (MDP) Solution

## Problem Statement

We are dealing with a non-episodic environment with two states ($S_1, S_2$) and a set of actions defined by the policy $\Pi$.

**Sample Transition Matrix**

Since the specific transition matrix was not provided, we will initialize the problem with the following values:

|Current State ($s$)|Action ($a$)|Next State ($s'$)|Probability $P(s' \mid s, a)$|Reward $R(s, a, s')$|
|---|---|---|---|---|
|$S_1$|$a_1$|$S_1$|0.5|10|
|||$S_2$|0.5|0|
|$S_1$|$a_2$|$S_1$|0.0|0|
|||$S_2$|1.0|2|
|$S_2$|$a_1$|$S_1$|0.1|0|
|||$S_2$|0.9|1|
|$S_2$|$a_2$|$S_1$|0.9|5|
|||$S_2$|0.1|0|

## Part 0: The Bellman Equation

To find the best policy (Optimal Policy $\pi^*$), we use the **Bellman Optimality Equation**.

The value of a state under the optimal policy, denoted $V^*(s)$, is the maximum expected return achievable from that state. It is defined as:

$$V^*(s) = \max_{a} \sum_{s'} P(s' | s, a) \big[ R(s, a, s') + \gamma V^*(s') \big]$$

Where:

- $s$: Current state ($S_1$ or $S_2$)
    
- $a$: Action taken
    
- $s'$: Next state
    
- $P(s' | s, a)$: Transition probability
    
- $R(s, a, s')$: Reward for the transition
    
- $\gamma$: Discount factor
    

## Part I: Algorithm for the Policy (Given $V_1=50, V_2=55$)

Here, we are asked to find the policy $\pi$ (which action to take) given that we already know the values of the states are $V(S_1) = 50$ and $V(S_2) = 55$. We assume $\gamma = 0.9$. This process is known as **Policy Extraction**.

### The Algorithm

For each state $s$, the policy $\pi(s)$ is the action $a$ that maximizes the immediate reward plus the discounted future value.

$$\pi(s) = \arg\max_{a} \sum_{s'} P(s' | s, a) \big[ R(s, a, s') + \gamma V(s') \big]$$

### Application to our Matrix

**Calculations for State** $S_1$ **&** $S_2$

|State|Action|Calculation Logic|Q-Value|Optimal Action?|
|---|---|---|---|---|
|$S_1$|$a_1$|$0.5[10 + 0.9(50)] + 0.5[0 + 0.9(55)]$|**52.25**|**Yes** ($\pi(S_1) = a_1$)|
|$S_1$|$a_2$|$0[0 + 0.9(50)] + 1.0[2 + 0.9(55)]$|51.50|No|
|$S_2$|$a_1$|$0.1[0 + 0.9(50)] + 0.9[1 + 0.9(55)]$|**49.95**|**Tie**|
|$S_2$|$a_2$|$0.9[5 + 0.9(50)] + 0.1[0 + 0.9(55)]$|**49.95**|**Tie**|

**Result:**

- $\pi(S_1) = a_1$
    
- $\pi(S_2) = \{a_1, a_2\}$ (Either action is optimal)
    

## Part II: Calculate Optimal Policy ($\gamma = 0.9$)

To find the optimal policy from scratch, we use **Value Iteration**.

### Step 1: Initialization

Initialize $V_0(S_1) = 0$ and $V_0(S_2) = 0$.

### Step 2: Iteration 1 ($k=1$)

We calculate $V_1$ using the Bellman Update Rule:

$$V_{k+1}(s) = \max_{a} \sum_{s'} P(s' | s, a) \big[ R(s, a, s') + \gamma V_k(s') \big]$$

**Calculations using** $V_0=0$

|State|Action|Calculation Logic ($V_0=0$)|Q-Value|New $V_1(s)$|
|---|---|---|---|---|
|$S_1$|$a_1$|$0.5[10 + 0] + 0.5[0 + 0]$|**5.0**|$V_1(S_1) = 5.0$|
|$S_1$|$a_2$|$1.0[2 + 0]$|2.0||
|$S_2$|$a_1$|$0.1[0] + 0.9[1]$|0.9||
|$S_2$|$a_2$|$0.9[5] + 0.1[0]$|**4.5**|$V_1(S_2) = 4.5$|

### Step 3: Iterate until Convergence

You would repeat Step 2 using the new values ($V_1(S_1)=5, V_1(S_2)=4.5$) until the numbers stabilize. Once stable, you perform the **Final Extraction** (same as Part I) to determine the best policy.
# Question 2: Policy Iteration Problem & Solution
## Method 1 : solve an equation to find the V0(S)
## 1. The Full Question

**Problem Statement:** Consider the following Markov Decision Process (MDP).

- **States:** $S_1, S_2, S_3$
    
- **Actions:** $a_1, a_2$
    
- **Discount Factor (**$\gamma$**):** $0.5$ (Assumed for calculation)
    
- **Initial Policy (**$\pi_0$**):**
    
    - $\pi(S_1) = a_1$
        
    - $\pi(S_2) = a_2$
        
    - $\pi(S_3) = a_2$
        

**Transition and Reward Table:** _Note: Transitions for S2 were missing in the prompt, so standard logical values have been assumed to allow for a solution._

|Current State|Action|Next State Probabilities|Reward|
|---|---|---|---|
|**S1**|a1|0.7 $S_1$, 0.3 $S_2$|2|
|**S1**|a2|0.6 $S_3$, 0.4 $S_2$|3|
|**S2**|a1|1.0 $S_1$ (Assumed)|1 (Assumed)|
|**S2**|a2|1.0 $S_2$|4|
|**S3**|a1|1.0 $S_3$|0|
|**S3**|a2|1.0 $S_1$|1|

**Task:**

1. Perform **Policy Evaluation** for the initial policy $\pi_0$.
    
2. Perform **Policy Improvement** to generate the new policy $\pi_1$.
    

## 2. Solution: Step-by-Step

### Step 1: Policy Evaluation

We must calculate the Value function $V^\pi(s)$ for the current policy. The Bellman Expectation Equation is:

$$V^\pi(s) = \sum P(s'|s, \pi(s)) [R(s, \pi(s), s') + \gamma V^\pi(s')]$$

Based on our initial policy $\pi_0 = \{S_1: a_1, S_2: a_2, S_3: a_2\}$, we set up the system of equations:

1. **For S2 (Action** $a_2$**):**
    
    $$V(S_2) = 4 + 0.5 [ 1.0 \times V(S_2) ]$$$$V(S_2) = 4 + 0.5 V(S_2)$$$$0.5 V(S_2) = 4$$$$V(S_2) = 8$$
2. **For S1 (Action** $a_1$**):**
    
    $$V(S_1) = 2 + 0.5 [ 0.7 V(S_1) + 0.3 V(S_2) ]$$
    
    Substitute $V(S_2) = 8$:
    
    $$V(S_1) = 2 + 0.5 [ 0.7 V(S_1) + 2.4 ]$$$$V(S_1) = 2 + 0.35 V(S_1) + 1.2$$$$V(S_1) - 0.35 V(S_1) = 3.2$$$$0.65 V(S_1) = 3.2$$$$V(S_1) = 3.2 / 0.65$$$$V(S_1) \approx 4.92$$
3. **For S3 (Action** $a_2$**):**
    
    $$V(S_3) = 1 + 0.5 [ 1.0 \times V(S_1) ]$$
    
    Substitute $V(S_1) = 4.92$:
    
    $$V(S_3) = 1 + 0.5(4.92)$$$$V(S_3) = 3.46$$

**Current Values:**

- $V(S_1) = 4.92$
    
- $V(S_2) = 8.00$
    
- $V(S_3) = 3.46$
    

### Step 2: Policy Improvement

We calculate the Q-values for all actions using the $V$ values from Step 1.

$$Q(s, a) = R(s,a) + \gamma \sum P(s'|s,a) V(s')$$

**1. Improve State S1:**

- **Action** $a_1$ **(Current):** $Q(S_1, a_1) = V(S_1) = 4.92$
    
- **Action** $a_2$ **(Alternative):**
    
    $$Q(S_1, a_2) = 3 + 0.5 [ 0.6 V(S_3) + 0.4 V(S_2) ]$$$$Q(S_1, a_2) = 3 + 0.5 [ 0.6(3.46) + 0.4(8.00) ]$$$$Q(S_1, a_2) = 3 + 0.5 [ 2.076 + 3.2 ]$$$$Q(S_1, a_2) = 3 + 2.638 = \mathbf{5.64}$$
- **Conclusion:** Since $5.64 > 4.92$, change policy to $a_2$.
    

**2. Improve State S2:**

- **Action** $a_1$ **(Alternative):**
    
    $$Q(S_2, a_1) = 1 + 0.5 [ 1.0 V(S_1) ]$$$$Q(S_2, a_1) = 1 + 0.5(4.92) = 3.46$$
- **Action** $a_2$ **(Current):** $Q(S_2, a_2) = V(S_2) = \mathbf{8.00}$
    
- **Conclusion:** Since $8.00 > 3.46$, keep policy as $a_2$.
    

**3. Improve State S3:**

- **Action** $a_1$ **(Alternative):**
    
    $$Q(S_3, a_1) = 0 + 0.5 [ 1.0 V(S_3) ]$$$$Q(S_3, a_1) = 0 + 0.5(3.46) = 1.73$$
- **Action** $a_2$ **(Current):** $Q(S_3, a_2) = V(S_3) = \mathbf{3.46}$
    
- **Conclusion:** Since $3.46 > 1.73$, keep policy as $a_2$.
    

## 3. Final Answer

**The New Policy (**$\pi_{new}$**):**

| State  | Old Action | New Action |
| ------ | ---------- | ---------- |
| **S1** | a1         | **a2**     |
| **S2** | a2         | **a2**     |
| **S3** | a2         | **a2**     |

---
## Method 2 : we will initialize v(s) = 0

# Policy Iteration Problem & Solution

## 2. Solution: Step-by-Step

### Step 1: Policy Evaluation (One Sweep)

We perform exactly **one iteration** ($k=1$) of the Bellman Expectation Equation. We initialize $V_0(s) = 0$.

$$V_{1}(s) = R(s, \pi(s)) + \gamma \sum P(s'|s, \pi(s)) V_0(s')$$

Since $V_0(s') = 0$, the equation simplifies to just the immediate reward for this first sweep:

- **For S1 (**$a_1$**):**
    
    $$V_1(S_1) = 2 + 0.5 [ 0.7(0) + 0.3(0) ] = \mathbf{2.0}$$
- **For S2 (**$a_2$**):**
    
    $$V_1(S_2) = 4 + 0.5 [ 1.0(0) ] = \mathbf{4.0}$$
- **For S3 (**$a_2$**):**
    
    $$V_1(S_3) = 1 + 0.5 [ 1.0(0) ] = \mathbf{1.0}$$

**Values after One Sweep:**

- $V(S_1) = 2.0$
    
- $V(S_2) = 4.0$
    
- $V(S_3) = 1.0$
    

### Step 2: Policy Improvement

We calculate the Q-values for all actions using the $V_1$ **values** calculated above.

$$Q(s, a) = R(s,a) + \gamma \sum P(s'|s,a) V_1(s')$$

**1. Improve State S1:**

- **Action** $a_1$ **(Current):**
    
    $$Q(S_1, a_1) = 2 + 0.5 [ 0.7(2.0) + 0.3(4.0) ]$$$$Q(S_1, a_1) = 2 + 0.5 [ 1.4 + 1.2 ] = 2 + 1.3 = \mathbf{3.3}$$
- **Action** $a_2$ **(Alternative):**
    
    $$Q(S_1, a_2) = 3 + 0.5 [ 0.6(1.0) + 0.4(4.0) ]$$$$Q(S_1, a_2) = 3 + 0.5 [ 0.6 + 1.6 ] = 3 + 1.1 = \mathbf{4.1}$$
- **Conclusion:** Since $4.1 > 3.3$, change policy to $a_2$.
    

**2. Improve State S2:**

- **Action** $a_1$ **(Alternative):**
    
    $$Q(S_2, a_1) = 1 + 0.5 [ 1.0(2.0) ]$$$$Q(S_2, a_1) = 1 + 1.0 = \mathbf{2.0}$$
- **Action** $a_2$ **(Current):**
    
    $$Q(S_2, a_2) = 4 + 0.5 [ 1.0(4.0) ]$$$$Q(S_2, a_2) = 4 + 2.0 = \mathbf{6.0}$$
- **Conclusion:** Since $6.0 > 2.0$, keep policy as $a_2$.
    

**3. Improve State S3:**

- **Action** $a_1$ **(Alternative):**
    
    $$Q(S_3, a_1) = 0 + 0.5 [ 1.0(1.0) ]$$$$Q(S_3, a_1) = 0 + 0.5 = \mathbf{0.5}$$
- **Action** $a_2$ **(Current):**
    
    $$Q(S_3, a_2) = 1 + 0.5 [ 1.0(2.0) ]$$$$Q(S_3, a_2) = 1 + 1.0 = \mathbf{2.0}$$
- **Conclusion:** Since $2.0 > 0.5$, keep policy as $a_2$.
    

## 3. Final Answer

**The New Policy (**$\pi_{new}$**):**

|State|Old Action|New Action|
|---|---|---|
|**S1**|a1|**a2**|
|**S2**|a2|**a2**|
|**S3**|a2|**a2**|

---
# Question 3:  Complexity

Define $|S|$ as the number of states and $|A|$ as the number of actions.

### 1. Policy Evaluation

Policy evaluation computes the value function $V^\pi(s)$ for a specific, fixed policy.

- **Analytical Solution (Solving Linear Equations):** $O(|S|^3)$
    
    - This approach involves inverting a matrix of size $|S| \times |S|$ to solve $(I - \gamma P)V = R$.
        
- **Iterative Solution:** $O(|S|^2)$ per iteration
    
    - For each state, we iterate over all possible next states to update the value.
        

### 2. Policy Improvement

Policy improvement generates a new, greedy policy by looking at the current value function $V(s)$.

- **Complexity:** $O(|S|^2 \cdot |A|)$
    
    - To improve the policy, we must calculate the Q-value for every action in every state.
        
    - For **each state** ($|S|$), we iterate over **each action** ($|A|$).
        
    - For each action, we sum over the probabilities of **next states** ($|S|$).
        
    - **Total:** $|S| \times |A| \times |S| = O(|S|^2 |A|)$.