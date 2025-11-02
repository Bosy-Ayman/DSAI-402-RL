
|**Function / Attribute**|**Type**|**Purpose / Description**|**Used In**|**Example Usage**|
|---|---|---|---|---|
|`gym.make(env_name, **kwargs)`|Function|Creates and initializes the environment. You can customize it with parameters like `is_slippery` in FrozenLake.|Before training|`env = gym.make("FrozenLake-v1", is_slippery=True)`|
|`env.reset()`|Function|Resets the environment to the starting state and returns the initial observation (state). Also resets rewards and episode info.|At the start of each episode|`state, info = env.reset()`|
|`env.step(action)`|Function|Executes one step in the environment given an action. Returns: `(next_state, reward, terminated, truncated, info)`.|In policy testing or agent training loops|`next_state, reward, terminated, truncated, info = env.step(action)`|
|`env.render()`|Function|Visually renders the current state of the environment. If `render_mode="human"`, it shows it on screen.|During simulation or testing|`env.render()`|
|`env.close()`|Function|Closes the environment window and cleans up resources.|After finishing all episodes|`env.close()`|
|`env.unwrapped`|Attribute|Gives access to the raw environment without wrappers (important for accessing internal attributes like `env.P`).|Used in value/policy iteration to access transition probabilities|`env = env.unwrapped`|
|`env.P`|Attribute (dict)|The transition probability dictionary: `env.P[state][action] = [(prob, next_state, reward, done), ...]`. It describes the full Markov Decision Process (MDP) dynamics.|**Core** in Value Iteration & Policy Iteration|`for prob, next_state, reward, done in env.P[s][a]: ...`|
|`env.action_space`|Object|Describes all possible actions the agent can take.|Used to know number of actions|`env.action_space.n` (for discrete spaces)|
|`env.observation_space`|Object|Describes the set of possible states or observations in the environment.|Used to know number of states|`env.observation_space.n` (for discrete states)|
|`env.action_space.sample()`|Function|Randomly picks an action from the available actions (useful for exploration or testing).|In random or exploratory policies|`action = env.action_space.sample()`|
|`env.observation_space.sample()`|Function|Randomly samples a state (useful for debugging or random starts).|Testing or debugging|`state = env.observation_space.sample()`|
|`env.spec`|Attribute|Holds environment metadata, such as ID, version, and max_episode_steps.|For information or configuration|`print(env.spec)`|
|`env.reward_range`|Attribute|Tuple showing the minimum and maximum possible reward values.|Used for scaling or debugging|`print(env.reward_range)`|
|`env.metadata`|Attribute|Dictionary with information about rendering modes and FPS.|To check available render modes|`print(env.metadata)`|
|`env.seed(seed_value)` _(older Gym)_|Function|Sets a fixed random seed for reproducibility. _(Deprecated in Gymnasium)_|Used in reproducible experiments|`env.reset(seed=42)` (modern way)|
|`env.max_episode_steps`|Attribute|Defines the maximum steps before an episode ends automatically.|Used for loop control|`for t in range(env.spec.max_episode_steps): ...`|

## 🧠 Deep Understanding of Important Elements

### 🔹 1. Transition Probability `env.P`

The `env.P` dictionary is the mathematical model of the environment—the core of the **Markov Decision Process (MDP)**. Accessing this attribute is crucial for **model-based** reinforcement learning algorithms, such as **Value Iteration** and **Policy Iteration**, which explicitly use these probabilities to compute the optimal policy.

Each entry `env.P[state][action]` is a list of possible transitions that could occur when taking the specified action from the given state. Each transition is represented as a tuple:

$$(probability, next\_state, reward, terminated)$$

#### Stochastic vs. Deterministic Environments

- **Stochastic (Probabilistic) MDP:** This is the case in the standard 'slippery' FrozenLake environment. If the sum of probabilities for a given `env.P[state][action]` entry is greater than one, it indicates that taking one action can lead to several possible next states.
    
    - _Example for Stochastic FrozenLake (Slippery):_
        
        ```python
        env.P[0][1] 
        # [(0.333, 4, 0, False), (0.333, 1, 0, False), (0.333, 0, 0, False)]
        ```
        
        In this case, the agent attempts to move RIGHT (action $1$) but has a $33.3\%$ chance of actually moving down (to state $4$), right (to state $1$), or staying put (state $0$) due to the slippery ice.
        
