![[Pasted image 20251101013004.png]]
## [1] create the environment

```python
env = gym.make('Taxi-v3')
env = env.unwrapped # access internal transitions (env.P)


n_states = env.observation_space.n

n_actions = env.action_space.n
```

## [2] Initialize Parameters

```python

discount = 0.9    # γ (gamma): discount factor

theta = 1e-6      # small threshold for stopping policy evaluation

max_iterations = 1000

  
# initial policy (π): all zeros (can be random)

policy = np.zeros(n_states, dtype=int)

  
# initial state values (V): all zeros

V = np.zeros(n_states)
```

## [3] Policy evaluation


![[Pasted image 20251101012119.png]]

```python
def policy_evaluation(env,policy,discount.theta):
	while True:
		delta = 0
		for s in range(n_states):
			a = policy[s]
			v = 0
			for prob, next_s,reward in env.P[s][a]:
				v += prob*(reward+ discount*V[next_s])
			delta = max(delta,abs(V[s]-v))
		if delta <theta:
			break
		return v
```

## [4] Policy Improvement

![[Pasted image 20251101012156.png]]
``` python
def policy_improvement(env,V,policy, discount):
	policy_stable = True
	for s in range(n_states):
	
		old_action = policy[s]
		Q = np.zeros(n_actions)
		
		for a in range(n_actions):
			for prob,next_s,reward, done in env.P[s][a]:
			 Q +=prob+(reward +discount*V[next_s])
		best_action = np.argmax(Q)
		policy[s] = best_action
		if best_action != old_action:
			policy_stable = False
	return policy, policy_stable
			
```
## [4] Policy Iteration

    Main loop: alternate between policy evaluation and improvement
    until policy stabilizes (converges).

```python

def policy_iteration(env, policy, V, discount, theta, max_iterations):


    for i in range(max_iterations):

        V = policy_evaluation(env, policy, V, discount, theta)

        policy, stable = policy_improvement(env, V, policy, discount)

        if stable:

            print(f"✅ Policy converged after {i + 1} iterations")

            break

    return policy, V
```

##  RUN POLICY ITERATION

```python
optimal_policy ,final_values = policy_iteration(env,policy, V, discount, theta, max_iterations)
print(final_values)
print(optimal_policy)
```
## TEST THE LEARNED POLICY

```python
env= gym.make("Taxi-v3", render_mode="human")
state ,info = env.reset()
done = false
path =[state]
while not done:
	action = int(optimal_policy[state])
	next_state,reward,terminated,truncted,info = env.step(action)
	done =terminated,truncted
	path.append(next_state)
	env.render()
	state = next_state
print(path)

```