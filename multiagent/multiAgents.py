# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        foodDistance = []
        ghostDistance = []
        foodList = currentGameState.getFood().asList()
        pacmanPos = list(successorGameState.getPacmanPosition())

        for ghost in newGhostStates:
            ghostDistance.append(manhattanDistance(ghost.getPosition(), pacmanPos))

        for ghostDist in ghostDistance:
            if ghostDist <= 1:
                return float('-inf')

        for food in foodList:
            foodDistance.append(-1 * manhattanDistance(food, pacmanPos))

        return max(foodDistance)

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.
        
          gameState.getLegalActions(agentIndex):
            #Returns a list of legal actions for an agent
            #agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            #Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            #Returns the total number of agents in the game
        """

        "*** YOUR CODE HERE ***"
        minimaxval = []
        legalaction = gameState.getLegalActions(0)
        for action in legalaction:
            v = self.minimax(gameState.generateSuccessor(0, action), 1, 0)
            minimaxval.append((v, action))
        return max(minimaxval)[1]

    def minimax(self, gameState, agent, depth):

        if agent >= gameState.getNumAgents():
            agent = 0
            depth += 1

        if depth == self.depth:
            return self.evaluationFunction(gameState)

        legalactions = gameState.getLegalActions(agent)

        if not legalactions:
            return self.evaluationFunction(gameState)

        minimaxvals = []

        if agent == 0:
            for action in legalactions:
                v = self.minimax(gameState.generateSuccessor(agent, action), agent + 1, depth)
                minimaxvals.append((v, action))
            return max(minimaxvals)[0]

        else:
            for action in legalactions:
                v = self.minimax(gameState.generateSuccessor(agent, action), agent + 1, depth)
                minimaxvals.append((v, action))
            return min(minimaxvals)[0]

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def expectation(self, a, n):
        prb = 1.0 / n
        sum = 0
        for i in range(0,n):
            sum += (a[i] * prb)
        return float(sum)

    def expvalue(self, gameState, agent, depth):

        if agent >= gameState.getNumAgents():
            agent = 0
            depth += 1

        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        legalactions = gameState.getLegalActions(agent)

        if agent == 0:
            v = float("-inf")
            for action in legalactions:
                v = max(v, self.expvalue(gameState.generateSuccessor(agent, action), agent + 1, depth))
            return v
        else:
            v = []
            for action in legalactions:
                expectivals = self.expvalue(gameState.generateSuccessor(agent, action), agent + 1, depth)
                v.append(expectivals)
            return self.expectation(v,len(legalactions))

    def getAction(self, gameState):

        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"

        expectimaxvals = []
        legalactions = gameState.getLegalActions(0)

        for action in legalactions:
            v = self.expvalue(gameState.generateSuccessor(0, action),1,0)
            expectimaxvals.append((v, action))

        bestIndices = []

        for index in range(len(expectimaxvals)):
            if expectimaxvals[index] == max(expectimaxvals):
                bestIndices.append(index)

        selectindex = random.choice(bestIndices)

        return expectimaxvals[selectindex][1]

def betterEvaluationFunction(currentGameState):

    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: For calculating a better evaluation function I have divided the function
                    into two parts i.e distance to food and capsule.

                    For food , the distance to food is inverted and added to state score.
                    For pallet/capsule, the distance is multiplied with a factor of 2 and subtracted from state score.
    """
    "*** YOUR CODE HERE ***"

    position = currentGameState.getPacmanPosition()
    foods = currentGameState.getFood().asList()
    newcaps = currentGameState.getCapsules()
    tempfood = []

    score = currentGameState.getScore()

    # Considering the food locations
    if foods:
        for f in foods:
            tempfood.append(manhattanDistance(position,f))
        closestFoodDis = min(tempfood)
    else:
        closestFoodDis = 0.5

    score = score + 1.0 / closestFoodDis

    # Considering the capsule location
    for capsule in newcaps:
        score = score - (2 * manhattanDistance(capsule, list(position)))

    return score

# Abbreviation
better = betterEvaluationFunction

