---
theme: neversink
background: RL-bg.png
class: 'text-center'
title: Reinforcement Learning (DSAI 402)
author: Mohamed Ghalwash
year: 2025-2026
venue: Zewail City
mdc: true
lecture: 8
slide:
  disableSlideNumbers: true
slide_info: false
---

# Reinforcement Learning <br> (DSAI 402)
## Lecture 8

Mohamed Ghalwash
<Email v="mghalwash@zewailcity.edu.eg" />

---
layout: fact
---

# Recording is NOT allowed 

---
transition: fade-out
layout: top-title
class: ns-c-center-item
---

:: title :: 

# Lecture 7 Recap

:: content :: 

- Model-based

- Model-free 
  - MC
  - MC with Exploring start 
  - $\epsilon$-greedy MC

- TD Learning 
  
--- 
layout: top-title
---
:: title ::

# What is TD Learning?

:: content :: 

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \right]
$$

- Model-free reinforcement learning method
- Learns the **value function** $V(s)$ of states directly
- Updates estimates **at each step**, not waiting for episode end
- Combines ideas from **Monte Carlo** and **Dynamic Programming**
  

--- 
layout: top-title
---

:: title ::

# Why TD Learning?

:: content :: 

- Can learn **online**: updates immediately at every step
- Does not require knowledge of the full episode
- Often faster and more data-efficient than Monte Carlo methods



--- 
layout: top-title
---

:: title ::

# TD Update Rule

:: content :: 

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \right]
$$

$\alpha$ is the learning rate  


### TD Error (Temporal Difference Error)

$$
\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)
$$

- Measures the difference between estimated and actual rewards
- Used to adjust $V(S_t)$ closer to true expected future rewards

---
layout: center
class: text-center
---

# Learn More

[Course Homepage](https://github.com/m-fakhry/DSAI-402-RL)