- **Deterministic MDP:** If the `is_slippery=False` parameter is passed during environment creation, the environment becomes deterministic. This means that for any state-action pair, there will be only _one_ possible transition, and its probability will be $1.0$.
    
    - _Example for Deterministic FrozenLake (Non-Slippery):_
        
        ```
        env.P[0][1] 
        # [(1.0, 1, 0, False)]
        ```
        
        From state $0$, taking action $1$ (RIGHT) **always** leads to state $1$.
        

The `terminated` (or `done`) boolean in the tuple is critical as it tells the planning algorithm which states are terminal (like the Hole or Goal) and must be treated as absorbing states with a value of zero.

### 🔹 2. Observation and Action Spaces

The spaces define the boundaries of the Reinforcement Learning problem. Gymnasium uses the `gym.Space` class hierarchy to represent these, primarily divided into **Discrete** and **Continuous** types.

#### Discrete Spaces (`Discrete(n)`)

As seen in FrozenLake:

```python
print(env.observation_space)  # Discrete(16)
print(env.action_space)       # Discrete(4)
```

- **Observation space (**$16$**)** $\rightarrow$ Represents a set of $16$ mutually exclusive states (the $16$ tiles on the grid). States are referenced by integer indices from $0$ to $15$.
    
- **Action space (**$4$**)** $\rightarrow$ Represents a choice from $4$ specific, distinct actions (LEFT, DOWN, RIGHT, UP), also referenced by integer indices from $0$ to $3$.
    

We use `.n` to query the total count of states or actions:

```
num_states = env.observation_space.n
num_actions = env.action_space.n
```

#### Continuous Spaces (`Box(low, high, shape)`)

Continuous environments, like CartPole or robotics environments, use the `Box` space, where observations and actions are represented by multi-dimensional arrays of floating-point numbers.

- **Observation Space Example (CartPole):**
    
    ```python
    print(env_cartpole.observation_space) 
    # Box(-4.8..4.8, -Inf..Inf, -0.418..0.418, -Inf..Inf, (4,), float32)
    ```
    
    This space defines $4$ continuous values for the state: position of the cart, velocity of the cart, angle of the pole, and angular velocity of the pole. You can access the specific limits:
    
    ```python
    print(env_cartpole.observation_space.low) 
    # [-4.8  -inf -0.418 -inf]
    ```
    
- **Action Space Example (Robotics):** For a robotic arm where the action is a continuous motor torque, the action space might be defined as `Box([-1.0], [1.0], (1,), float32)`, meaning the action is a single float between $-1.0$ and $1.0$.
    

### 🔹 3. Step Function in Detail: The Terminated/Truncated Split

The `env.step(action)` function is the primary way the agent interacts with the environment. It returns a tuple of five values, and the separation of the final two booleans is a critical feature of Gymnasium designed for clarity in episode termination:

$$ (next_state, reward, terminated, truncated, info) $$

|Return Value|Description|Implication for Episode|
|---|---|---|
|**`next_state`**|The new state index (discrete) or array (continuous) reached after applying the action.|Used as the starting point for the next time step.|
|**`reward`**|The scalar value received for the transition $S \rightarrow S'$.|Used to update the agent's Value or Q-function.|
|**`terminated`**|**Natural End:** `True` if the episode ended because the agent achieved a goal state, failed, or hit a constraint built into the core MDP.|The task is **completed** (success or failure).|
|**`truncated`**|**External End:** `True` if the episode ended because a limit, usually a step count limit (defined by `env.spec.max_episode_steps`), was reached.|The task was **interrupted**.|
|**`info`**|A dictionary for auxiliary debugging/logging information (e.g., probability of success, a hidden true state, or other metadata).|Not used for core RL calculations but useful for debugging.|

#### Controlling the Episode Loop

In prior versions of Gym, only one boolean (`done`) was returned. In Gymnasium, the loop must continue until _either_ flag is true:

```python
done = terminated or truncated
if done:
    # Episode finished, break loop and reset environment
    state, info = env.reset()
```

This split is important because model-free algorithms often treat termination (win/lose) and truncation (timeout) differently when calculating state values or bootstrapping.

### 🔹 4. Reset Function and Reproducibility

The `env.reset()` function prepares the environment for a new episode.

```
state, info = env.reset(seed=42)
```

