
# Question 1 : Monte Carlo


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