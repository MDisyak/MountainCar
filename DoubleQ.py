import blackjack
from pylab import *
#324 num tiles


def learn(alpha, eps, numTrainingEpisodes):
    returnSum = 0.0
    for episodeNum in range(numTrainingEpisodes):
        G = 0
        currentState = blackjack.init()
        terminate = False
        while not terminate:
            if randint(0,101) > eps*100:#greedy action
                action = argmax(theta1[currentState] + theta2[currentState])
            else:#Epsilon action (explore)
                action = randint(0,2)
            G, nextState = blackjack.sample(currentState, action)
            if randint(0,2) == 0:#0.5 probability
                theta1[currentState, action] = theta1[currentState, action] + alpha * (G + theta2[nextState, argmax(theta1[nextState])] - theta1[currentState, action])
            else:#0.5 probability
                theta2[currentState, action] = theta2[currentState, action] + alpha * (G + theta1[nextState, argmax(theta2[nextState])] - theta2[currentState, action])
            currentState = nextState
            if not nextState:
                terminate = True
            #print("Episode: ", episodeNum, "Return: ", G)

        returnSum = returnSum + G
        #if episodeNum % 10000 == 0 and episodeNum != 0:
            #print("Average return so far: ", returnSum/episodeNum)
    #print (returnSum/numTrainingEpisodes)

def evaluate(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
        G = 0
        currentState = blackjack.init()
        terminate = False
        while not terminate:
            action = policy(currentState)
            G, nextState = blackjack.sample(currentState, action)
            currentState = nextState
            if not nextState:
                terminate = True
        returnSum = returnSum + G
    return returnSum / numEvaluationEpisodes

def policy(state):
    return argmax(theta1[state] + theta2[state])


def qHat(state, action, weightVector):


    return

learn(0.0001, 0.5, 1000000)
blackjack.printPolicy(policy)
print("Evaluation of policy is: ", evaluate(1000000))

