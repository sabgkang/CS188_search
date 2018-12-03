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
    #print "is (1,1) the goal", problem.isGoalState((1,1))
    return  [s, s, w, s, w, w, s, w]

#-----Paul Kang------------------
#global variables
actionsList =[]
testSteps = 0
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
    "*** YOUR CODE HERE ***"
    global actionsList

    actions = util.Stack()
    rope = util.Stack()
    
    here = problem.getStartState() 
 
    findNextDFS(problem, rope, actions, here)

    shortestPath = 0  
    for i in range(len(actionsList)):
        print "*** Path:", i, len(actionsList[i])
        if len(actionsList[i]) <= len(actionsList[shortestPath]):
            shortestPath = i
    
    print "Use steps:", testSteps, "Found ", len(actionsList), "pathes. Choose #", shortestPath  
    print "Shortest actions:",actionsList[shortestPath]
    return  actionsList[shortestPath]
    util.raiseNotDefined()

def findNextDFS(problem, rope, actions, here):
    global actionsList
    global testSteps
    
    if problem.isGoalState(here):
        actionsCopy = list(actions.list)
        actionsList.append(actionsCopy)
        actions.pop()
        return
    
    #move one step
    rope.push(here)
    successors = problem.getSuccessors(here)
      
    for successor in successors:
        nextFound = False
        nextPos = successor[0]

        posMark=False
        for pos in rope.list:
            if pos == nextPos:
                posMark = True
                
        if posMark == False:
            limit = 20000    
            if testSteps == limit:
                print "stop at step#", limit
                return False
            
            else:
                testSteps += 1
                actions.push(successor[1])
                nextFound = findNextDFS(problem, rope, actions, nextPos)
    
    if here == problem.getStartState():
        return

    else: #move one step
        if not actions.isEmpty():
            actions.pop()          
            rope.pop() 
            
    return    
#---------------------------------

#-----Paul Kang------------------    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    searchList = []
    
    start = problem.getStartState()

    here=[None, None, start] #[pre, actionTohere, here]
    searchList.append(here)
    findNextBFS(problem, searchList, 0)
    
    for index in range(len(searchList)):
        if problem.isGoalState(searchList[index][2]):
            break
    
    print index
    actions=util.Queue()
    composeActions(searchList, actions, index) 
    return actions.list
    
    #util.raiseNotDefined()

def composeActions(searchList, actions, index):
    actions.push(searchList[index][1])
    
    prevIndex = searchList[index][0]
    if prevIndex ==0: return
    composeActions(searchList, actions, prevIndex)

def findNextBFS(problem, searchList, index): 
    global testSteps
    

    if problem.isGoalState(searchList[index][2]):
        print "********************goal*****"
        return
    
    
    limit = 10000    
    if testSteps == limit:
        print "stop at step#", limit
        print aaa
        return False
            
    else:
        testSteps += 1
        
    successors = problem.getSuccessors(searchList[index][2])
    
    for successor in successors:
        
        for state in searchList:
            #print "*****state", state[2], "next",successor[0]
            nextVisited = False
            if state[2] == successor[0]:
                nextVisited = True
                #print state[2], "next is visited"
                break
                
        if nextVisited == False:
            nextState = [index, successor[1], successor[0]]
            searchList.append(nextState)
    
    index +=1
    findNextBFS(problem, searchList, index)
    
    
    
#-----------------------

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch