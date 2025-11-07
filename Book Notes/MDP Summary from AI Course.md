https://radical-cream-bc9.notion.site/Markov-Decision-Process-MDP-f9cd61af3c514168bc3ff4d16cbd3358
# Markov Decision Process (MDP)

Important Note: The equations in these notes are written in terms of $R(s, a, s')$, while the slides use $R(s)$, so they are slightly different .

We are concerned with _**sequential decision problems**_, in which the agent’s _**utility**_ depends on a sequence of decisions.

If the environment were deterministic, a solution would be easy. Unfortunately, the environment won’t always go along with our solution, because the actions are unreliable (_**stochastic motion model**_). Each action achieves the intended effect with some probability.

# Grid World Example

- The agent lives in a grid.
- The actions in each state are U_p_, _Down_, _Left_ and _Right_.
- Each action succeeds with probability 0.8, but the rest of the time, the action moves the agent at right angles to the intended direction.
- If the agent bumps into a wall, it stays in the same square

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0a6ccc15-81bf-45cc-b566-a6c17b56b87c/c6590bdd-bb44-4de9-84cf-0c866fa041d8/Untitled.png)

# Formal Definition of MDP

A _**Markov Decision Process**_ or _**MDP**_ is a _**sequential decision**_ problem for a _**stochastic**_, _**fully observable environment**_ with a _**Markovian**_ transition model and _**additive rewards**_.

An MDP consists of:

- A set of _**States**_ $s \in S$ (with an _**initial state**_ $s_0$)
    
- A set of _**Actions**_ in each state $a \in A(s)$
    
- A _**Transition model**_ $P(s' | \ s, a)$
    
    Describes the outcome of each action in each state. Here, the outcome is stochastic, so the transition model is represented as a _**conditional probability distribution**_ of reaching state $s'$ given that action $a$ is done in state $s$.
    
    We will assume that transitions are _**Markovian**_: the probability of reaching $s'$ from $s$ depends only on $s$ and not on the history of earlier states. In probabilistic terms, this is known as _**conditional independence**_.
    
- A _**Reward function**_ $R(s, a, s')$
    
    For every transition from $s$ to $s'$ via action $a$, the agent receives a reward $R(s, a, s')$. The rewards may be positive or negative.
    
    Sometimes rewards depend only on a given state regardless of how this state was reached. In other words, $R(s)$ is the reward for being in state $s$.
    
- A Utility function $U$ Because the decision problem is sequential, the utility function will depend on a sequence of states and actions—an _**environment history**_—rather than on a single state.
    
    For now, the utility of an environment history is just the sum of the rewards received.
    

# Policy

In MDP, no fixed action sequence can solve the problem, because the environment is stochastic, thus the agent might end up in a state other than the goal.

Therefore, a solution must specify what the agent should do for any state that the agent might reach. We call this plan a _**policy**_ denoted $\pi$.

In other words a policy is a function $\pi: S \to A$, where $\pi(s)$ is the action recommended by the policy $\pi$ for state s.

No matter what the outcome of the action, the resulting state will be in the policy, and the agent will know what to do next.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0a6ccc15-81bf-45cc-b566-a6c17b56b87c/2b7c68c2-4328-4ac6-9a35-4ada5c72ca4c/Untitled.png)

A policy represents the _**agent function**_ explicitly and is therefore a description of a simple reflect agent. However, the computation of the policy itself involves a utility-based agent.

## Finite Horizons VS Infinite Horizons

A _**finite horizon**_ means that there is a fixed time $N$ after which nothing matters—the game is over, so to speak. In an _**infinite horizon**_ there is no fixed deadline (note that this does not necessarily mean that all state sequences are infinite).

With a finite horizon, an optimal action in a given state may depend on how much time is left. A policy that depends on the time is called _**nonstationary**_.

With no fixed time limit there is no reason to behave differently in the same state at different times. Hence, an optimal action depends only on the current state, and the optimal policy is _**stationary**_.

# Utilities Over Time

The obvious naïve definition of the utility function for a given environment history $h = s_0, a_0, s_1, a_1, \dots$ is just the sum of rewards received. That is,

$$ U([s_0, a_0, s_1, a_1, \dots]) = R(s_0, a_0, s_1) + R(s_1, a_1, s_2) + \dots $$

We call this additive reward. The intuition is that we would like to maximize the sum of rewards

Would you rather have $10M$ after $10$ months or $1M$ for $9$ moths?

We tend to prefer immediate rewards over long-term possibly larger rewards, especially in environments where resources are scarce or unpredictable.

We would like to model the same phenomena in calculating the utility of an agent in MDP.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0a6ccc15-81bf-45cc-b566-a6c17b56b87c/749ea9b2-737e-4da7-abf1-08808f040638/Untitled.png)

We do so by the notion of discounted rewards. The idea is to make rewards decay exponentially with time.

