
import numpy as np
import matplotlib.pyplot as plt
# fixing seed for reproducibility, change this with your student id
np.random.seed(20220414) 

def create_maze(n, obst):
    """First create a maze. When doing so, please make sure it is a
    solvable one, i.e., if the start or finish states were blocked, 
    you will need to re-run the program.

    Args:
        n (int): creating an n*n maze
        obst (int): the number of obstacles in the maze

    Returns:
        maze (np.array): maze
    """

    maze = np.ones((n, n))
    for _ in range(obst):
        maze[np.random.randint(0, n), np.random.randint(0, n)] = -100
    maze[0, 0] = 1  # start point
    maze[n-1, n-1] = 10  # finish point

    return maze

def visualize_maze(maze):
    """visualze the maze

    Args:
        maze (np.array): an n*n maze

    """

    n=maze.shape[0]
    plt.figure()
    plt.imshow(maze, cmap="gray")
    plt.axis('off')
    obst=0
    for i in range(n):
        for j in range(n):
            if maze[i, j] == -100:
                obst+=1
                plt.text(j, i, 'X', ha='center', va='center', color='red') # Mark obstacles
    plt.text(0, 0, 'START', ha='right', va='center')
    plt.text(n-1, n-1, 'FINISH', ha='left', va='center')
    plt.title(f"{n}x{n} maze")
    # plt.title(f"maze of {n}x{n} with {obst} obstacles")
    # plt.show()
    plt.savefig('maze.pdf')

    return

def create_reward(maze):
    """
    We will create the reward matrix for the maze

    First, let's desfine the possible actions that the agent can take in this
    environment. 

    Let's assume at each state we have 8 possible actions:
    upward                    :  (i-n)
    downward                  :  (i+n)
    left                      :  (i-1)
    right                     :  (i+1)
    diagonally south east     :  (i+n+1)
    diagonally south west     :  (i+n-1)
    diagonally north east     :  (i-n+1)
    diagonally north west     :  (i-n-1)

    For any other action it should receive reward of -INF (negative infinity) 
    to prevent it from happening

    Args:
        maze (np.array): maze

    Returns:
        reward: reward table
    """

    n = maze.shape[0]
    start = 0
    finish = n * n - 1

    # Create the reward matrix for the maze
    reward = np.zeros((n * n, n * n))

    # Initialize with Maze Rewards
    for i in range(finish+1):
        reward[i, :] = maze.flatten()

    # Penalize Invalid Moves
    #modified to EXCLUDE diagonal moves
    for i in range(finish+1):
        for j in range(finish+1):
            if j not in [
                i - n, i + n, i - 1, i + 1
            ]:
                reward[i, j] = -np.inf
            elif j in [
                i + n + 1, i + n - 1, i - n + 1, i - n - 1
            ]:
                reward[i,j] = -1000 # number that is not -inf or -100

    # Boundary Condition Handling
    for i in range(0, finish+1, n):
        for j in range(0, i + n + 1):
            if j in [i + n - 1, i - 1, i - n - 1]:
                reward[i, j] = -np.inf
                reward[j, i] = -np.inf

    return reward


def qlearning(maze, reward, 
            gamma = 0.99, 
            max_iter = 1000, 
            alpha = 0.1, ):
    """ we aim to perform Q-learning.

    Args:
        maze (np.array): _description_
        reward (np.array): reward table
        gamma (float, optional): discount factor. Defaults to 0.99.
        max_iter (int, optional): maximum number of iteration. Defaults to 1000.
        alpha (float, optional): learning rate. Defaults to 0.99.

    Returns:
        qtable (np.array): Q-table
    """

    n = maze.shape[0]
    start = 0
    finish = n * n - 1

    # Q-learning parameters
    qtable = np.random.randn(*reward.shape)  # Initialize randomly

    # Find the optimal policy using the Bellman's equation
    for _ in range(max_iter):
        cs = start  # Current state
        while True:

            ##### Implement your solution here 

            # to help you with the implementation 
            # we have provided a pseudo code for each step
            # START OF YOUR CODE

            # 1. Find possible actions for the current state based on reward table
            actions_set = np.where(reward[cs, :] >= 0)[0]
            
            # 2. Choose a random action as next state and store it to a variable `ns`
            ns = np.random.choice(actions_set) # next state occurs based on action from current state 

            # 3. Find the maximum Q-value for the next state
            actions_new = np.where(reward[ns, :] >= 0)[0]
            max_q = np.max([qtable[ns, i] for i in actions_new]) 

            # 4. Update Q-value using Bellman's equation
            # qtable[cs, ns] = (reward[cs, ns] + gamma * max_q)
            # 4.5 Update Q-value using Temporal Difference (as per part 5)
            qtable[cs, ns] = (1-alpha) * qtable[cs, ns] + alpha * (reward[cs, ns] + gamma * max_q)

            # END OF YOUR CODE
            ##### 

            # Check if the goal is reached
            if cs == finish:
                break

            # Move to the next state
            cs = ns # ns is the random action you choose in step 2. 


    return qtable


def solve_maze(qtable, start, finish):
    """Solve the maze using qtable

    Args:
        qtable (np.array): _description_
        start (int): start point
        finish (int): finish point

    Returns:
        path: path to solve the maze
    """


    n = int(qtable.shape[0]**0.5)
    start = 0
    finish = n * n - 1
    move = None
    path = [start]

    while move != finish:
        move = np.argmax(qtable[start, :])

        # Prevent small loops
        if move in path:
            sorted_indices = np.argsort(qtable[start, :])[::-1]
            for idx in sorted_indices[1:]:
                if idx not in path:
                    move = idx
                    break

        path.append(move)
        start = move

    # Reproducing the path in the maze
    pmat = np.zeros((n, n))
    for pos in path:
        row, col = divmod(pos, n)
        pmat[row, col] = 100

    # Result: optimal path from START to FINISH
    print(f"Total steps: {len(path)}")
    print("Final path:")
    for row, col in [(divmod(pos, n)) for pos in path]:
        print(f"({row+1},{col+1})", end="\t")

    return pmat

def visualize_solution(pmat, maze):
    """Visualize the solution

    Args:
        pmat (np.array): path of the solved maze
        maze (np.array): maze
    """
    

    n=maze.shape[0]

    # Visualize the solution
    plt.figure()
    plt.imshow(pmat, cmap="gray")
    for i in range(n):
        for j in range(n):
            if maze[i, j] == -100:
                plt.text(j, i, 'X', ha='center', va='center', color='red')
            if pmat[i, j] == 100:
                plt.text(j, i, '\u2022', ha='center', va='center', color='black')
    plt.text(0, 0, 'START', ha='right', va='center')
    plt.text(n-1, n-1, 'GOAL', ha='left', va='center')
    plt.imshow(maze, alpha=0.2, cmap="gray")
    plt.axis('off')
    # plt.show()
    plt.savefig('solved_maze.pdf')

    return



if __name__=='__main__':
    n=12
    obst=30

    maze = create_maze(n, obst)
    visualize_maze(maze)
    reward = create_reward(maze)
    ### before you call this function, complete the implementation of qlearning
    qtable = qlearning(maze, reward)
    

    n = maze.shape[0]
    start = 0
    finish = n * n - 1
    pmat = solve_maze(qtable, start, finish)
    visualize_solution(pmat, maze)



