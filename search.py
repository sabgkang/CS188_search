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

#--------------------------------
"""
class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0
"""
actionsList =[]
stoneMap = []
testSteps = 0

def myMazeSearch5(problem):
    global actionsList
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """

    actions = util.Stack()
    #rope = []
    rope = util.Stack()
    
    start = problem.getStartState() 
 
    findNext5(problem, rope, actions, start)
    #print rope
    #print "Final", actionsList
    shortestPath = 0
    
    for i in range(len(actionsList)):
        print "*** Path:", i, len(actionsList[i])
        if len(actionsList[i]) <= len(actionsList[shortestPath]):
            #print "shorter"
            shortestPath = i
    
    print "Use steps:", testSteps, "Found ", len(actionsList), "pathes. Choose #", shortestPath  
    print actionsList[shortestPath]
    return  actionsList[shortestPath]

def findNext5(problem, rope, actions, start):
    global actionsList
    global testSteps
    
    #print "***", start, actions.list
    if problem.isGoalState(start):
        #print "*********** Goal ****"
        #a_copy = list(actions.list)
        a_copy = list(actions.list)
        actionsList.append(a_copy)
        #print actions.list
        
        #popAction(actions)
        actions.pop()
        
        #print actionsList
        #print test
        #goal = True
        return
    
    #pushToRope(rope, start)
    rope.push(start)
    #print "*******",testSteps
    #print rope
    successors = problem.getSuccessors(start)
      
    for successor in successors:
        nextFound = False
        nextPos = successor[0]

        posMark=False
        for pos in rope.list:
            #print "compare", pos, nextPos
            #if (pos[0],pos[1]) == nextPos:
            if pos == nextPos:
                posMark = True
                
        if posMark == False:
            #print "next found at ", nextPos, "steps", testSteps
            limit = 20000    
            if testSteps == limit:
                print "stop at step#", limit
                return False
            
            else:
                testSteps += 1
                #pushAction(actions, successor[1])
                actions.push(successor[1])
                #print actions
                nextFound = findNext5(problem, rope, actions, nextPos)
                #print "*****back to", start, "From", nextPos
    
    #print start, "serch is over", actions
    if start == problem.getStartState():
        #print "Back to start"
        return

    else:
        #if actions.len()>0: 
        if not actions.isEmpty():
            #popAction(actions)
            actions.pop()
            
            rope.pop()
            #popFromRope(rope)
            
        #print start, "nowhere to go", actionsList 
        
    return

def myMazeSearch1(problem):
    global actionsList
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    

    actions = initActionArray()
    start = problem.getStartState() #(x,y) = (col, row)
    print start

    #Search all root's succesors
    successors = problem.getSuccessors(start)
    for successor in successors:
		stones2 = [] ##(x,y) starts from (1,1), for findNext2
		stones2.append(start)
		nextPos = successor[0]
		pushAction(actions, successor[1])
		findNext2(problem, stones2, actions, nextPos, 1)
    #end of Search all root's succesors
    
    #Search NOT all root's succesors, use stones1/findNext1 or stones2/findNext2
    #stones1 = initFlagArray(50,50) #(x,y) starts from (1,1), for findNext1
    #stones2 = [] ##(x,y) starts from (1,1), for findNext2    
    #findNext1(problem, stones1, actions, start, 1)
    #findNext2(problem, stones2, actions, start, 1)
    #end of Search NOT all root's succesors
    
    print actionsList
    shortestPath = 0
    for i in range(len(actionsList)):
        if len(actionsList[i]) <= len(actionsList[shortestPath]):
            shortestPath = i
                
    return  actionsList[shortestPath]

def myMazeSearch4(problem):
    global actionsList
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    

    actions = initActionArray()
    start = problem.getStartState() #(x,y) = (col, row)

    rope = []   
    findNext4(problem, rope, actions, start)
 
    #print "Final", actionsList
    shortestPath = 0
    
    for i in range(len(actionsList)):
        #print "*****", i, len(actionsList[i])
        if len(actionsList[i]) <= len(actionsList[shortestPath]):
            #print "shorter"
            shortestPath = i
    
    print "Use steps:", testSteps, "Found ", len(actionsList), "pathes. Choose #", shortestPath  

    return  actionsList[shortestPath]

def findNext4(problem, rope, actions, start):
    global actionsList
    global testSteps
    
    if problem.isGoalState(start):
        #print "*********** Goal ****"
        a_copy = list(actions)
        actionsList.append(a_copy)
        #print actions
        popAction(actions)
        #print actionsList
        #print test
        #goal = True
        return
    
    pushToRope(rope, start)
    #print "*******",testSteps
    #print rope
    successors = problem.getSuccessors(start)
      
    for successor in successors:
        nextFound = False
        nextPos = successor[0]

        posMark=False
        for pos in rope:
            #print "compare", pos, nextPos
            if (pos[0],pos[1]) == nextPos:
                posMark = True
                
        if posMark == False:
            #print "next found at ", nextPos, "steps", testSteps
            limit = 20000    
            if testSteps == limit:
                print "stop at step#", limit
                return False
            
            else:
                testSteps += 1
                pushAction(actions, successor[1])
                #print actions
                nextFound = findNext4(problem, rope, actions, nextPos)
                #print "*****back to", start, "From", nextPos
    
    #print start, "serch is over", actions
    if start == problem.getStartState():
        #print "Back to start"
        return

    else:
        if len(actions) >0: 
            popAction(actions)
            popFromRope(rope)
            
        #print start, "nowhere to go" 
        
    return

def myMazeSearch3(problem):
    global actionsList
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    

    actions = initActionArray()
    start = problem.getStartState() #(x,y) = (col, row)
    print start

    #Search all root's succesors
#    successors = problem.getSuccessors(start)
#    for successor in successors:
#		stones2 = [] ##(x,y) starts from (1,1), for findNext2
#		stones2.append(start)
#		nextPos = successor[0]
#		pushAction(actions, successor[1])
#		findNext2(problem, stones2, actions, nextPos, 1)
    #end of Search all root's succesors
    
    stones3 = [] ##(x,y) starts from (1,1), for findNext2    
    findNext3(problem, stones3, actions, start, 1)

    
    print actionsList
    shortestPath = 0
    for i in range(len(actionsList)):
        if len(actionsList[i]) <= len(actionsList[shortestPath]):
            shortestPath = i
                
    return  actionsList[shortestPath]

def findNext3(problem, stones, actions, start, testSteps):
    global actionsList
    global stoneMap
    if problem.isGoalState(start):
        print "*********** Goal ****"
        a_copy = list(actions)
        actionsList.append(a_copy)
        print actions
        popAction(actions)
        print actionsList

        goal = True
        return True
    
    stones.append(start)
    successors = problem.getSuccessors(start)
      
    for successor in successors:
        nextFound = False
        nextPos = successor[0]
        pushStones(stoneMap, stones)
        print "*******push",stones
        stoneMark=False
        for stone in stones:
            if stone == nextPos:
                stoneMark = True
                
        if stoneMark == False:
            print "next found at ", nextPos, "steps", testSteps
                
            if testSteps == 100:
                return False
            
            else:
                testSteps += 1
                pushAction(actions, successor[1])
                print actions
                nextFound = findNext3(problem, stones, actions, nextPos, testSteps)
                stones = list(popStones(stoneMap))
                print "*****pop", stones
                print "*****back to", start, "From", nextPos
    
    print start, "serch is over", actions
    if start == problem.getStartState():
        print "Back to start"

    else:
        if len(actions) >0: popAction(actions)
        print actions, start, "nowhere to go" 
        
    return

# stones map uses a list to be appended to
def findNext2(problem, stones, actions, start, testSteps):
    global actionsList

    if problem.isGoalState(start):
        print "*********** Goal ****"
        a_copy = list(actions)
        actionsList.append(a_copy)
        print actions
        popAction(actions)
        print actionsList

        goal = True
        return True
    
    stones.append(start)
    successors = problem.getSuccessors(start)
      
    for successor in successors:
        nextFound = False
        nextPos = successor[0]
        
        stoneMark=False
        for stone in stones:
            if stone == nextPos:
                stoneMark = True
                
        if stoneMark == False:
            print "next found at ", nextPos, "steps", testSteps
                
            if testSteps == 100:
                return False
            
            else:
                testSteps += 1
                pushAction(actions, successor[1])
                print actions
                nextFound = findNext2(problem, stones, actions, nextPos, testSteps)
                print "back to", start, "From", nextPos
    
    print start, "serch is over", actions
    if start == problem.getStartState():
        print "Back to start"

    else:
        if len(actions) >0: popAction(actions)
        print actions, start, "nowhere to go"          
            
    
# stones map uses a pre-allocated list
def findNext1(problem, stones, actions, start, testSteps):
    global actionsList

    if problem.isGoalState(start):
        print "*********** Goal ****"
        a_copy = list(actions)
        actionsList.append(a_copy)
        print actions
        popAction(actions)
        print actionsList

        goal = True
        return True
    
    stones[start[0]][start[1]] = 1
    successors = problem.getSuccessors(start)
      
    for successor in successors:
        nextFound = False
        nextPos = successor[0]
        if stones[nextPos[0]][nextPos[1]] == 0:
            #if goal == True: return True
            print "next found at ", nextPos, "steps", testSteps
                
            if testSteps == 100:
                return False
            else:
                testSteps += 1
                pushAction(actions, successor[1])
                print actions
                nextFound = findNext1(problem, stones, actions, nextPos, testSteps)
                print "back to", start, "From", nextPos
    
    print start, "serch is over", actions
    if start == problem.getStartState():
        print "Back to start"

    else:
        popAction(actions)
        print actions, start, "nowhere to go"          
        

def initActionArray():
    actions = []
    return actions
    
def pushStones(stoneMap, stones):
    stoneMap.append(list(stones))

def popStones(stoneMap):
    stonesPoped = stoneMap[-1]
    stoneMap.pop()
    return stonesPoped

def pushToRope(rope, pos):
    rope.append(list(pos))
    
def popFromRope(rope):
    posPoped = list(rope[-1])
    rope.pop()
    return posPoped

def pushAction(actions, actionToPush):
    actions.append(actionToPush)

def popAction(actions):
    actionPoped = actions[-1]
    actions.pop()
    return actionPoped

def initFlagArray(row,col):
    flags=[]
    for i in range(row):
        rowFlags=[]
        for j in range(col):
            rowFlags.append(0)
        flags.append(rowFlags)
        
    return flags
   
    
#---------------------------------
    
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
    print "Start:", problem.getStartState()
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

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
