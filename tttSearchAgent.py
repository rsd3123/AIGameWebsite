'''
Tic Tac Toe Search Agent
Minimax algorithm
Rudy DeSanti
March 31, 2022
Return what square on the board (numbered 0-8) to place an 'O' in.
'''
#Make AI chose a random path on tie

#Implement number of moves into score
import math
from random import Random, random, randrange
import sys



def Max(board):

    #Get Valid Moves
    actions = getValidMovesMax(board)

    #Base Case
    #If action is null, score is not none, then leaf
    score = scoreBoard(board['board'])
    if not actions or score != None:
        return {'board': board['board'], 'square':board['square'], 'score': score}

    #for each action
    currentHighest = None
    currentAction = None 
    currentBoard = None
    for action in actions:
        temp = Min(action)
        mistakeMade = False
        currentChance = random()
        if chanceToNotMakeMistake  < currentChance:
            mistakeMade = True

        if currentHighest == None or (temp['score'] > currentHighest and not mistakeMade):
            currentHighest = temp['score']
            currentAction = temp['square']
            currentBoard = temp['board']
    
    return {'board':currentBoard, 'square':currentAction, 'score':currentHighest}
        
def Min(board):

    #Get Valid Moves
    actions = getValidMovesMin(board)

    #Base Case
    #If action is null, score
    score = scoreBoard(board['board'])
    if not actions or score != None:
        return {'board': board['board'], 'square':board['square'], 'score': score}

    #for each action
    currentLowest = None
    currentAction = None 
    currentBoard = None
    for action in actions:
        temp = Max(action)
        if currentLowest == None or temp['score'] < currentLowest:
            currentLowest = temp['score']
            currentAction = temp['square']
            currentBoard = temp['board']
    
    return {'board':currentBoard, 'square':currentAction, 'score':currentLowest}  


def getValidMovesMax(board):
    actions = []

    for i in range(len(board['board'])):
        if board['board'][i] == 'empty':
            newBoard = board['board'][:]
            
            newBoard[i] = "O"
            if board['square'] == None:
                actions.append({'board': newBoard, 'square':i, 'score': None})
            else:
                actions.append({'board': newBoard, 'square':board['square'], 'score': None})

    return actions

def getValidMovesMin(board):
    actions = []

    for i in range(len(board['board'])):
        if board['board'][i] == 'empty':
            newBoard = board['board'][:]
            
            newBoard[i] = "X"
            if board['square'] == None:
                actions.append({'board': newBoard, 'square':i, 'score': None})
            else:
                actions.append({'board': newBoard, 'square':board['square'], 'score': None})

    return actions

def scoreBoard(board):
    
    numOfEmptySpaces = 0
    for i in range(len(board)):
        if(board[i] == 'empty'):
            numOfEmptySpaces = numOfEmptySpaces + 1
    
    #Return 1 for win, -1 for loss, 0 for tie
    if board[0] != 'empty' and ((board[0] == board[1] and board[1] == board[2]) or (board[0] == board[3] and board[3] == board[6])):
        if(board[0] == 'X'):
           return -1
        elif(board[0] == 'O'):
            return 1 + numOfEmptySpaces
         
    elif board[4] != 'empty' and ((board[3] == board[4] and board[4] == board[5]) or (board[1] == board[4] and board[4] == board[7]) or (board[2] == board[4] and board[4] == board[6]) or (board[0] == board[4] and board[4] == board[8])):
        if(board[4] == 'X'):
            return -1
        elif(board[4] == 'O'):
           return 1 + numOfEmptySpaces
    
    elif board[8] != 'empty' and ((board[6] == board[7] and board[7] == board[8]) or (board[2] == board[5] and board[5] == board[8])):
        if(board[8] == 'X'):
            return -1
        elif(board[8] == 'O'):
            return 1 + numOfEmptySpaces
            
    #Board full, no one wins
    elif board[0] != 'empty' and board[1] != 'empty' and board[2] != 'empty' and board[3] != 'empty' and board[4] != 'empty' and board[5] != 'empty' and board[6] != 'empty' and board[7] != 'empty' and board[8] != 'empty':
        return 0
    
    #If not anything
    else:
        return None
        
def main():
    global chanceToNotMakeMistake
    argument = sys.argv[1]
    difficulty = sys.argv[2]

    if difficulty == "impossible":
        chanceToNotMakeMistake = 1
    elif difficulty == "hard":
        chanceToNotMakeMistake = .75
    elif difficulty == "medium":
        chanceToNotMakeMistake = .50
    elif difficulty == "easy":
        chanceToNotMakeMistake = .25
        
    #Split up argument string into array
    board = argument.split(',')

    #Start recursive call
    answer = Max({'board': board, 'square': None, 'score': None})
    print(answer['square'])
 
if __name__ == '__main__':
    main()