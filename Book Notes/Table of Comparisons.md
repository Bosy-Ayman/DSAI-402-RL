
| Parameter         | Symbol | Scope / Algorithm | Range / Default | Description                                                                                                                                   |
| ----------------- | ------ | ----------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Discount Factor   | γ      | Global            | 0.1 – 0.99      | Determines the importance of future rewards. Higher values (e.g. 0.99) encourage long-term planning; lower values focus on immediate rewards. |
| Training Episodes | N      | Model-Free        | 100 – 50,000    | Total number of episodes the agent interacts with the environment to learn a policy.                                                          |
| Learning Rate     | α      | TD / Q-Learning   | 0.01 – 1.0      | Controls how much new information overrides old information. α = 0 means no learning; α = 1 uses only the latest information.                 |
| Epsilon           | ε      | ε-Greedy          | 0.0 – 1.0       | Controls exploration vs. exploitation. Probability of taking a random action to explore new states.                                           |
| Convergence Theta | θ      | Model-Based (DP)  | 1e-6 (default)  | Stopping threshold for Value / Policy Iteration. Training stops when ΔV < θ.                                                                  |

# RL Parameters & Algorithm Complexity

## Parameter Impact Analysis

|Parameter|Change|Impact|Convergence|Best For|
|---|---|---|---|---|
|**Discount Factor (γ)**|↑ Increase (→ 0.99)|Long-term planning, values future rewards. Useful for sequential decision-making (navigation, games). Can lead to instability if environment is stochastic.|Slower convergence, requires more episodes|Navigation, games, long-horizon tasks|
||↓ Decrease (→ 0.1)|Myopic behavior, focuses on immediate rewards. Ignores future consequences.|Faster convergence, fewer episodes needed|Immediate reward tasks|
|**Learning Rate (α)**|↑ Increase (→ 1.0)|Fast updates, learns quickly from recent experiences. High variance, oscillations, may diverge. Previous knowledge discarded.|Fast but unstable|Non-stationary environments (risky)|
||↓ Decrease (→ 0.01)|Stable learning, smooth convergence, averages out noise. Requires many episodes to converge. Previous knowledge heavily weighted.|Slow but stable|Noisy/stochastic environments|
|**Epsilon (ε)**|↑ Increase (→ 1.0)|Pure exploration, takes random actions. Discovers all states. Avoids local optima, samples diverse trajectories. Inefficient, suboptimal rewards.|High variance, slow convergence|Initial exploration phase|
||↓ Decrease (→ 0.0)|Pure exploitation, exploits current best policy. High immediate rewards if policy is good. Gets stuck in local optima.|Fast convergence (local)|Exploitation phase, known good policy|
|**Training Episodes (N)**|↑ Increase (→ 50K)|Better convergence, more time to explore and refine. Discovers complex patterns, more stable final policy. Computational overhead.|Exponential improvement|Complex environments, optimal solutions|
||↓ Decrease (→ 100)|Fast training, quick feedback. Incomplete learning, poor policy, high variance.|Quick but suboptimal|Quick prototyping, simple environments|
|**Convergence Theta (θ)**|↑ Increase (→ 1e-3)|Early stopping, loose convergence criterion. Faster execution, reduced computation. Suboptimal value function.|Fast but loose|Quick approximations|
||↓ Decrease (→ 1e-9)|Strict convergence, tight criterion. Waits for true convergence. Optimal value function. More iterations needed.|Slow but optimal|High-precision solutions|


---

## Algorithm Complexity Analysis

|Algorithm|Type|Time Complexity|Space Complexity|Convergence Rate|Scalability|
|---|---|---|---|---|---|
|Value Iteration|Model-Based DP|O(k\|S\|²\|A\|)|O(\|S\|)|Exponential (1-γ)^k|Poor|
|Policy Iteration|Model-Based DP|O(m·\|S\|²\|A\| + \|S\|²)|O(\|S\|)|Typically faster than VI|Poor|
|Q-Learning|Model-Free (TD)|O(N·L·\|S\|·\|A\|)|O(\|S\|·\|A\|)|O(1/t) - slow|Moderate|
|SARSA|Model-Free (TD)|O(N·L·\|S\|·\|A\|)|O(\|S\|·\|A\|)|O(1/t) - slow|Moderate|
|TD(0)|Model-Free (TD)|O(N·L·\|S\|)|O(\|S\|)|O(1/t) - slow|Moderate|
|TD(n-step)|Model-Free (TD)|O(N·L·\|S\|)|O(\|S\|)|O(1/t) - varies with n|Moderate|
|Monte Carlo (First-Visit)|Model-Free (MC)|O(N·L)|O(\|S\|)|O(1/√N) - medium|Good|
|Monte Carlo (Every-Visit)|Model-Free (MC)|O(N·L²)|O(\|S\|)|O(1/√N) - medium|Good|
|DQN|Deep Model-Free|O(N·L·\|forward pass\|)|O(\|replay buffer\|)|Variable|Excellent|

