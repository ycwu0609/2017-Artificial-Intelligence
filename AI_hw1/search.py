# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# P2-1
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    
    "[Project 2] YOUR CODE HERE"
    state=problem.getStartState()
    TheStack = util.Stack()
    visited= set()
    visited.add(state)
    TheStack.push((state,[]))
    
    while not TheStack.isEmpty():
        CurrentNode=TheStack.pop()
        #state is CurrentNode[0],path is CurrentNode[1]
        if problem.isGoalState(CurrentNode[0]):
            return CurrentNode[1]

        #Child=problem.getSuccessors(CurrentNode[0])
        for Child in problem.getSuccessors(CurrentNode[0]):
            #ChildState=Child[0]
            #ChildAction=Child[1]
            tempPath = list()
            if Child[0] not in visited:
                visited.add(Child[0])
                tempPath.extend(CurrentNode[1])
                tempPath.append(Child[1])
                TheStack.push((Child[0],tempPath))
                if problem.isGoalState(Child[0]):
                    visited.remove(Child[0])
        
    util.raiseNotDefined()

# P2-2
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    "[Project 2] YOUR CODE HERE"    
    
    state=problem.getStartState()#get start state coordinate
    TheQueue=util.Queue()
    TheQueue.push((state,[]))
    visited=set()
    visited.add(state)
    
    while not TheQueue.isEmpty():
        current=TheQueue.pop()
        
        if problem.isGoalState(current[0]):
            return current[1]
        for child in problem.getSuccessors(current[0]):
            
            #temppath=list(path)#record the hole path
            tempPath = list()
            if  child[0] not in visited:#not yet visit
                visited.add(child[0])
                tempPath.extend(current[1])
                tempPath.append(child[1])
                TheQueue.push((child[0],tempPath))            
                
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# P2-3
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "print heuristic(problem.getStartState(), problem)"
    
    "[Project 2] YOUR CODE HERE"
    start=problem.getStartState()#get start state coordinate
    ThePriorityQueue=util.PriorityQueue()
    ThePriorityQueue.push((start,[]),0)
    visited=set()
    visited.add(start)
    
    while not ThePriorityQueue.isEmpty():
        current=ThePriorityQueue.pop()
        #current[0] is current state,current[1] is the path
        if problem.isGoalState(current[0]):
            return current[1]
        successors=problem.getSuccessors(current[0])
        for succ in successors:
            #succ[0] is coordinate,succ[1] is direction
            heuristicCost=heuristic(succ[0],problem)
            tempPath = list()
            if succ[0] not in visited:
                visited.add(succ[0])
                tempPath.extend(current[1])
                tempPath.append(succ[1])
                totalCost=problem.getCostOfActions(tempPath)+heuristicCost
                ThePriorityQueue.push((succ[0],tempPath),totalCost)
                if problem.isGoalState(succ[0]):
                    visited.remove(succ[0])
    util.raiseNotDefined()


# Abbreviations
astar = aStarSearch
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
