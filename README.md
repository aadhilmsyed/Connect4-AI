# AI Connect-4 Regional Championship 2024 Submission

**Aadhil Mubarak Syed**  
*Department of Computer Science*  
*University of California, Davis*  
*ECS 170: Intro to Artificial Intelligence*  
*Professor Ian Davidson*  
*19 February 2024*

## Introduction

In the realm of artificial intelligence, competitive gaming platforms provide an exciting arena for applying and evaluating cutting-edge AI techniques. In this project, developed for the "AI Connect-4 Regional Championship," I present an AI agent designed to compete against other highly intelligent opponents in the game of Connect-4. This report details the development process, algorithms used, and the performance of the agent against benchmark opponents.

## Evaluation Function

The heart of any Connect-4 AI lies in its evaluation function. I devised a robust evaluation function that considers the number of consecutive pieces on the board for both players. Each configuration of consecutive pieces is assigned a weight proportional to its strategic importance. By calculating the utility of the current game state for both the player and opponent, we can determine the desirability of a move. The difference between the player's utility and the opponent's utility serves as the overall evaluation score. This evaluation function guides the decision-making process of the AI.

## Coding the Agent

Two variants of the minimax algorithm were implemented: the original minimax and an optimized version using alpha-beta pruning. The latter offers a more efficient solution by reducing the number of nodes evaluated in the search tree. The implementation adheres to the time constraint of 0.5 seconds per move, ensuring timely decision-making during gameplay. While a successor function was initially considered to optimize alpha-beta pruning, empirical testing revealed its detrimental effect on performance due to increased computation time.

## Testing the Agent

The AI agent was rigorously tested against benchmark opponents, including StupidAI, RandomAI, and MonteCarloAI. The results demonstrate the agent's proficiency, achieving significant victories against StupidAI and RandomAI. However, challenges arose when facing the more competitive MonteCarloAI. Despite the AI's respectable performance, certain limitations, such as the restricted search depth, hindered its ability to outperform MonteCarloAI consistently.

## Final Results

The final performance of the AI agent against benchmark opponents is summarized below:

| Opponent     | Wins | Ties | Losses |
|--------------|------|------|--------|
| StupidAI     | 10   | 0    | 0      |
| RandomAI     | 10   | 0    | 0      |
| MonteCarloAI | 13   | 0    | 7      |

While the AI agent demonstrated competitive prowess, further optimization, particularly in expanding the search depth, could enhance its capabilities, potentially yielding improved results against formidable opponents like MonteCarloAI.

---

This submission reflects my dedication to developing intelligent AI agents capable of competing at the highest levels. I am confident in the robustness of the algorithms implemented and eager to continue refining them for future competitions.
