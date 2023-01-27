import math

from functions import testGoal, getNeighbors


def euclideanDistance(prev_row, goal_row, prev_col, goal_col):  # Euclidean Heuristic function
    # h = 𝑠𝑞𝑟𝑡((𝑐𝑢𝑟𝑟𝑒𝑛𝑡 𝑐𝑒𝑙𝑙.𝑥 − 𝑔𝑜𝑎𝑙.𝑥)**2 + 𝑠𝑞𝑟𝑡((𝑐𝑢𝑟𝑟𝑒𝑛𝑡 𝑐𝑒𝑙𝑙.𝑦 − 𝑔𝑜𝑎𝑙.𝑦)**2)
    return math.sqrt((prev_row - goal_row) ** 2 + (prev_col - goal_col) ** 2)


def manhattanDistance(prev_row, goal_row, prev_col, goal_col):  # Manhattan Heuristic function
    # h(n) = abs(currentState.x - goal.x) + abs(currentState.y - goal.y)
    return abs(prev_row - goal_row) + abs(prev_col - goal_col)


def heuristicDecider(option, state, goal):  # Decides which heuristic to use
    state = list(state)  # converting state(string) to list of characters '0' -> '9'
    goal = list(goal)  # converting goal (string) to list of characters '0' -> '9'
    H = 0
    for i, item in enumerate(
            state):  # iterating through the state's characters  ("i" is the index, "item" is the character(Digit))
        if item == '0':
            i = 0  # Removing zero as it isn't counted in the heuristic functions
            item = 0
        else:  # any digit other than '0'
            # i = int(i)
            item = goal.index(item)  # Modification for any goal.
        prev_row, prev_col = int(i / 3), i % 3  # i/3 get the row , i%3 get the column
        goal_row, goal_col = int(item / 3), int(item) % 3
        if option == 0:
            H += manhattanDistance(prev_row, goal_row, prev_col, goal_col)
        else:
            H += euclideanDistance(prev_row, goal_row, prev_col, goal_col)
    return H


def A_star(option, initialState, goalState):
    # f = G + h
    G = 0  # G is the cost between states
    parent = {initialState: None}  # parent is used to track path to goal
    frontier = {initialState: heuristicDecider(option, initialState, goalState) + G}
    # hashing data for faster performance , key is initial state , value is F=G+H
    explored = set()  # defining empty set that will contain the expanded (explored) states
    depth = {initialState: 0}  # will be used to find the longest depth
    while frontier:
        state = min(frontier, key=frontier.get)  # finding minimum heuristic value (just like a priority queue)
        # state = next(iter(frontier))
        G = frontier[state] - heuristicDecider(option, state, goalState)  # Tracking G F=G+H G=F-H
        frontier.pop(state)  # removing element from frontier
        explored.add(state)  # adding state to explored
        # print(state)
        G += 1  # increasing cost by 1 (we went down in our tree)
        if testGoal(state, goalState):  # checking if goal was reached
            return parent, state, depth[max(depth, key=depth.get)], explored
        for neighbour in getNeighbors(state):  # iterating through neighbors
            neighbour = ''.join(neighbour)  # joining list of characters to get a string
            if neighbour not in frontier and neighbour not in explored:
                # checking if string exists in frontier or explored
                parent[neighbour] = state  # the parent of the neighbor is the state
                depth[neighbour] = depth[state] + 1  # depth is increased by 1
                frontier[neighbour] = heuristicDecider(option, neighbour,
                                                       goalState) + G  # inserting new neighbor in frontier_state
    return False
