

PART 1 & 2: THEORETICAL ANSWERS


1. Counterexample: Value Iteration with gamma = 1

   ----------------------------------------------

   Scenario: Imagine a state in Breakout where the ball enters a vertical loop,

   bouncing between the paddle and the ceiling indefinitely without hitting any

   bricks.

   Why it fails: If the agent receives a positive reward (e.g., +1 for survival)

   periodically in this loop, the Value V(s) is the sum of infinite future rewards:

   V(s) = 1 + 1 + 1 + ... = Infinity.

   Value Iteration tries to converge to a fixed number. Since the sum grows

   forever, the algorithm fails to converge.

  

2. Scenario: Greedy vs. Epsilon-Greedy

   -----------------------------------

   Scenario: The "Safe Middle" Trap.

   Greedy Failure: A Greedy agent exploits the current best knowledge. In MinAtar

   Breakout, keeping the paddle in the center is a "safe" strategy to return the

   ball. The agent might converge to this local optimum and never try risky moves

   required to hit the corners.

   Epsilon-Greedy Success: To clear the corner bricks, the paddle must hit the

   ball with its edge to create a sharp angle. This is risky. An Epsilon-Greedy

   agent will occasionally take random "risky" moves. Eventually, one of these

   moves will clear a hard-to-reach brick, revealing a massive reward and

   allowing the agent to learn the superior strategy.