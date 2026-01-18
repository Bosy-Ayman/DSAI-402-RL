### Questions collected from these links:

**Cairo University RL Drive 1 :** https://drive.google.com/drive/folders/1dkEfcOpsroXeU-nCaPn-hlr8y6nWuiaz 

**Cairo University RL Drive 2 :**  https://drive.google.com/drive/folders/1WiGlKSzJ0wviSWu25eHqLLJoK1jqkWkh 

[sarsa,qleaning Numerical example - Google Drive](https://drive.google.com/drive/u/0/folders/1huJegZPq0f6htsYAi7DpKIunNWKuhiXE)

https://www.cs.cmu.edu/~15281-s20/recitations/rec9/rec9_sol.pdf --> it include TD and sarsa
# Question 1 

**Solved here :** https://www.youtube.com/watch?v=2sisptKZils&list=PLxoZxAo3dSLJ_OJOA8hmuoMmHlblXLyzf&index=16&t=249s (10 min)

![Question 1](components/recap1.png)
![Question1](components/after_mid.png)



---
# Question 2
![Question 2](components/recap3.png)

---
# Question 3 - Monte Carlo
![Question 3](components/question_mc.png)

---
# Question 4 : 
Briefly explain the insights observed in the below graph:
![graph](components/graph.png)

Answer [2 Points]:
The figure demonstrates the effect of exploration vs. exploitation.

==When ε = 0, t==he average reward being plateaued (i.e., almost constant)

==As ε is increased from 0 → 0.1==, the average reward starts to increase as the agent can randomly
choose actions that can offer better rewards instead of being limited to its experience.

==As ε is increased from 0.01 → 0.1==, the rate of increase is better as the agent can find better
reward in less number of steps compared to 0.01.


---
# Question 6: Theoretical
**b. In the ε-greedy action selection method, and for the case of two actions and ε = 0.25, what
is the probability that the greedy action is selected? Elaborate on your answer.
Answer [2 Points]:**

Total = 0.75+ 0.125 = 0.875
The Probability of choosing the greedy action: 1- ε = 0.75 [1 Point]
The probability of choosing the greedy action but randomly is ε * (1⁄2) = 0.25*0.5 = 0.125
[1 Point] Note (1⁄2) since we only have 2 actions

**c. What is the purpose of using the discount factor ‘γ’ when estimating returns in an MDP?
Is it necessary for all types of RL problems and why?**
Answer [2 Points]:

Problems with finite episodes can be solved without a discount factor, but problems with
infinite episodes must use a discount factor so we can have a bounded cumulative reward.
Hence, it is not mandatory in all cases but it simplifies equations by formulating solution
that can work in all cases.

**b. In ε-greedy action selection, for the case of two actions and ε = 0.5, what is the
probability that the greedy action is selected? Explain your answer.**

derivation
0.5 probability derived of choosing the greedy action, which is 1-ε
= 1-0.5 = 0.5
0.25% chance derived of being chosen as the random option with
ε= 0.5x0.5=0.25
The probability is 0.5+0.25 = 0.75

**Whats the main shortcoming of TD learning that Q-learning resolves?**
TD value learning provides a value for each state for a given policy . It is impossible to get the optimal policy directly from the learned values because the state values are learned for the given policy . And if we want to follow policy iteration to extract an improved policy from these values, we would need to use the R and T functions (which we dont have). With Q-learning, we can get values of Q-states (i.e., (state, action) pairs) of the optimal policy, from which we can extract an optimal policy simply by taking the action corresponding to the maximum Q-value from each state.

---
# Question 7 : TD n step

![Question](components/nstep.png)
![answer](components/nstepanswer.png)

---
# Question 8: TD n step
![N step](components/nstep2.png)
---
# Question 9 : SARSA / N Step SARSA / Q learning


## Part 1: The Setup (Shared Environment)

To clearly see the difference between Q-Learning and SARSA, we assume some learning has already happened.

**Parameters:**

- **Discount Factor (**$\gamma$**):** $0.9$
    
- **Learning Rate (**$\alpha$**):** $0.5$
    
- **Exploration (**$\epsilon$**):** $0.1$ (10% chance to explore)
    

**The Scenario:** We are at State **A**.

- **Action Right** leads to State **B** (Reward = 0).
    
- From State **B**, there are two known paths:
    
    - **Action Best:** leads to $+50$ reward ($Q(B, \text{Best}) = 50$).
        
    - **Action Bad:** leads to $-10$ reward ($Q(B, \text{Bad}) = -10$).
        

**Current Q-Values:**

- $Q(A, \text{Right}) = 10$ (Current estimate)
    
- $Q(B, \text{Best}) = 50$
    
- $Q(B, \text{Bad}) = -10$
    

## Part 2: Q-Learning (Off-Policy)

**Concept:** Q-Learning assumes you will act _optimally_ in the next state, even if you are currently exploring or making mistakes. It is "optimistic."

**The Episode Step:**

1. We are at **A**. We choose **Right**.
    
2. We arrive at **B**. Reward $R = 0$.
    
3. **Crucial Moment:** Q-Learning looks at State B and asks, _"What is the max value possible here?"_
    

**The Math:**

$$Q(S, A) \leftarrow Q(S, A) + \alpha [ R + \gamma \max_{a'} Q(S', a') - Q(S, A) ]$$

Substitute values for updating $Q(A, \text{Right})$:

1. **Max Future Value:** $\max(50, -10) = 50$.
    
2. **TD Target:** $0 + 0.9(50) = 45$.
    
3. **TD Error:** $45 - 10 = 35$.
    
4. **Update:** $10 + 0.5(35) = 27.5$.
    

**New** $Q(A, \text{Right}) = 27.5$ _(Note: The value increased because it assumes we will take the "Best" action next.)_

## Part 3: SARSA (On-Policy)

**Concept:** SARSA learns from the _actual_ path taken. If the agent explores and picks a bad action, SARSA effectively says, _"This path leads to a mistake, so the previous state is less valuable."_

**The Episode Step:**

1. We are at **A**. We choose **Right**.
    
2. We arrive at **B**. Reward $R = 0$.
    
3. **Crucial Moment:** Because of $\epsilon$-greedy (exploration), the agent decides to pick **Action Bad** for the next step.
    

**The Math:**

$$Q(S, A) \leftarrow Q(S, A) + \alpha [ R + \gamma Q(S', A') - Q(S, A) ]$$

Substitute values for updating $Q(A, \text{Right})$:

1. **Actual Future Value:** We picked "Bad", so we use $Q(B, \text{Bad}) = -10$.
    
2. **TD Target:** $0 + 0.9(-10) = -9$.
    
3. **TD Error:** $-9 - 10 = -19$.
    
4. **Update:** $10 + 0.5(-19) = 0.5$.
    

**New** $Q(A, \text{Right}) = 0.5$ _(Note: The value dropped significantly because the agent actually plans to take the "Bad" action next.)_

## Part 4: Exam Question (n-step SARSA)

**Question:** You are given the following 3-step trajectory taken by an agent. Calculate the **2-step SARSA** update for the starting state $S_0$.

**Trajectory:**

$$S_0 \xrightarrow{A_0} R_1=2 \xrightarrow{} S_1 \xrightarrow{A_1} R_2=5 \xrightarrow{} S_2 \xrightarrow{A_2} \dots$$

**Given:**

- $Q(S_0, A_0) = 3$
    
- $Q(S_1, A_1) = 4$
    
- $Q(S_2, A_2) = 10$
    
- $\gamma = 0.9$
    
- $\alpha = 0.1$
    

**Solution:**

**Step 1: Calculate the n-step Return (**$G_t^{(n)}$**)** For $n=2$, we sum the rewards for 2 steps, then bootstrap from the Q-value at the 3rd state ($S_2$).

$$G_0^{(2)} = R_1 + \gamma R_2 + \gamma^2 Q(S_2, A_2)$$$$G_0^{(2)} = 2 + 0.9(5) + 0.9^2(10)$$$$G_0^{(2)} = 2 + 4.5 + 0.81(10)$$$$G_0^{(2)} = 2 + 4.5 + 8.1$$$$G_0^{(2)} = 14.6$$

**Step 2: Apply the Update Rule**

$$Q(S_0, A_0) \leftarrow Q(S_0, A_0) + \alpha [ G_0^{(2)} - Q(S_0, A_0) ]$$$$Q(S_0, A_0) \leftarrow 3 + 0.1 [ 14.6 - 3 ]$$$$Q(S_0, A_0) \leftarrow 3 + 0.1 [ 11.6 ]$$$$Q(S_0, A_0) \leftarrow 3 + 1.16$$

**Final Answer:** $Q(S_0, A_0) = 4.16$

## Summary Cheat Sheet

|Feature|Q-Learning|SARSA|n-step SARSA|
|---|---|---|---|
|**Equation**|$R + \gamma \max Q(S', a')$|$R + \gamma Q(S', A')$|$R_1 + \dots + \gamma^n Q(S_{t+n}, A_{t+n})$|
|**Bootstrap**|Immediate (1-step)|Immediate (1-step)|Delayed (n-steps)|
|**Policy**|Off-Policy (optimistic)|On-Policy (realistic)|On-Policy|
|**Updates**|Even if you act randomly, it learns the optimal path.|If you act randomly, it learns the random path.|Needs to wait $n$ steps to update.|