This is known as _**additive discounted rewards**_: the utility of an environment history is defines as

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0a6ccc15-81bf-45cc-b566-a6c17b56b87c/b3928aa3-045e-49d3-9d7f-779ae12bc500/Untitled.png)

```
    1 

Worth 
 Now
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0a6ccc15-81bf-45cc-b566-a6c17b56b87c/97e5977b-383b-4600-995f-f0411d916be3/Untitled.png)

```
    $\\gamma$
```

Worth Next Step

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/0a6ccc15-81bf-45cc-b566-a6c17b56b87c/3528e769-fa09-4970-bea4-ce8e427540bb/Untitled.png)

```
    $\\gamma^2$
```

Worth Two Steps

$$ U([s_0, a_0, s_1, a_1, \dots]) = R(s_0, a_0, s_1) + \gamma R(s_1, a_1, s_2) + \gamma^2R(s_2, a_2, s_3) \dots $$

Where the _**discount factor**_ $\gamma$ is a number between 0 and 1. It describes the preference of an agent for current rewards over future rewards. When $\gamma$ is close to 0, rewards in the distant future are viewed as insignificant. When $\gamma$ is close to 1, an agent is more willing to wait for long-term rewards. When $\gamma$ is exactly 1, discounted rewards reduce to the special case of purely additive rewards.

With infinite horizons there is a potential difficulty: if the environment does not contain a terminal state, or if the agent never reaches one, then environment histories will be infinitely long, and utilities will generally be infinite.

However, with discounted rewards, the utility of an infinite sequence is finite:

$$ U([s_0, a_0, s_1, a_1, \dots]) = \sum_{t=0}^\infty \gamma^t R(s_t, a_t, s_{t+1}) ≤ \sum_{t=0}^\infty \gamma^t R_{max} = \frac {R_{max}} {1-\gamma} $$

# Optimal Policies and Utilities

The quality of a policy is measured by the _**expected utility**_ of the possible environment histories generated by that policy.

To calculate the expected utility of a particular policy $\pi$, we assume the agent is in some initial state $s$ and define a random variable $S_t$ to be the state the agent reaches at time $t$ when executing $\pi$.

The expected utility obtained by executing $\pi$ starting in $s$ is given by:

$$ U_\pi(s) = \mathbb{E}\Bigg[ \sum_{t=0}^\infty \gamma^t R(S_t, \pi(S_t), S_{t+1}) \Bigg] $$

Now, out of all the policies the agent could choose to execute starting in $s$, there’s an optimal policy (possibly more than one) which we denote $\pi^*_s$ and is given by:

$$ \pi^*_s = \argmax_\pi U_\pi(s) $$

In words, the optimal policy starting at initial state $s$ is the one that maximizes the expected utility over the state sequences.

Does the initial state $s$ matter?

A remarkable consequence of using discounted utilities with infinite horizons is that the optimal policy is independent of the starting state (of course, the action sequence won’t be independent).

So regardless of the state $s$, there’s an optimal policy which we denote as $\pi^*$.

Given this definition of optimal policy, the true utility of a state $s$ is just $U^{\pi^*}(s)$—that is, the expected sum of discounted rewards if the agent executes an optimal policy.

Hence, we simply denote the utility of a state $s$ as $U(s)$ which is defined as the maximum expected sum of discounted rewards the agent can obtain starting at $s$.

# Bellman Equation

The utility function $U(s)$ allows the agent to select actions by using the principle of maximum expected utility—that is, choose the action that maximizes the reward for the next step plus the expected discounted utility of the subsequent state:

$$ \boxed{\pi^*(s) = \argmax_{a \in A(s)} \sum_{s'} p(s'|\ s, a) \ [R(s, a, s') + \gamma U(s')]} $$

There is a direct relationship between the utility of a state and the utility of its neighbors: _the utility of a state is the expected reward for the next transition plus the discounted utility of the next state, assuming that the agent chooses the optimal action._ That is, the utility of a state is given by

$$ \boxed{U(s) = \max_{a \in A(s)} \sum_{s'} p(s'|\ s, a) \ [R(s, a, s') + \gamma U(s')]} $$

This is called the **Bellman equation.**

# Action-Utility Function (Q-Function)

Another important quantity is the _**action-utility function**_, or _**Q-function**_: $Q(s,a)$ is the expected utility of taking a given action $a$ in a given state $s$.

We can compute the utility of a state from the Q-function as:

$$ \boxed{U(s) = \max_a Q(s, a)} $$

Furthermore, the optimal policy can be extracted from the Q-function as:

$$ \boxed{\pi^*(s) = \argmax_a Q(s, a)} $$

We can develop an equivalent Bellman equation for Q-functions instead of utilities as:

$$ \boxed{ Q(s, a) = \sum_{s'} p(s'|\ s, a) [R(s, a, s') + \gamma \max_{a'} Q(s', a')) } $$

Comparing this to the original bellman equation, it seems as if the max was moved

# Algorithms for MDP

## Value Iteration

If there are $n$ possible states, then there are $n$ Bellman equations, one for each state. The $n$ equations contain $n$ unknowns—the utilities of the states. So we would like to solve these simultaneous equations to find the utilities.

There is one problem: the equations are _**nonlinear**_, because the “_**max**_” operator is not a linear operator.

We can however use an iterative approach. We start with arbitrary initial values for the utilities, calculate the right-hand side of the equation, and plug it into the left-hand side—thereby updating the utility of each state from the utilities of its neighbors. We repeat this until we reach an _**equilibrium**_ (convergence).

The iteration step, called a _**Bellman update**_, looks like this:

$$ U_{i+1} \leftarrow \max_{a \in A(s)} \sum_{s'} p(s'|\ s, a) \ [R(s, a, s') + \gamma U_i(s')] $$

Where the update is assumed to be applied _simultaneously_ to all the states at each iteration.

We can think of the value iteration algorithm as _propagating information through the state space by means of local updates_.

```python
function VALUE-ITERATION(mdp, ε) returns a utility function
 # ε is the maximum error allowed in the utility of any state

	U = [0 for s in S] # Vectors of utilities for states in S
	
	repeat 
		δ = 0 # The maximum relative change in the utility of any state
		for state s in S
			U'[s] = max{ p(s'|s, a)[R(s, a, s') + ϒ*U[s']] } # Update step
			δ = max(δ, |U'[s] - U[s]|)
			U = U'
	until δ ≤ ε (1-ϒ)/ϒ # Convergence
	return U
```

It’s guaranteed that value iteration always converges to a unique solution of the Bellman equations whenever $\gamma < 1$, and thus, the corresponding policy is optimal.

## Policy Iteration

The policy iteration algorithm is based on a simple observation: it is possible to get an optimal policy even when the utility function estimate is inaccurate. If one action is clearly better than all others, then the exact magnitude of the utilities on the states involved need not be precise.

This insight suggests an alternative way to find optimal policies.

The policy iteration algorithm alternates two steps, beginning from some initial policy $\pi_0$:

- **Policy evaluation**
    
    Given a policy $\pi_i$ calculate $U_i$, the utility of each state if $\pi_i$ were to be executed.
    
    $$ U_i = \sum_{s'} p(s'|\ s, \pi_i[s]) \ [R(s, \pi_i[s], s') + \gamma U_i(s')] $$
    
    This is a simplified version of the Bellman equation because the action in each state is fixed by the policy $\pi$. The important point is that these equations are _**linear**_, because the “max” operator has been removed.
    
    For $n$ states, we have $n$ linear equations with $n$ unknowns, which can be solved exactly in time $O(n^3)$ by standard linear algebra methods.
    
- **Policy update**
    
    Calculate a new policy $\pi_{i+1}$, using one-step look-ahead based on $U_i$.
    
    $$ \pi_{i+1}[s] \leftarrow \argmax_{a \in A(s)} \sum_{s'} p(s'|\ s, a) \ [R(s, a, s') + \gamma U_i(s')] $$
    

```python
function POLICY-ITERATION(mdp) returns a policy
	π = random() # Policy vector indexed by state, initially random
	U = [0 for s in S] # Vectors of utilities for states in S
	
	repeat 
		U = POLICY-EVALUATION(π, U)
		unchanged = True
		for state s in S
			a* = argmax{ p(s'|s, a)[R(s, a, s') + ϒ*U[s']] } # Policy Update Step
			if a* ≠ π[s]
				π[s] = a*
				unchanged = False
	until unchanged # Convergence
	return U
```

The algorithm terminates when the policy improvement step yields no change in the utilities. Because there are only finitely many policies for a finite state space, and each iteration improves the policy, policy iteration must terminate.

At this point, we know that the utility function $U_i$ is a fixed point of the Bellman update (utilities converged), so it is a solution to the Bellman equations, and $\pi_i$ must be an optimal policy.

# Variant of Policy Iteration

## Modified Policy Iteration

For small state spaces, policy evaluation using exact solution methods is often the most efficient approach. For large state spaces, $O(n^3)$ is too much.

Instead of solving the equations exactly, we can perform some number of simplified value iteration steps to give a reasonably good approximation of the utilities.

$$ U_{i+1} \leftarrow \sum_{s'} p(s'|\ s, \pi_i[s]) \ [R(s, \pi_i[s], s') + \gamma U_i(s')] $$

## Asynchronous Policy Iteration

The algorithms we have described so far require updating the utility or policy for all states at once. It turns out that this is not strictly necessary.

In fact, on each iteration, we can pick _**any subset of states**_ and apply either kind of updating (policy iteration or value iteration). This is called _**asynchronous policy iteration**_.

Given certain conditions on the initial policy and initial utility function, asynchronous policy iteration is guaranteed to converge to an optimal policy.

The freedom to choose any states to work on means that we can design much more efficient heuristic algorithms that concentrate on updating the values of states that are likely to be reached. There’s no sense planning for the results of an action you will never do.