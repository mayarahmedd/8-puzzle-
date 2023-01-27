from functions import commonCode, testGoal


def dfs(initialState, goalTest):
    explored = set()  # defining empty set that will contain the expanded (explored) states
    parent = {initialState: None}  # parent is used to track path to goal
    frontier_state = {initialState: True}  # hashing data for faster performance , key is initial state , value is true means neighbor found
    depth = {initialState: 0}  # will be used to find the longest depth
    while frontier_state:
        # state = next(iter(reversed(frontier_state)))
        # frontier_state.pop(state)
        state = frontier_state.popitem()[0]  # pop last element in frontier_state (just like a stack)
        explored.add(state)  # adding state to explored
        if testGoal(state, goalTest):  # checking if goal was reached
            return parent, state, depth[max(depth, key=depth.get)], explored
        depth, parent, frontier_state = commonCode(explored, state, depth, parent, frontier_state)
        # function that has common code which get neighbor of a state
    return False