### Notation Legend

- **N** = number of episodes/samples
- **L** = trajectory length
- **|S|** = number of states
- **|A|** = number of actions
- **d** = feature/parameter dimension
- **k** = number of iterations
- **m** = policy evaluation iterations
- **γ** = discount factor

---

## Algorithm Comparison Matrix

|Algorithm|Model Required?|On/Off-Policy|Tabular/Approximation|Best For|Main Challenge|
|---|---|---|---|---|---|
|Value Iteration|✓ Yes|N/A|Tabular only|Small discrete spaces|Curse of dimensionality|
|Policy Iteration|✓ Yes|N/A|Tabular only|Small discrete spaces|Expensive policy eval|
|Q-Learning|✗ No|Off-policy|Tabular (can approximate)|Discrete control|Slow convergence|
|SARSA|✗ No|On-policy|Tabular (can approximate)|Safe exploration|On-policy inefficiency|
|TD(0)|✗ No|On-policy|Tabular (can approximate)|Continuous online learning|Bias from bootstrapping|
|TD(n-step)|✗ No|On-policy (off-policy variant)|Tabular (can approximate)|Balancing MC and TD|n-step selection crucial|
|Monte Carlo (First-Visit)|✗ No|On-policy|Tabular|Episodic problems, unbiased|High variance|
|Monte Carlo (Every-Visit)|✗ No|On-policy|Tabular|Better data efficiency|Biased, higher variance|
|DQN|✗ No|Off-policy|Neural networks|High-dim observations|Non-stationarity|

---

## Quick Parameter Tuning Guide

**Long-horizon Navigation**

- **Parameters:** γ=0.95-0.99, α=0.1, ε=0.1, N=10K+
- **Reasoning:** Far-sighted planning, stable learning, moderate exploration

**Quick Prototyping**

- **Parameters:** γ=0.9, α=0.5, ε=0.2, N=1K
- **Reasoning:** Fast convergence prioritized over optimality

**Stochastic Environment**

- **Parameters:** γ=0.95, α=0.05-0.1, ε=0.15-0.2, N=high
- **Reasoning:** Low α for noise averaging, higher N for stability

**Safe Exploration (Robotics)**

- **Parameters:** γ=0.95, α=0.01-0.05, ε=0.05, N=very high
- **Reasoning:** Conservative approach: low ε prevents dangerous exploration

**Model-Based DP**

- **Parameters:** θ=1e-6, γ=0.99
- **Reasoning:** Tight convergence for exact solution

---

## Key Insights

### TD vs MC vs DP

**Dynamic Programming (VI, PI):** Requires model, offline computation, exact solutions

**Temporal Difference (TD, Q-Learning, SARSA):** Model-free, online learning, bootstrapping (low variance, high bias)

**Monte Carlo:** Model-free, episodic, unbiased (high variance, low bias)

**TD(n-step):** Bridges TD and MC - adjust n to balance bias-variance tradeoff

### Bias-Variance Tradeoff

- **Higher bias, low variance:** TD(0), bootstrapping methods
- **Low bias, high variance:** Monte Carlo, full-episode returns
- **Balanced:** TD(n-step) with appropriate n selection

### Convergence Guarantees

- **Model-Based:** Guaranteed convergence with proper parameter selection
- **Q-Learning:** Off-policy, converges to optimal despite policy changes
- **SARSA:** On-policy, converges but to policy-dependent value function
- **Monte Carlo:** Converges but needs complete episodes
- **TD(0):** Fast convergence but less sample efficient than MC