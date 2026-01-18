
### **Question 1: Bellman Equations & Value Functions (15 pts)**

Consider the following deterministic MDP with 2 states: `S = {s₀, s₁}` and actions `A = {a₁, a₂}`. The transition and reward functions are:

| Current State | Action | Next State | Reward |
|---------------|--------|------------|--------|
| s₀            | a₁     | s₁         | +2     |
| s₀            | a₂     | s₀         | 0      |
| s₁            | a₁     | s₁         | -1     |
| s₁            | a₂     | s₀         | +1     |

Let policy π be stochastic: π(a₁|s₀) = 0.5, π(a₂|s₀) = 0.5, π(a₁|s₁) = 0.8, π(a₂|s₁) = 0.2. Discount factor γ = 0.9.

**(a) [5 pts]** Write the Bellman equation for vπ(s). Define each term clearly.

**(b) [7 pts]** Compute vπ(s₀) and vπ(s₁) using the Bellman equation. Assume initial values v₀(s₀) = 0, v₀(s₁) = 0. Perform **one iteration** of policy evaluation (i.e., compute v₁(s₀) and v₁(s₁)).

**(c) [3 pts]** Show that vπ(s) = Σₐ π(a|s) qπ(s,a) holds for state s₀.

---

### **Question 2: Policy Evaluation & Improvement (20 pts)**

You are interacting with a simplified vending machine MDP (from Lecture 4). There are 2 states:
- `s`: Start state (no selection made)
- `t`: Terminal state (after dispensing snack)

Actions: Press **A** (Biscoff, reward +1), Press **B** (Doritos, reward +2), Press **C** (Galaxy, reward +3). Pressing any button transitions deterministically to terminal state `t`.

Current stochastic policy: π(A|s) = 0.2, π(B|s) = 0.3, π(C|s) = 0.5. Assume γ = 1.0, and v(t) = 0.

**(a) [8 pts]** Compute vπ(s) using the **policy evaluation** update. Show the complete summation.

**(b) [8 pts]** Now perform **policy improvement**. For each action a ∈ {A, B, C}, compute qπ(s, a) and derive the new improved policy π'(s) = argmaxₐ qπ(s, a).

**(c) [4 pts]** Is π' better than π? Justify your answer using the policy improvement theorem (no formal proof required, just logical reasoning).

---

### **Question 3: Value Iteration (20 pts)**

Consider a 3×3 grid world (modified from Lecture 4's 4×4 example). The agent starts at top-left, terminal states are bottom-right (shaded). Rewards: -1 for each transition. Undiscounted (γ = 1), episodic. Actions: Up, Down, Left, Right (deterministic).

```
┌────┬────┬────┐
│ S₀ │ S₁ │ S₂ │
├────┼────┼────┤
│ S₃ │ S₄ │ S₅ │
├────┼────┼────┤
│ S₆ │ S₇ │ S₈ │ (Terminal)
└────┴────┴────┘
```

**(a) [12 pts]** Perform **value iteration** for k = 0, 1, and 2. Show the value function vₖ(s) for each non-terminal state. Initialize v₀(s) = 0 for all states.

**(b) [5 pts]** After convergence, extract the optimal policy π*(s) for states S₀, S₁, and S₃ by computing:
π*(s) = argmaxₐ Σₛ' p(s'|s,a)[r(s,a,s') + γv*(s')].

**(c) [3 pts]** Explain **why** value iteration converges to the optimal value function v*(s) even though we never explicitly evaluate a fixed policy.

---

### **Question 4: Monte Carlo Estimation (25 pts)**

You have the following three episodes from an unknown MDP. Assume γ = 1.0 and first-visit MC estimation:

**Episode 1:** S₀, +3, S₁, +2, S₂, -1, Terminal  
**Episode 2:** S₁, +4, S₀, +1, S₂, +2, Terminal  
**Episode 3:** S₀, +2, S₀, +3, S₁, +1, S₂, -2, Terminal

**(a) [18 pts]** Compute the **first-visit Monte Carlo** estimate for v(s) for states S₀, S₁, and S₂ after **all three episodes**. Show:
- The return G for each state's first appearance in each episode
- The running average after each episode

**(b) [5 pts]** Briefly describe how you would modify the algorithm to perform **every-visit** MC estimation instead. What would change in the calculation for v(S₀) in Episode 3?

**(c) [2 pts]** Why must we estimate q(s,a) in model-free methods instead of just v(s)? State the key limitation that prevents using v(s) alone.

---

### **Question 5: Conceptual Design & Comparison (20 pts)**

**(a) [8 pts]** Compare **Model-based** (Dynamic Programming) vs **Model-free** (Monte Carlo) methods across three dimensions:
1. Information required to start learning
2. How they compute expectations
3. Computational efficiency and sample complexity

**(b) [7 pts]** Dr. Ghalwash mentioned "Issues in Policy Iteration" in Lecture 5. List **two practical problems** with policy iteration and explain how **value iteration** addresses these issues.

**(c) [5 pts]** Design an MDP for a **robot delivery task**:
- Define **states**, **actions**, **rewards** (be specific, e.g., reward values)
- Explain how your design handles the exploration-exploitation tradeoff in a model-free setting.

---

## **Answer Key & Grading Rubric**

### **Q1: Bellman Equations**

