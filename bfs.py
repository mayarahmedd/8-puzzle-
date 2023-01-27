from functions import testGoal, commonCode


def bfs(initialState, goalTest):
    explored = set()  # defining empty set that will contain the expanded (explored) states
    parent = {initialState: None}  # parent is used to track path to goal
    frontier_state = {
        initialState: True}  # hashing data for faster performance , key is initial state
    # , value is true means neighbor found
    depth = {initialState: 0}  # will be used to find the longest depth
    while frontier_state:  # while there is state in frontiers explore
        state = next(iter(frontier_state))  # converting frontier dict to iterable and finding first state
        frontier_state.pop(state)  # removing element from frontier
        explored.add(state)  # adding state to explored
        if testGoal(state, goalTest):  # checking if goal was reached
            return parent, state, depth[max(depth, key=depth.get)], explored
        depth, parent, frontier_state = commonCode(explored, state, depth, parent, frontier_state)
    return False

