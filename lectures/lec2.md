---
theme: neversink
background: RL-bg.png
class: 'text-center'
transition: slide-left
title: Reinforcement Learning (DSAI 402)
author: Mohamed Ghalwash
year: 2025-2026
venue: Zewail City
mdc: true
lecture: 2
# slide:
#   disableSlideNumbers: true
slide_info: false
---

# Reinforcement Learning <br> (DSAI 402)
## Lecture 2

Mohamed Ghalwash
<Email v="mghalwash@zewailcity.edu.eg" />

---
transition: fade-out
layout: top-title
class: ns-c-center-item
---

:: title :: 

# Lecture 1 Recap

:: content :: 

- RL definition (environment, action, reward, observation)
- Challenges in RL
- Into for Markov Process 


```mermaid {theme: 'neutral', scale: 1}
graph LR
A((Agent)) --> |Action| B((Environment))
B --> |Observation| A
B --> |Reward| A
classDef cir fill:#f9f,stroke:#333,stroke-width:4px;
class A,B cir;
linkStyle 0 stroke:#333,stroke-width:2px,color:black;
linkStyle 1 stroke:#333,stroke-width:2px,color:green;
linkStyle 2 stroke:#333,stroke-width:2px,color:blue;
```

<BottomBar/>

---
layout: top-title
# image: images/mouse_maze.png
---

:: title :: 

# Markov Process 

:: content :: 

- States 
- Transition matrix $P$
- Markov Property: $P(S_t|S_{t-1},S_{t-2},\ldots,S_1) = P(S_t|S_{t-1})$

<br><br>
Examples:

- Weather `S R S S S R R R S R `

- Currency Exchange Rate 
  
<br><br><br>

- What does it mean $P^2$? 
  
<BottomBar/>

---
layout: top-title
# image: images/mouse_maze.png
---

:: title :: 

# Markov Reward Process 

:: content :: 

- States: $S$
- Transition matrix: $P$ _source $\rightarrow$ target_
- Accumulated Reward: $G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \ldots$
- Markov property: $P(R_t, S_t|S_{t-1},S_{t-2},\ldots,S_1) = P(R_t, S_t|S_{t-1})$
- Value function: $V(s) = E(G | S_t = s)$

<br><br><br><br><br>
Examples 
- Cat moving through rooms 

<BottomBar/>

---
layout: center
class: text-center
---

# Learn More

[Slidev](https://sli.dev) · [Course Homepage](https://github.com/m-fakhry/DSAI-402-RL)
