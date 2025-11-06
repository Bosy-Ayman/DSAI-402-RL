### Questions collected from these links:
 https://www.cs.cmu.edu/~15281-s20/recitations/rec8/rec8_sol.pdf
 
https://inst.eecs.berkeley.edu/~cs188/textbook/mdp/value-iteration.html

https://drive.google.com/drive/folders/1G5jykkoGMt8XAPdeOP2kP_ZqghpoFRdz

https://drive.google.com/file/d/11_oVkIcoS-9D8btd7I4j0uIJGExlQeeG/view
# Question 1 : 

**Explained here:** 
1- https://www.youtube.com/watch?v=hXaVyWkyEdk&list=PLp8QV47qJEg4jFp_HLrNXALHwISaefUqF&index=5  (25:00 min)
2 - https://www.youtube.com/watch?v=0t-QpSABExg&list=PLp8QV47qJEg79XnSgOCqp7EbjQ-pp9xyp&index=5 (better)
## (a) What is the transition function ($T(s,a,s')$)?

The transition function, $T(s, a, s')$, gives the probability of landing in state $s'$ **given** that you are in state $s$ and take action $a$. We must list this for all possible $s$ and $a$.

### 1. Action: `Stop`

This action is **deterministic** (it's not random). The rules state that if the car chooses `Stop`, the game ends. Our "end" state is `Done`.

- Therefore, for any state $s \in \{0, 2, 3, 4, 5\}$, the probability of transitioning to `Done` after choosing `Stop` is 1.
    

$$T(s, \text{Stop}, \text{Done}) = 1 \quad \text{for } s \in \{0, 2, 3, 4, 5\}$$

### 2. Action: `Move`
![[Pasted image 20251106170153.png]]

This action is **stochastic** (it's random). The car moves 2, 3, or 4 spaces, each with equal probability (1/3). We need to calculate the resulting state ($s'$) for each starting state ($s$).

- **From $s=0$:**
    
    - Move +2 $\to$ $s'=2$. Prob = 1/3.
        
    - Move +3 $\to$ $s'=3$. Prob = 1/3.
        
    - Move +4 $\to$ $s'=4$. Prob = 1/3.
        
    - _Transitions:_ $T(0, \text{Move}, 2) = \tfrac{1}{3}$, $T(0, \text{Move}, 3) = \tfrac{1}{3}$, $T(0, \text{Move}, 4) = \tfrac{1}{3}$.
        
- **From $s=2$:**
    
    - Move +2 $\to$ $2+2=4$. So, $s'=4$. Prob = 1/3.
        
    - Move +3 $\to$ $2+3=5$. So, $s'=5$. Prob = 1/3.
        
    - Move +4 $\to$ $2+4=6$. The rule says "total reaches 6 or higher, the game ends." So, $s'=\text{Done}$. Prob = 1/3.
        
    - _Transitions:_ $T(2, \text{Move}, 4) = \tfrac{1}{3}$, $T(2, \text{Move}, 5) = \tfrac{1}{3}$, $T(2, \text{Move}, \text{Done}) = \tfrac{1}{3}$.
        
- **From $s=3$:**
    
    - Move +2 $\to$ $3+2=5$. So, $s'=5$. Prob = 1/3.
        
    - Move +3 $\to$ $3+3=6$. So, $s'=\text{Done}$. Prob = 1/3.
        
    - Move +4 $\to$ $3+4=7$. This is also $\ge 6$, so $s'=\text{Done}$. Prob = 1/3.
        
    - _Transitions:_ We combine the two "Done" outcomes: $T(3, \text{Move}, 5) = \tfrac{1}{3}$, $T(3, \text{Move}, \text{Done}) = \tfrac{1}{3} + \tfrac{1}{3} = \tfrac{2}{3}$.
        
- **From $s=4$:**
    
    - Move +2 $\to$ $4+2=6$ ($s'=\text{Done}$). Prob = 1/3.
        
    - Move +3 $\to$ $4+3=7$ ($s'=\text{Done}$). Prob = 1/3.
        
    - Move +4 $\to$ $4+4=8$ ($s'=\text{Done}$). Prob = 1/3.
        
    - _Transitions:_ All outcomes lead to `Done`. $T(4, \text{Move}, \text{Done}) = \tfrac{1}{3} + \tfrac{1}{3} + \tfrac{1}{3} = 1$.
        
- **From $s=5$:**
    
    - Move +2 $\to$ $5+2=7$ ($s'=\text{Done}$). Prob = 1/3.
        
    - Move +3 $\to$ $5+3=8$ ($s'=\text{Done}$). Prob = 1/3.
        
    - Move +4 $\to$ $5+4=9$ ($s'=\text{Done}$). Prob = 1/3.
        
    - _Transitions:_ All outcomes lead to `Done`. $T(5, \text{Move}, \text{Done}) = 1$.
        

(All other transitions $T(s,a,s')$ are 0.)

---

## (b) What is the reward function ($R(s,a,s')$)?

The reward function, $R(s, a, s')$, gives the **immediate reward** you get for taking action $a$ from state $s$ and landing in state $s'$.

- **Action: `Stop`**
    
    - The rule says: "If the car chooses `Stop`... reward = the current total spaces moved."
        
    - This reward is received when you transition to the `Done` state.
        
    - $R(0, \text{Stop}, \text{Done}) = 0$
        
    - $R(2, \text{Stop}, \text{Done}) = 2$
        
    - $R(3, \text{Stop}, \text{Done}) = 3$
        
    - $R(4, \text{Stop}, \text{Done}) = 4$
        
    - $R(5, \text{Stop}, \text{Done}) = 5$
        
- **Action: `Move`**
    
    - The rule says: "`Move` has no immediate reward."
        
    - This means the reward is 0 for _any_ transition caused by `Move`, even if it ends the game.
        
    - $R(s, \text{Move}, s') = 0$ for all $s, s'$.
        
- **Automatic End (Moving $\ge 6$)**
    
    - The rule says: "If the total reaches 6 or higher, the game ends automatically and the car receives reward 0."
        
    - This confirms our `Move` reward. For example, $R(2, \text{Move}, \text{Done}) = 0$, $R(4, \text{Move}, \text{Done}) = 0$, etc.
        

---

## (c) Do value iteration for 4 iterations with ($\gamma=1$).

**Value Iteration** is an algorithm to find the optimal value $V^*(s)$ of each state. The "value" of a state is the maximum expected reward you can get starting from that state.

We use the Bellman Update equation:

$$V_{k+1}(s) = \max_{a} \sum_{s'} T(s, a, s') \big( R(s, a, s') + \gamma V_k(s') \big)$$

This looks complex, but it's just a formula for "The value of my state is the **best action** I can take." The value of an action is the _average_ (the $\sum$) of: (the _immediate reward_) + (the _discounted value of where I land_).

We are given $\gamma=1$ and start with $V_0(s) = 0$ for all states.

- **Key:** The value of the terminal state is always 0: $V_k(\text{Done}) = 0$ for all $k$.
    

Let's calculate the value of each action (the "Q-value") for each state.

- $Q(s, \text{Stop}) = T(s, \text{Stop}, \text{Done}) \cdot (R(s, \text{Stop}, \text{Done}) + \gamma V_k(\text{Done}))$
    
    - $Q(s, \text{Stop}) = 1 \cdot (s + 1 \cdot 0) = s$
        
    - **The value of `Stop` is _always_ equal to the current state's score $s$.**
        
- $Q(s, \text{Move}) = \sum_{s'} T(s, \text{Move}, s') \cdot (R(s, \text{Move}, s') + \gamma V_k(s'))$
    
    - Since $R(s, \text{Move}, s') = 0$ and $\gamma=1$, this simplifies to:
        
    - **$Q(s, \text{Move}) = \sum_{s'} T(s, \text{Move}, s') \cdot V_k(s')$**
        

Then, $V_{k+1}(s) = \max(Q(s, \text{Stop}), Q(s, \text{Move}))$.

---

Iteration 0:

$V_0 = [V(0), V(2), V(3), V(4), V(5)]$

$$V_0 = [0.0, 0.0, 0.0, 0.0, 0.0]$$

---

**Iteration 1 (using $V_0$):**

- $V_1(0) = \max(Q(0, \text{Stop}), Q(0, \text{Move}))$
    
    - $Q(0, \text{Stop}) = 0$
        
    - $Q(0, \text{Move}) = \tfrac{1}{3}V_0(2) + \tfrac{1}{3}V_0(3) + \tfrac{1}{3}V_0(4) = \tfrac{1}{3}(0) + \tfrac{1}{3}(0) + \tfrac{1}{3}(0) = 0$
        
    - $V_1(0) = \max(0, 0) = 0$
        
- $V_1(2) = \max(Q(2, \text{Stop}), Q(2, \text{Move}))$
    
    - $Q(2, \text{Stop}) = 2$
        
    - $Q(2, \text{Move}) = \tfrac{1}{3}V_0(4) + \tfrac{1}{3}V_0(5) + \tfrac{1}{3}V_0(\text{Done}) = \tfrac{1}{3}(0) + \tfrac{1}{3}(0) + \tfrac{1}{3}(0) = 0$
        
    - $V_1(2) = \max(2, 0) = 2$
        
- $V_1(3) = \max(Q(3, \text{Stop}), Q(3, \text{Move}))$
    
    - $Q(3, \text{Stop}) = 3$
        
    - $Q(3, \text{Move}) = \tfrac{1}{3}V_0(5) + \tfrac{2}{3}V_0(\text{Done}) = \tfrac{1}{3}(0) + \tfrac{2}{3}(0) = 0$
        
    - $V_1(3) = \max(3, 0) = 3$
        
- $V_1(4) = \max(Q(4, \text{Stop}), Q(4, \text{Move}))$
    
    - $Q(4, \text{Stop}) = 4$
        
    - $Q(4, \text{Move}) = 1 \cdot V_0(\text{Done}) = 0$
        
    - $V_1(4) = \max(4, 0) = 4$
        
- $V_1(5) = \max(Q(5, \text{Stop}), Q(5, \text{Move}))$
    
    - $Q(5, \text{Stop}) = 5$
        
    - $Q(5, \text{Move}) = 1 \cdot V_0(\text{Done}) = 0$
        
    - $V_1(5) = \max(5, 0) = 5$
        

$$V_1 = [0.0, 2.0, 3.0, 4.0, 5.0]$$

---

**Iteration 2 (using $V_1$):**

- $V_2(0) = \max(Q(0, \text{Stop}), Q(0, \text{Move}))$
    
    - $Q(0, \text{Stop}) = 0$
        
    - $Q(0, \text{Move}) = \tfrac{1}{3}V_1(2) + \tfrac{1}{3}V_1(3) + \tfrac{1}{3}V_1(4) = \tfrac{1}{3}(2) + \tfrac{1}{3}(3) + \tfrac{1}{3}(4) = \tfrac{9}{3} = 3.0$
        
    - $V_2(0) = \max(0, 3.0) = 3.0$
        
- $V_2(2) = \max(Q(2, \text{Stop}), Q(2, \text{Move}))$
    
    - $Q(2, \text{Stop}) = 2$
        
    - $Q(2, \text{Move}) = \tfrac{1}{3}V_1(4) + \tfrac{1}{3}V_1(5) + \tfrac{1}{3}V_1(\text{Done}) = \tfrac{1}{3}(4) + \tfrac{1}{3}(5) + \tfrac{1}{3}(0) = \tfrac{9}{3} = 3.0$
        
    - $V_2(2) = \max(2, 3.0) = 3.0$
        
- $V_2(3) = \max(Q(3, \text{Stop}), Q(3, \text{Move}))$
    
    - $Q(3, \text{Stop}) = 3$
        
    - $Q(3, \text{Move}) = \tfrac{1}{3}V_1(5) + \tfrac{2}{3}V_1(\text{Done}) = \tfrac{1}{3}(5) + \tfrac{2}{3}(0) = \tfrac{5}{3} \approx 1.67$
        
    - $V_2(3) = \max(3, 1.67) = 3.0$
        
- $V_2(4) = \max(Q(4, \text{Stop}), Q(4, \text{Move}))$
    
    - $Q(4, \text{Stop}) = 4$
        
    - $Q(4, \text{Move}) = 0$
        
    - $V_2(4) = \max(4, 0) = 4.0$
        
- $V_2(5) = \max(Q(5, \text{Stop}), Q(5, \text{Move}))$
    
    - $Q(5, \text{Stop}) = 5$
        
    - $Q(5, \text{Move}) = 0$
        
    - $V_2(5) = \max(5, 0) = 5.0$
        

$$V_2 = [3.0, 3.0, 3.0, 4.0, 5.0]$$

---

**Iteration 3 (using $V_2$):**

- $V_3(0) = \max(Q(0, \text{Stop}), Q(0, \text{Move}))$
    
    - $Q(0, \text{Stop}) = 0$
        
    - $Q(0, \text{Move}) = \tfrac{1}{3}V_2(2) + \tfrac{1}{3}V_2(3) + \tfrac{1}{3}V_2(4) = \tfrac{1}{3}(3) + \tfrac{1}{3}(3) + \tfrac{1}{3}(4) = \tfrac{10}{3} \approx 3.33$
        
    - $V_3(0) = \max(0, 3.33) = 3.33$
        
- $V_3(2) = \max(Q(2, \text{Stop}), Q(2, \text{Move}))$
    
    - $Q(2, \text{Stop}) = 2$
        
    - $Q(2, \text{Move}) = \tfrac{1}{3}V_2(4) + \tfrac{1}{3}V_2(5) + \tfrac{1}{3}V_2(\text{Done}) = \tfrac{1}{3}(4) + \tfrac{1}{3}(5) + \tfrac{1}{3}(0) = \tfrac{9}{3} = 3.0$
        
    - $V_3(2) = \max(2, 3.0) = 3.0$
        
- $V_3(3) = \max(Q(3, \text{Stop}), Q(3, \text{Move}))$
    
    - $Q(3, \text{Stop}) = 3$
        
    - $Q(3, \text{Move}) = \tfrac{1}{3}V_2(5) + \tfrac{2}{3}V_2(\text{Done}) = \tfrac{1}{3}(5) + \tfrac{2}{3}(0) = \tfrac{5}{3} \approx 1.67$
        
    - $V_3(3) = \max(3, 1.67) = 3.0$
        
- $V_3(4) = \max(4, 0) = 4.0$
    
- $V_3(5) = \max(5, 0) = 5.0$
    

$$V_3 \approx [3.33, 3.0, 3.0, 4.0, 5.0]$$

---

**Iteration 4 (using $V_3$):**

- $V_4(0) = \max(Q(0, \text{Stop}), Q(0, \text{Move}))$
    
    - $Q(0, \text{Stop}) = 0$
        
    - $Q(0, \text{Move}) = \tfrac{1}{3}V_3(2) + \tfrac{1}{3}V_3(3) + \tfrac{1}{3}V_3(4) = \tfrac{1}{3}(3) + \tfrac{1}{3}(3) + \tfrac{1}{3}(4) = \tfrac{10}{3} \approx 3.33$
        
    - $V_4(0) = \max(0, 3.33) = 3.33$
        
- $V_4(2) = \max(Q(2, \text{Stop}), Q(2, \text{Move}))$
    
    - $Q(2, \text{Stop}) = 2$
        
    - $Q(2, \text{Move}) = \tfrac{1}{3}V_3(4) + \tfrac{1}{3}V_3(5) + \tfrac{1}{3}V_3(\text{Done}) = \tfrac{1}{3}(4) + \tfrac{1}{3}(5) + \tfrac{1}{3}(0) = \tfrac{9}{3} = 3.0$
        
    - $V_4(2) = \max(2, 3.0) = 3.0$
        
- ...and so on. We see that $V_4(3)=3$, $V_4(4)=4$, $V_4(5)=5$.
    

$$V_4 \approx [3.33, 3.0, 3.0, 4.0, 5.0]$$

Result:

The values are $V_4 = V_3$, so the algorithm has converged.

|**State**|**V0​**|**V1​**|**V2​**|**V3​**|**V4​**|
|---|---|---|---|---|---|
|**0**|0.0|0.0|3.0|3.33|3.33|
|**2**|0.0|2.0|3.0|3.0|3.0|
|**3**|0.0|3.0|3.0|3.0|3.0|
|**4**|0.0|4.0|4.0|4.0|4.0|
|**5**|0.0|5.0|5.0|5.0|5.0|

---

## (d) What is the optimal policy (after convergence) for ($\gamma=1$)?

The optimal policy $\pi^*(s)$ is the action that resulted in the maximum value in our final, converged iteration ($V_4$). We just need to look at which Q-value "won" the $\max()$ function for each state.

- **State 0:**
    
    - $Q(0, \text{Stop}) = 0$
        
    - $Q(0, \text{Move}) \approx 3.33$
        
    - **Best action: `Move`**
        
- **State 2:**
    
    - $Q(2, \text{Stop}) = 2$
        
    - $Q(2, \text{Move}) = 3.0$
        
    - **Best action: `Move`**
        
- **State 3:**
    
    - $Q(3, \text{Stop}) = 3$
        
    - $Q(3, \text{Move}) \approx 1.67$
        
    - **Best action: `Stop`**
        
- **State 4:**
    
    - $Q(4, \text{Stop}) = 4$
        
    - $Q(4, \text{Move}) = 0$
        
    - **Best action: `Stop`**
        
- **State 5:**
    
    - $Q(5, \text{Stop}) = 5$
        
    - $Q(5, \text{Move}) = 0$
        
    - **Best action: `Stop`**
        

Optimal Policy $\pi^*$:

| State | 0 | 2 | 3 | 4 | 5 |

| :--- | :--- | :--- | :--- | :--- | :--- |

| Action | Move | Move | Stop | Stop | Stop |

**Intuition:** At states 4 and 5, moving gives a 100% chance of a 0 reward, so stopping is obvious. At state 3, moving has a 2/3 chance of a 0 reward and a 1/3 chance of landing in state 5 (value 5). The expected value $\approx 1.67$, which is worse than stopping for 3. At states 0 and 2, the risk of "busting" (going to `Done` for 0) is low enough that the _potential_ to land on 4 or 5 makes moving the better choice.

---

## (e) How do results change with ($\gamma=0.1$)? (intuitive)

The discount factor $\gamma$ controls how much we value future rewards.

- $\gamma=1$ (far-sighted): A reward tomorrow is just as good as a reward today.
    
- $\gamma=0.1$ (near-sighted): A reward tomorrow is worth only 10% of a reward today.
    

With $\gamma=0.1$, the algorithm becomes "greedy" and heavily prefers immediate rewards. The value of `Stop` (immediate reward $s$) will be much more appealing than the value of `Move` (immediate reward 0, future reward $\gamma \cdot V(s')$).

Let's re-examine the choices, especially state 2:

- **At State 2:**
    
    - $Q(2, \text{Stop}) \to$ Immediate reward of **2**.
        
    - $Q(2, \text{Move}) \to 0 + 0.1 \cdot (\text{expected future value})$
        
    - The expected future value (from landing on 4, 5, or Done) is at most 5. So $0.1 \cdot 5 = 0.5$.
        
    - Clearly, the immediate reward of **2** is much better than a discounted future reward of **$\le 0.5$**.
        
    - **The policy at state 2 will flip from `Move` to `Stop`.**
        
- **At State 0:**
    
    - $Q(0, \text{Stop}) \to$ Immediate reward of **0**.
        
    - $Q(0, \text{Move}) \to 0 + 0.1 \cdot (\text{expected future value})$
        
    - The expected future value is positive (e.g., landing on 2, 3, 4). So the value of moving is small, but still greater than 0.
        
    - **The policy at state 0 will remain `Move`.**
        

New Optimal Policy (with $\gamma=0.1$):

| State | 0 | 2 | 3 | 4 | 5 |

| :--- | :--- | :--- | :--- | :--- | :--- |

| Action | Move | Stop | Stop | Stop | Stop |

---

## (f) Policy iteration for two iterations with ($\gamma=1$).

**Policy Iteration** is a different algorithm. It involves two steps that we repeat:

1. **Policy Evaluation:** Given a _fixed_ policy $\pi$, find its _true_ value $V^\pi(s)$. We do this by solving a system of linear equations.
    
2. **Policy Improvement:** Using the values $V^\pi(s)$ we just found, act "greedily" to find a new, better policy $\pi_{k+1}$.
    

We start with $\pi_0 = [0:\text{Move}, 2:\text{Stop}, 3:\text{Move}, 4:\text{Stop}, 5:\text{Move}]$ and $\gamma=1$.
Here is a step-by-step resolution of the policy iteration problem from part (f).

**Key Information:**

- **States:** $\{0, 2, 3, 4, 5\}$. $V(\text{Done}) = 0$.
    
- **Discount Factor:** $\gamma = 1$.
    
- **Reward Function:** $R(s, \text{Stop}, \text{Done}) = s$. All other rewards are 0.
    
- **Transition Function (Abbreviated):**
    
    - $T(s, \text{Stop}) \rightarrow 1.0 \text{ to Done}$
        
    - $T(0, \text{Move}) \rightarrow 1/3 \text{ to } 2, 1/3 \text{ to } 3, 1/3 \text{ to } 4$
        
    - $T(2, \text{Move}) \rightarrow 1/3 \text{ to } 4, 1/3 \text{ to } 5, 1/3 \text{ to Done}$
        
    - $T(3, \text{Move}) \rightarrow 1/3 \text{ to } 5, 2/3 \text{ to Done}$
        
    - $T(4, \text{Move}) \rightarrow 1.0 \text{ to Done}$
        
    - $T(5, \text{Move}) \rightarrow 1.0 \text{ to Done}$
        

---

## Iteration 1: $\pi_0 \rightarrow \pi_1$

### Step 1.A: Policy Evaluation for $\pi_0$

We need to find $V^{\pi_0}$ for the policy $\pi_0 = \{\text{Move}, \text{Stop}, \text{Move}, \text{Stop}, \text{Move}\}$. We use the Bellman equation for policy evaluation, iterating until $V_k$ converges.

$V^{\pi}_{k+1}(s) = \sum_{s'} T(s, \pi(s), s')[R(s, \pi(s), s') + \gamma V^{\pi}_k(s')]$

- **Initial Values:** $V^{\pi_0}_0 = \{0, 0, 0, 0, 0\}$
    
- **Calculate $V^{\pi_0}_1$ (using $V^{\pi_0}_0$):**
    
    - $V^{\pi_0}_1(0)$ [Move]: $(1/3)[0 + 1 \cdot V^{\pi_0}_0(2)] + (1/3)[0 + 1 \cdot V^{\pi_0}_0(3)] + (1/3)[0 + 1 \cdot V^{\pi_0}_0(4)] = (1/3)[0] + (1/3)[0] + (1/3)[0] = \mathbf{0}$
        
    - $V^{\pi_0}_1(2)$ [Stop]: $1 \cdot [R(2, \text{Stop}, \text{Done}) + 1 \cdot V^{\pi_0}_0(\text{Done})] = 1 \cdot [2 + 0] = \mathbf{2}$
        
    - $V^{\pi_0}_1(3)$ [Move]: $(1/3)[0 + 1 \cdot V^{\pi_0}_0(5)] + (2/3)[0 + 1 \cdot V^{\pi_0}_0(\text{Done})] = (1/3)[0] + (2/3)[0] = \mathbf{0}$
        
    - $V^{\pi_0}_1(4)$ [Stop]: $1 \cdot [R(4, \text{Stop}, \text{Done}) + 1 \cdot V^{\pi_0}_0(\text{Done})] = 1 \cdot [4 + 0] = \mathbf{4}$
        
    - $V^{\pi_0}_1(5)$ [Move]: $1 \cdot [0 + 1 \cdot V^{\pi_0}_0(\text{Done})] = 1 \cdot [0 + 0] = \mathbf{0}$
        
    - **Result $V^{\pi_0}_1$:** $\{0, 2, 0, 4, 0\}$
        
- **Calculate $V^{\pi_0}_2$ (using $V^{\pi_0}_1$):**
    
    - $V^{\pi_0}_2(0)$ [Move]: $(1/3)[0 + V^{\pi_0}_1(2)] + (1/3)[0 + V^{\pi_0}_1(3)] + (1/3)[0 + V^{\pi_0}_1(4)] = (1/3)[2] + (1/3)[0] + (1/3)[4] = \mathbf{2}$
        
    - $V^{\pi_0}_2(2)$ [Stop]: $1 \cdot [2 + V^{\pi_0}_1(\text{Done})] = \mathbf{2}$
        
    - $V^{\pi_0}_2(3)$ [Move]: $(1/3)[0 + V^{\pi_0}_1(5)] + (2/3)[0 + V^{\pi_0}_1(\text{Done})] = (1/3)[0] + (2/3)[0] = \mathbf{0}$
        
    - $V^{\pi_0}_2(4)$ [Stop]: $1 \cdot [4 + V^{\pi_0}_1(\text{Done})] = \mathbf{4}$
        
    - $V^{\pi_0}_2(5)$ [Move]: $1 \cdot [0 + V^{\pi_0}_1(\text{Done})] = \mathbf{0}$
        
    - **Result $V^{\pi_0}_2$:** $\{2, 2, 0, 4, 0\}$
        
- **Calculate $V^{\pi_0}_3$ (using $V^{\pi_0}_2$):**
    
    - $V^{\pi_0}_3(0)$ [Move]: $(1/3)[0 + V^{\pi_0}_2(2)] + (1/3)[0 + V^{\pi_0}_2(3)] + (1/3)[0 + V^{\pi_0}_2(4)] = (1/3)[2] + (1/3)[0] + (1/3)[4] = \mathbf{2}$
        
    - (All other states also remain the same)
        
    - **Result $V^{\pi_0}_3$:** $\{2, 2, 0, 4, 0\}$
        
- **Evaluation Converged:** $V^{\pi_0} = \{2, 2, 0, 4, 0\}$.
    

### Step 1.B: Policy Improvement to find $\pi_1$

Now we find the best action for each state using $V^{\pi_0}$.

$\pi_1(s) = \arg\max_a Q(s, a)$, where $Q(s, a) = \sum_{s'} T(s, a, s')[R(s, a, s') + \gamma V^{\pi_0}(s')]$

- **State 0:**
    
    - $Q(0, \text{Stop})$: $1 \cdot [R(0, \text{Stop}, \text{Done}) + V^{\pi_0}(\text{Done})] = 1 \cdot [0 + 0] = \mathbf{0}$
        
    - $Q(0, \text{Move})$: $(1/3)[0 + V^{\pi_0}(2)] + (1/3)[0 + V^{\pi_0}(3)] + (1/3)[0 + V^{\pi_0}(4)] = (1/3)[2] + (1/3)[0] + (1/3)[4] = \mathbf{2}$
        
    - _Best: $\text{Move}$_
        
- **State 2:**
    
    - $Q(2, \text{Stop})$: $1 \cdot [R(2, \text{Stop}, \text{Done}) + V^{\pi_0}(\text{Done})] = 1 \cdot [2 + 0] = \mathbf{2}$
        
    - $Q(2, \text{Move})$: $(1/3)[0 + V^{\pi_0}(4)] + (1/3)[0 + V^{\pi_0}(5)] + (1/3)[0 + V^{\pi_0}(\text{Done})] = (1/3)[4] + (1/3)[0] + (1/3)[0] = \mathbf{4/3}$
        
    - _Best: $\text{Stop}$_
        
- **State 3:**
    
    - $Q(3, \text{Stop})$: $1 \cdot [R(3, \text{Stop}, \text{Done}) + V^{\pi_0}(\text{Done})] = 1 \cdot [3 + 0] = \mathbf{3}$
        
    - $Q(3, \text{Move})$: $(1/3)[0 + V^{\pi_0}(5)] + (2/3)[0 + V^{\pi_0}(\text{Done})] = (1/3)[0] + (2/3)[0] = \mathbf{0}$
        
    - _Best: $\text{Stop}$_
        
- **State 4:**
    
    - $Q(4, \text{Stop})$: $1 \cdot [R(4, \text{Stop}, \text{Done}) + V^{\pi_0}(\text{Done})] = 1 \cdot [4 + 0] = \mathbf{4}$
        
    - $Q(4, \text{Move})$: $1 \cdot [0 + V^{\pi_0}(\text{Done})] = \mathbf{0}$
        
    - _Best: $\text{Stop}$_
        
- **State 5:**
    
    - $Q(5, \text{Stop})$: $1 \cdot [R(5, \text{Stop}, \text{Done}) + V^{\pi_0}(\text{Done})] = 1 \cdot [5 + 0] = \mathbf{5}$
        
    - $Q(5, \text{Move})$: $1 \cdot [0 + V^{\pi_0}(\text{Done})] = \mathbf{0}$
        
    - _Best: $\text{Stop}$_
        

**New Policy $\pi_1 = \{\text{Move}, \text{Stop}, \text{Stop}, \text{Stop}, \text{Stop}\}$**

---

## Iteration 2: $\pi_1 \rightarrow \pi_2$

### Step 2.A: Policy Evaluation for $\pi_1$

We find $V^{\pi_1}$ for $\pi_1 = \{\text{Move}, \text{Stop}, \text{Stop}, \text{Stop}, \text{Stop}\}$. We use a "cold start" (resetting values to 0) as noted in the problem.

- **Initial Values:** $V^{\pi_1}_0 = \{0, 0, 0, 0, 0\}$
    
- **Calculate $V^{\pi_1}_1$ (using $V^{\pi_1}_0$):**
    
    - $V^{\pi_1}_1(0)$ [Move]: $(1/3)[0 + V^{\pi_1}_0(2)] + (1/3)[0 + V^{\pi_1}_0(3)] + (1/3)[0 + V^{\pi_1}_0(4)] = (1/3)[0] + (1/3)[0] + (1/3)[0] = \mathbf{0}$
        
    - $V^{\pi_1}_1(2)$ [Stop]: $1 \cdot [R(2, \text{Stop}, \text{Done}) + V^{\pi_1}_0(\text{Done})] = 1 \cdot [2 + 0] = \mathbf{2}$
        
    - $V^{\pi_1}_1(3)$ [Stop]: $1 \cdot [R(3, \text{Stop}, \text{Done}) + V^{\pi_1}_0(\text{Done})] = 1 \cdot [3 + 0] = \mathbf{3}$
        
    - $V^{\pi_1}_1(4)$ [Stop]: $1 \cdot [R(4, \text{Stop}, \text{Done}) + V^{\pi_1}_0(\text{Done})] = 1 \cdot [4 + 0] = \mathbf{4}$
        
    - $V^{\pi_1}_1(5)$ [Stop]: $1 \cdot [R(5, \text{Stop}, \text{Done}) + V^{\pi_1}_0(\text{Done})] = 1 \cdot [5 + 0] = \mathbf{5}$
        
    - **Result $V^{\pi_1}_1$:** $\{0, 2, 3, 4, 5\}$
        
- **Calculate $V^{\pi_1}_2$ (using $V^{\pi_1}_1$):**
    
    - $V^{\pi_1}_2(0)$ [Move]: $(1/3)[0 + V^{\pi_1}_1(2)] + (1/3)[0 + V^{\pi_1}_1(3)] + (1/3)[0 + V^{\pi_1}_1(4)] = (1/3)[2] + (1/3)[3] + (1/3)[4] = 9/3 = \mathbf{3}$
        
    - $V^{\pi_1}_2(2)$ [Stop]: $1 \cdot [2 + V^{\pi_1}_1(\text{Done})] = \mathbf{2}$
        
    - $V^{\pi_1}_2(3)$ [Stop]: $1 \cdot [3 + V^{\pi_1}_1(\text{Done})] = \mathbf{3}$
        
    - $V^{\pi_1}_2(4)$ [Stop]: $1 \cdot [4 + V^{\pi_1}_1(\text{Done})] = \mathbf{4}$
        
    - $V^{\pi_1}_2(5)$ [Stop]: $1 \cdot [5 + V^{\pi_1}_1(\text{Done})] = \mathbf{5}$
        
    - **Result $V^{\pi_1}_2$:** $\{3, 2, 3, 4, 5\}$
        
    
    > **Note:** The table provided in your question has a typo. It lists $V^{\pi_1}_2$ as $\{3, 3, 3, 4, 5\}$. The value for state 2, $V(2)$, under a "Stop" policy must be 2, as it's a terminal action with reward 2.
    
- **Calculate $V^{\pi_1}_3$ (using $V^{\pi_1}_2$):**
    
    - $V^{\pi_1}_3(0)$ [Move]: $(1/3)[0 + V^{\pi_1}_2(2)] + (1/3)[0 + V^{\pi_1}_2(3)] + (1/3)[0 + V^{\pi_1}_2(4)] = (1/3)[2] + (1/3)[3] + (1/3)[4] = 9/3 = \mathbf{3}$
        
    - (All other states remain the same as they are terminal)
        
    - **Result $V^{\pi_1}_3$:** $\{3, 2, 3, 4, 5\}$
        
- **Evaluation Converged:** $V^{\pi_1} = \{3, 2, 3, 4, 5\}$.
    

### Step 2.B: Policy Improvement to find $\pi_2$

Now we find the best action for each state using the converged $V^{\pi_1} = \{3, 2, 3, 4, 5\}$.

- **State 0:**
    
    - $Q(0, \text{Stop})$: $1 \cdot [0 + V^{\pi_1}(\text{Done})] = \mathbf{0}$
        
    - $Q(0, \text{Move})$: $(1/3)[0 + V^{\pi_1}(2)] + (1/3)[0 + V^{\pi_1}(3)] + (1/3)[0 + V^{\pi_1}(4)] = (1/3)[2] + (1/3)[3] + (1/3)[4] = 9/3 = \mathbf{3}$
        
    - _Best: $\text{Move}$_
        
- **State 2:**
    
    - $Q(2, \text{Stop})$: $1 \cdot [R(2, \text{Stop}, \text{Done}) + V^{\pi_1}(\text{Done})] = 1 \cdot [2 + 0] = \mathbf{2}$
        
    - $Q(2, \text{Move})$: $(1/3)[0 + V^{\pi_1}(4)] + (1/3)[0 + V^{\pi_1}(5)] + (1/3)[0 + V^{\pi_1}(\text{Done})] = (1/3)[4] + (1/3)[5] + (1/3)[0] = 9/3 = \mathbf{3}$
        
    - _Best: $\text{Move}$_
        
- **State 3:**
    
    - $Q(3, \text{Stop})$: $1 \cdot [R(3, \text{Stop}, \text{Done}) + V^{\pi_1}(\text{Done})] = 1 \cdot [3 + 0] = \mathbf{3}$
        
    - $Q(3, \text{Move})$: $(1/3)[0 + V^{\pi_1}(5)] + (2/3)[0 + V^{\pi_1}(\text{Done})] = (1/3)[5] + (2/3)[0] = \mathbf{5/3}$
        
    - _Best: $\text{Stop}$_
        
- **State 4:**
    
    - $Q(4, \text{Stop})$: $1 \cdot [R(4, \text{Stop}, \text{Done}) + V^{\pi_1}(\text{Done})] = 1 \cdot [4 + 0] = \mathbf{4}$
        
    - $Q(4, \text{Move})$: $1 \cdot [0 + V^{\pi_1}(\text{Done})] = \mathbf{0}$
        
    - _Best: $\text{Stop}$_
        
- **State 5:**
    
    - $Q(5, \text{Stop})$: $1 \cdot [R(5, \text{Stop}, \text{Done}) + V^{\pi_1}(\text{Done})] = 1 \cdot [5 + 0] = \mathbf{5}$
        
    - $Q(5, \text{Move})$: $1 \cdot [0 + V^{\pi_1}(\text{Done})] = \mathbf{0}$
        
    - _Best: $\text{Stop}$_
        

**New Policy $\pi_2 = \{\text{Move}, \text{Move}, \text{Stop}, \text{Stop}, \text{Stop}\}$**

---

## Final Result Summary

Here is the completed table with the typo from the original problem corrected (in bold).

|**States**|**0**|**2**|**3**|**4**|**5**|
|---|---|---|---|---|---|
|**$\pi_0$**|**Move**|**Stop**|**Move**|**Stop**|**Move**|
|$V^{\pi_0}_0$|0|0|0|0|0|
|$V^{\pi_0}_1$|0|2|0|4|0|
|$V^{\pi_0}_2$|2|2|0|4|0|
|$V^{\pi_0}_3$|2|2|0|4|0|
|**$\pi_1$**|**Move**|**Stop**|**Stop**|**Stop**|**Stop**|
|$V^{\pi_1}_0$|0|0|0|0|0|
|$V^{\pi_1}_1$|0|2|3|4|5|
|$V^{\pi_1}_2$|3|**2**|3|4|5|
|$V^{\pi_1}_3$|3|2|3|4|5|
|**$\pi_2$**|**Move**|**Move**|**Stop**|**Stop**|**Stop**|

You can see that $\pi_2$ matches the optimal policy $\pi^*$ found using value iteration in part (d).


---
# Question 2 : 
![[undefined - Imgur.jpg]]

---
# Question 3 : 

![[Pasted image 20251107004229.png]]
# Question 4 : 