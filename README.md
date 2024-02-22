# Connect-4 AI


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