**(a) [5 pts]**
vπ(s) = Σₐ π(a|s) Σₛ' p(s'|s,a)[r(s,a,s') + γ vπ(s')]  
- vπ(s): Expected return starting from state s under policy π
- π(a|s): Probability of taking action a in state s
- p(s'|s,a): Transition probability
- r(s,a,s'): Immediate reward
- γ: Discount factor

**(b) [7 pts]**
v₁(s₀) = 0.5 × (2 + 0.9×0) + 0.5 × (0 + 0.9×0) = **1.0**  
v₁(s₁) = 0.8 × (-1 + 0.9×0) + 0.2 × (1 + 0.9×0) = **-0.6**

**(c) [3 pts]**
qπ(s₀,a₁) = 2 + γv(s₁) = 2 + 0.9×0 = 2  
qπ(s₀,a₂) = 0 + γv(s₀) = 0  
Σₐ π(a|s₀)qπ(s₀,a) = 0.5×2 + 0.5×0 = 1 = vπ(s₀) ✓

---

### **Q2: Policy Evaluation & Improvement**

**(a) [8 pts]**
vπ(s) = 0.2 × (1 + 0) + 0.3 × (2 + 0) + 0.5 × (3 + 0) = 0.2 + 0.6 + 1.5 = **2.3**

**(b) [8 pts]**
qπ(s,A) = 1, qπ(s,B) = 2, qπ(s,C) = 3  
π'(s) = **C** (Press C) → deterministic policy

**(c) [4 pts]**
Yes, π' is better. For state s, qπ(s,π'(s)) = 3 > vπ(s) = 2.3. By policy improvement theorem, vπ'(s) ≥ vπ(s) for all s.

---

### **Q3: Value Iteration**

**(a) [12 pts]**
k=0: All non-terminal states = 0

k=1:
- v₁(S₀) = max{-1+0, -1+0} = **-1** (down or right)
- v₁(S₁) = max{-1+0, -1+0, -1+0} = **-1**
- v₁(S₃) = max{-1+0, -1+0} = **-1**

k=2:
- v₂(S₀) = max{-1+v₁(S₃), -1+v₁(S₁)} = max{-2, -2} = **-2**
- v₂(S₁) = max{-1+v₁(S₂)(-2), -1+v₁(S₄)(-2), -1+v₁(S₀)(-1)} = **-2**
- v₂(S₃) = max{-1+v₁(S₆)(-1), -1+v₁(S₄)(-2)} = **-2**

**(b) [5 pts]**
After convergence: v*(S₀)=-4, v*(S₁)=-3, v*(S₃)=-3  
π*(S₀)=Right, π*(S₁)=Right, π*(S₃)=Down

**(c) [3 pts]**
Value iteration directly updates v(s) using the Bellman optimality operator (max). This operator is a contraction mapping, guaranteeing convergence to the unique fixed point v* without needing to evaluate intermediate policies.

---

### **Q4: Monte Carlo Estimation**

**(a) [18 pts]**
**Episode 1**: S₀ first appears at t=0 → G = 3+2-1 = **4**  
**Episode 2**: S₀ first appears at t=1 → G = 1+2 = **3**  
**Episode 3**: S₀ first appears at t=0 → G = 2+3+1-2 = **4**

v(S₀) after 3 episodes: (4 + 3 + 4)/3 = **3.67**

**Episode 1**: S₁ first appears at t=1 → G = 2-1 = **1**  
**Episode 2**: S₁ first appears at t=0 → G = 4+1+2 = **7**  
**Episode 3**: S₁ first appears at t=2 → G = 1-2 = **-1**

v(S₁) after 3 episodes: (1 + 7 + -1)/3 = **2.33**

**Episode 1**: S₂ first appears at t=2 → G = -1 = **-1**  
**Episode 2**: S₂ first appears at t=2 → G = 2 = **2**  
**Episode 3**: S₂ first appears at t=3 → G = -2 = **-2**

v(S₂) after 3 episodes: (-1 + 2 + -2)/3 = **-0.33**

**(b) [5 pts]**
Every-visit MC averages returns following **all** visits to each state. In Episode 3, S₀ appears twice (t=0 and t=2). We would compute separate returns for each visit: G(t=0)=4 and G(t=2)=1-2=-1, then include both in the average.

**(c) [2 pts]**
Without a model, we cannot compute the transition probabilities p(s'|s,a) needed to look ahead and select actions from v(s) alone. We need q(s,a) to evaluate actions directly.

---

### **Q5: Conceptual Design**

**(a) [8 pts]**
1. **Info required**: Model-based needs p(s'|s,a) and r(s,a,s'); Model-free only needs experience samples.
2. **Expectations**: Model-based computes via summation; Model-free approximates by averaging sampled returns.
3. **Efficiency**: DP is computationally heavy per iteration but sample-efficient; MC is computationally light per episode but needs many samples.

**(b) [7 pts]**
1. **Problem**: Policy iteration requires full policy evaluation to convergence before improvement, which is slow.  
   **Solution**: Value iteration interleaves evaluation and improvement in each sweep.

2. **Problem**: Policy iteration requires solving a system of linear equations (expensive).  
   **Solution**: Value iteration uses simple iterative updates.

**(c) [5 pts]**
**States**: {At hub, Delivering, At destination}  
**Actions**: {Choose route A, B, C}  
**Rewards**: +10 for successful delivery, -1 per time step, -5 for traffic  
**Exploration**: Use ε-greedy: with probability ε try random routes to discover faster ones, otherwise exploit current best route via q(s,a).

---

**End of Exam**