The introduction of the `seed` parameter directly into `reset()` (instead of the deprecated `env.seed()`) is central to reproducible research in reinforcement learning. Setting a fixed integer seed:

1. **Initial State:** Ensures the starting state (e.g., initial position in CartPole, starting tile in FrozenLake) is always the same for that seed.
    
2. **Internal Randomness:** Fixes the internal random number generator (RNG) used for stochastic transitions (like the slipperiness in FrozenLake) and the `env.action_space.sample()` function, allowing training runs to be perfectly replicated.
    

The returned `info` dictionary from `reset()` often contains initial probability distributions or other metadata about the environment setup that is not considered part of the initial observation $S_0$.

### 🔹 5. Render Function and Modes

The visual output of the environment is controlled by the `render_mode` argument passed to `gym.make()`.

- **`render_mode="human"`:** This is the default when you want to watch the agent interact in real-time. It opens a native window on your local machine.
    
- **`render_mode="ansi"`:** Used primarily for text-based environments like FrozenLake. It returns the current environment state as a string, which is useful for printing the board layout in command-line environments or notebooks without graphical support.
    
- **`render_mode="rgb_array"`:** This is the standard mode for **headless training** (i.e., on cloud servers without a monitor) and for **video recording**. It returns the environment state as a NumPy array representing the raw pixel data, which can then be saved frame-by-frame.
    

### 🔹 6. Unwrapping the Environment and Wrappers

Gymnasium environments are commonly composed of an **inner core environment** (which holds `env.P`) and **outer wrappers**.

- **Wrappers** are standard components used to modify an environment's inputs, outputs, or behavior without changing its fundamental physics or MDP definition. Common examples include:
    
    - **`TimeLimit` Wrapper:** Automatically adds the functionality that sets the `truncated=True` flag after a defined number of steps (`env.spec.max_episode_steps`).
        
    - **Normalization Wrappers:** Automatically scale the observation space (e.g., from $[-10, 10]$ to $[-1, 1]$) or action space to aid neural network training.
        
    - **`ObservationWrapper` / `ActionWrapper`:** Used to change the format of the data returned to/sent by the agent (e.g., stacking the last four frames for a CNN).
        

The **`env.unwrapped` attribute** is used to bypass all these layers of wrappers and directly access the base environment object, which is necessary to retrieve non-standard attributes like the transition probability dictionary `env.P`.

## 🧩 Example — Using Everything Together

```python
import gymnasium as gym
import numpy as np

# Create a deterministic (non-slippery) environment for clarity
env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="ansi")
env = env.unwrapped # Unwrap to access the core P attribute

# Check spaces
print("States:", env.observation_space.n)
print("Actions:", env.action_space.n)

# Reset environment and set a seed for reproducibility
state, info = env.reset(seed=123)
print("Initial state (0):", state)

# Try one deterministic step (Action 2 is RIGHT)
action = 2
next_state, reward, terminated, truncated, info = env.step(action)
print(f"Action {action} (Right) -> Next State {next_state}, Reward {reward}, Terminated {terminated}, Truncated {truncated}")

# Example of accessing P for the transition that just occurred
# In a non-slippery env, env.P[0][2] should only have one outcome:
transition_data = env.P[state][action] 
print(f"Transition Data (from env.P): {transition_data}")

# Render environment (using ANSI mode, returns a string)
print("\n--- Current State Render ---")
print(env.render())

env.close()
```

## 🧾 Summary Table

|**Category**|**Key Functions / Attributes**|**Purpose**|
|---|---|---|
|**Setup & Lifecycle**|`gym.make()`, `env.reset()`, `env.close()`, `env.reset(seed=X)`|Create, initialize, and ensure reproducible episode starts and safe shutdown.|
|**Interaction Loop**|`env.step()`, `env.render()`|Execute agent actions and visualize environment progression.|
|**Spaces & Bounds**|`env.action_space`, `env.observation_space`, `.n`, `.low`, `.high`|Define the structure (Discrete or Continuous) and boundaries of inputs/outputs.|
|**Model Information**|`env.P`, `env.unwrapped`|Access the full MDP transition dynamics for model-based planning algorithms.|
|**Termination Status**|`terminated`, `truncated`|Precisely differentiate between a natural episode end (win/loss) and an imposed time limit.|
|**Metadata**|`env.spec`, `env.reward_range`, `env.metadata`|Obtain environment configuration, step limits, and reward boundaries for standardized implementation.|