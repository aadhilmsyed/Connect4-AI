# Connect-4 AI

## Minimax AI Algorithm

I implemented two variants of the minimax algorithm: the original minimax and an optimized version using alpha-beta pruning. The latter offers a more efficient solution by reducing the number of nodes evaluated in the search tree. The implementation adheres to the time constraint of 0.5 seconds per move, ensuring timely decision-making during gameplay. Both algorithms determine a move based on the nash equillibrium returned by the evaluation function.


## Evaluation and Heuristic Function

The evaluation function I devised considers the number of consecutive pieces on the board for both players. Each configuration of consecutive pieces is assigned a weight proportional to its likeliness to victory. By calculating the utility of the current game state for both the player and opponent, we can determine the desirability of a move. The difference between the player's utility and the opponent's utility serves as the overall evaluation score for a given game state. For my sucessor function which determines which column to explore first to maximize pruning, I ordered the columns based on a priority order of middle first, then corners, then everything else.


## Agent Performance

The AI agent underwent rigorous testing against benchmark opponents, including StupidAI, RandomAI, and MonteCarloAI. While it demonstrated proficiency, achieving significant victories against StupidAI and RandomAI, it faced challenges against the more competitive MonteCarloAI. Despite its respectable performance, limitations such as restricted search depth hindered its ability to consistently outperform MonteCarloAI.

The final performance results of the AI agent against benchmark opponents are summarized below:

| Opponent     | Wins | Ties | Losses |
|--------------|------|------|--------|
| StupidAI     | 10   | 0    | 0      |
| RandomAI     | 10   | 0    | 0      |
| MonteCarloAI | 13   | 0    | 7      |

While these results were obtained using a search depth of 3, it's noteworthy that running the algorithm with a depth of 4 resulted in undefeated performance against MonteCarloAI. This suggests that further optimization, particularly by expanding the search depth, could significantly enhance the agent's capabilities, potentially yielding improved results against formidable opponents like MonteCarloAI.


## Running this Program

To run the provided code, follow these instructions:

1. **Clone the Repository**: Clone or download the repository containing the Connect-4 project files.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where the project files are located.

3. **Run the Command**:
    - Use the following command format to execute the code:
    ```
    python main.py [OPTIONS]
    ```
    - Replace `[OPTIONS]` with the desired command-line options described below.

### Commandline Interface Options

| Option         | Description                                                          | Datatype | Example                   | Default |
|----------------|----------------------------------------------------------------------|----------|---------------------------|---------|
| -p1            | Agent acting as player 1 (e.g., minimaxAI)                          | String   | -p1 minimaxAI            | human   |
| -p2            | Agent acting as player 2 (e.g., minimaxAI)                          | String   | -p2 monteCarloAI         | human   |
| -seed          | Seed for AI’s with stochastic elements                               | int      | -seed 0                   | 0       |
| -w             | Rows of the game board                                               | int      | -w 6                      | 6       |
| -l             | Columns of the game board                                            | int      | -l 7                      | 7       |
| -visualize     | Bool to use or not use GUI                                           | bool     | -visualize True           | True    |
| -verbose       | Sends move-by-move game history to shell                             | bool     | -verbose True             | False   |
| -limit_players | Players with time limits (format: "x,y" where x and y are players)   | String   | -limit_players 1,2        | 1,2     |
| -time_limit    | Time limit for each player (format: "x,y" where x and y are float)   | String   | -time_limit 0.5,0.5       | 0.5,0.5 |
| -cvd_mode      | Swaps existing color scheme for colorblind-friendly palette          | bool     | -cvd_mode True            | False   |

### Example Commands

Here are some example commands to run the code:

- To run a game with `alphaBetaAI` as player 1 and `stupidAI` as player 2:
  ```
  python main.py -p1 alphaBetaAI -p2 stupidAI -limit_players 1,2 -verbose True -seed 0
  ```

- To run a game with `stupidAI` as player 1 and `alphaBetaAI` as player 2:
  ```
  python main.py -p1 stupidAI -p2 alphaBetaAI -limit_players 1,2 -verbose True -seed 0
  ```

- Adjust the options as needed to customize the game settings and behavior.
