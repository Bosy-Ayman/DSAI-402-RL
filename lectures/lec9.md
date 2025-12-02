--- 
layout: top-title 
--- 

:: title :: 

# On-policy TD control (SARSA)

:: content :: 

- Estimate the action value function $q$ not the state value function $v$

$$
q(s_t, a_t) = q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma q(s_{t+1}, a_{t+1}) - q(s_t, a_t) \right]
$$

<v-click>

- What is on-policy and off-policy?

</v-click>

---
layout: cover
--- 

# Q-Learning

