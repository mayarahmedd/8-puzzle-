import time


from a_star import A_star
from bfs import bfs
from dfs import dfs
from functions import validateInput, checkIfSolvable, printNodes

if __name__ == '__main__':
    stop = 0
    while stop == 0:
        try:
            inputPuzzle = input("Please Enter Your puzzle: ")
            if validateInput(inputPuzzle) and checkIfSolvable(inputPuzzle):
                print("1.BFS 2.DFS 3.A star with Manhattan Heuristic 4.A star with Euclidean Distance 5.EXIT")
                choice = input("Please Enter Your Choice(1-4): ")
                t0 = time.time()  # start timer
                choice = int(choice)
                current_State = inputPuzzle
                parents = {}
                expanded = set()
                maxDepth = 0

                if choice == 1:
                    parents, current_State, maxDepth, expanded = bfs(inputPuzzle, "012345678")
                elif choice == 2:
                    parents, current_State, maxDepth, expanded = dfs(inputPuzzle, "012345678")
                elif choice == 3:
                    parents, current_State, maxDepth, expanded = A_star(0, inputPuzzle, "012345678")
                elif choice == 4:
                    parents, current_State, maxDepth, expanded = A_star(1, inputPuzzle, "012345678")
                elif choice == 5:
                    stop = 1
                trace_state = current_State  # This is used to trace the path to goal
                cost = 0
                pathToGoal = []  # Used to trace the path to goal
                while parents[trace_state]:  # while not none
                    cost += 1  # increasing cost as we go up
                    pathToGoal.append(trace_state)  # adding element to pathToGoal list to be printed
                    trace_state = parents[trace_state]  # Going to the parent
                pathToGoal.append(trace_state)  # adding last element which doesn't have a parent
                printNodes(pathToGoal, 0)  # printing path To Goal
                printNodes(list(expanded), 1)  # printing explored nodes after turning them to list of string
                print("Depth is ", maxDepth)
                print("cost=", cost)
                t1 = time.time() - t0  # stopping timer

                print("Time elapsed: ", t1)  # printing CPU seconds elapsed (floating point)
                print()

        except:
            stop = 1
            print()
