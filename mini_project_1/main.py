import sys
import copy
import search

from solution import Trip, ASARProblem, State

def main():
    
    
    filename = "examples/simple{}.txt"
    solution_file = "solutions/solution{}.txt"

    for k in range(1, 9):

        print("Solving Problem:", k)

        problem = ASARProblem()
        State.counters = {0: 1}
        Trip.counter   = 0
        Trip.min_cost  = sys.maxsize

        with open(filename.format(k), "r+") as file:
            problem.load(file)

        for _ in range(0, 1):

            best = search.astar_search(problem, problem.heuristic)
            
            if (best != None): 
                with open(solution_file.format(k), "w+") as file:
                    problem.save(file, best.state)

            else:
                with open(solution_file.format(k), "w+") as file:
                    problem.save(file, best)
                
                print("Infeasible")
            
            for key in State.counters:
                    print(key, ":",State.counters[key])

if __name__ == "__main__":
    main()
