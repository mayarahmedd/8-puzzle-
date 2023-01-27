
def testGoal(explored, goalTest):
    if explored == goalTest:
        return True
    else:
        return False
#indexes              #example
# 0 1 2               # 1 2 3
# 3 4 5               # 4 0 5
# 6 7 8               # 6 7 8
def getNeighbors(currentPuzzle):  # This function is used to find the neighbors (children) of the current puzzle
    state = str(currentPuzzle)
    index = currentPuzzle.find('0')  # finding index of zero to see available slides
    neighbors = []
    if index > 2:  # move up
        neighbors.append(swap(state, index - 3))
    if index < 6:  # move down
        neighbors.append(swap(state, index + 3))
    if index % 3 > 0:  # move left
        neighbors.append(swap(state, index - 1))
    if index % 3 < 2:  # move right
        neighbors.append(swap(state, index + 1))
    return neighbors


def swap(currentPuzzle, neighbor):  # This function is used to swap 0 with the available neighbor
    list1 = list(currentPuzzle)  # converting string (puzzle) to list of characters
    b = neighbor  # index of neighbor
    a = list1.index('0')  # getting index of 0
    list1[a], list1[b] = list1[b], list1[a]  # swapping
    return list1


def commonCode(explored, state, depth, parent, frontier_state):
    for neighbour in getNeighbors(state):  # iterating through neighbors
        neighbour = ''.join(neighbour)  # joining list of characters to get a string
        if neighbour not in frontier_state and neighbour not in explored:
            # checking if string exists in frontier or explored
            parent[neighbour] = state  # the parent of the neighbor is the state
            depth[neighbour] = depth[state] + 1  # depth is increased by 1
            frontier_state[neighbour] = True  # inserting new neighbor in frontier_state
    return depth, parent, frontier_state







def printNodes(printingNodes, option):
    # printingNodes is list of string that has either explored nodes or has nodes from Path to goal
    if option == 0:
        print("Path To Goal:")
        printingNodes.reverse()  # reversing to start from original puzzle to goal not vice versa
    else:
        print("Explored Nodes:")
    for word in range(len(printingNodes)):  # word is the index of string inside printingNodes
        for i in range(0, 10, 3):  # "i" is the index of letters in the string
            print(" ".join(printingNodes[word][i:i + 3]))  # adding space between each number


def validateInput(inputPuzzleState):  # validate that input is 9 digits from 0 to 9 with no duplicates
    if len(inputPuzzleState) != 9:
        print("Incorrect Puzzle(It should 9 digits)")
        return False
    try:
        int(inputPuzzleState)  # used in try except to see if the input is only integer or not
        duplicates = [number for number in list(inputPuzzleState) if
                      list(inputPuzzleState).count(number) > 1]  # count duplicates and save them
        if len(duplicates) != 0:
            print("Incorrect Puzzle (Repeated Digit)")
            return False
        return True
    except(Exception,):
        print("Incorrect Puzzle (Not integer)")
        return False


def checkIfSolvable(inputPuzzleState):  # check if the puzzle is solvable.....This can be done
    # by checking for even inversions or odd inversions. If it is even then it can be solved because every slide (
    # change in puzzle) add two inversions or remove 2 inversions So if it is odd inversions it won't be solved This
    # can be done by simply counting how many large digit come before a smaller digit
    inversions = 0
    for i in range(0, 9):  # iterating through all elements
        for j in range(i + 1, 9):
            if int(inputPuzzleState[i]) > int(inputPuzzleState[j]) and int(inputPuzzleState[i]) != 0 and int(
                    inputPuzzleState[j]) != 0:  # 0 isn't counted in inversions
                inversions += 1
    if inversions % 2 != 0:  # if it is odd, it can't be solved
        print("This Puzzle can't be solved")
        return False
    return True




