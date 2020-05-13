#!/usr/bin/env python
# coding: utf-8
# @Author: Tushar Kakkar

from pandas import *
import pprint
from os import system
import sys
import time
import copy


# In[233]:


def findImmutableCoord(bigGrid):
    outList = []
    
    for i in range(len(bigGrid)):
        for j in range(len(bigGrid[0])):
            if bigGrid[i][j] != 0:
                outList.append((i, j))
    
    return outList


# In[211]:


def prepBoard():
    
    '''
    #easy
    return \
    [[0, 6, 0, 3, 0, 0, 8, 0, 4], \
     [5, 3, 7, 0, 9, 0, 0, 0, 0], \
     [0, 4, 0, 0, 0, 6, 3, 0, 7], \
     [0, 9, 0, 0, 5, 1, 2, 3, 8], \
     [0, 0, 0, 0, 0, 0, 0, 0, 0], \
     [7, 1, 3, 6, 2, 0, 0, 4, 0], \
     [3, 0, 6, 4, 0, 0, 0, 1, 0], \
     [0, 0, 0, 0, 6, 0, 5, 2, 3], \
     [1, 0, 2, 0, 0, 9, 0, 8, 0]] 
    '''
    
    
    '''
    #Hard
    return \
    [[0, 7, 0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 8, 0, 0], \
     [2, 0, 6, 0, 9, 1, 4, 0, 0], \
     [0, 0, 0, 9, 0, 0, 0, 6, 0], \
     [0, 1, 5, 0, 0, 7, 0, 4, 0], \
     [0, 8, 0, 0, 5, 0, 0, 9, 0], \
     [0, 3, 0, 4, 0, 0, 0, 0, 0], \
     [0, 0, 8, 0, 6, 0, 7, 0, 0], \
     [7, 0, 0, 0, 3, 0, 0, 1, 9]]
     '''
    
    
    #Tough
    return \
    [[0, 0, 1, 0, 0, 6, 0, 8, 4], \
     [0, 0, 0, 0, 9, 0, 0, 0, 0], \
     [0, 0, 0, 3, 0, 0, 0, 5, 0], \
     [0, 0, 6, 0, 7, 1, 8, 0, 0], \
     [0, 0, 3, 0, 0, 0, 0, 0, 6], \
     [2, 1, 0, 9, 0, 0, 0, 0, 0], \
     [9, 0, 0, 0, 0, 0, 0, 7, 0], \
     [3, 0, 4, 0, 0, 0, 0, 6, 0], \
     [0, 0, 5, 0, 0, 0, 0, 0, 0]] 
       
        
    
    '''
    #Toughest Taken from Wikipedia 
    #https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#/media/File:Sudoku_puzzle_hard_for_brute_force.svg
    
    return \
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 3, 0, 8, 5], \
     [0, 0, 1, 0, 2, 0, 0, 0, 0], \
     [0, 0, 0, 5, 0, 7, 0, 0, 0], \
     [0, 0, 4, 0, 0, 0, 1, 0, 0], \
     [0, 9, 0, 0, 0, 0, 0, 0, 0], \
     [5, 0, 0, 0, 0, 0, 0, 7, 3], \
     [0, 0, 2, 0, 1, 0, 0, 0, 0], \
     [0, 0, 0, 0, 4, 0, 0, 0, 9]]
    '''

# In[180]:


def getGridOrigionByElementLoc(x, y):
    return getOriginCoord(x), getOriginCoord(y)


# In[118]:


def getOriginCoord(number):
    if number < 3:
        return 0
    elif number > 2 and number < 6:
        return 3
    else:
        return 6


# In[178]:


def gridToList(bigGrid, origin):
    x = origin[0]
    y = origin[1]
    li = list()
    
    for i in [a[y : y + 3] for a in grid[x : x + 3]]:
        li += i
    
    return li


# In[182]:


def colToList(bigGrid, column):
    return [a[column] for a in bigGrid]


# In[184]:


def verifyList(li, element):
    return element in li

# In[226]:


def debugPrint(grid, i, j, k):
    print ('gridToList: ', gridToList(grid, getGridOrigionByElementLoc(i, j)))
    print ('colToList: ', colToList(grid, i))
    print ('row: ', grid[i])

#%%
def progressBar(i, j, prog):
    retVal = prog
    
    calc = i * 10 + j
    
    if calc > prog:
        retVal = calc
        #print(i, j, retVal)
        sys.stdout.write("=")
        sys.stdout.flush()    
    
    return retVal

#%%
def progressBar2(i, j, oldI, oldJ):
    
    calc = i * 10 + j
    calcOld = oldI * 10 + oldJ
    
    if calcOld > calc:
        sys.stdout.write("\b" * (calcOld - calc))
        sys.stdout.write(" " * (calcOld - calc))
        sys.stdout.write("\b" * (calcOld - calc))
    elif calc > calcOld: 
        sys.stdout.write("=" * (calc - calcOld))
        
    sys.stdout.flush()  
    
    return i, j
    
#%%
def outputHeader():
    _ = system('cls')
    print ("Sudoku Solver...\n")
    print ("Problem:")
    print (DataFrame(gridOrig).to_string(index=False, header=False).replace('0', '_'))  

# In[239]:

showProgressBar = True
grid = prepBoard()
gridOrig = copy.deepcopy(grid)
immuCoord = findImmutableCoord(grid)
timeWasted = 0

#pp = pprint.PrettyPrinter()
#pp.pprint(grid)

outputHeader()

if showProgressBar:
    sys.stdout.write("\n[%s]" % (" " * 80))
    sys.stdout.flush()  
    sys.stdout.write("\b" * (80+1))

i = 0
direction = 1
progressIJ = 0
lastI = 0
lastJ = 0
ts = time.time()


while i < 9:
    if direction == -1: 
        j = 8
    else:
        j = 0
            
    while j < 9:

        if showProgressBar:
            progressIJ = progressBar(i, j, progressIJ)
            #lastI, lastJ = progressBar2(i, j, lastI, lastJ)
        
        if j == -1:
            break
            
        if (i, j) in immuCoord:
            j += direction
            continue
            
        if direction == -1 and grid[i][j] == 9:
            grid[i][j] = 0
            j += direction
            continue
        
        cellNum = grid[i][j]
        direction = 1
        for k in range(1, 10):    
            if cellNum == 0:
                cellNum = 1
        
            z1 = gridToList(grid, getGridOrigionByElementLoc(i, j))
            z2 = colToList(grid, j)
            z3 = grid[i]
               
            if cellNum in z1 or cellNum in z2 or cellNum in z3: 
                cellNum += 1
                if cellNum > 9:
                    grid[i][j] = 0
                    break
            else:
                grid[i][j] = cellNum
                break
        
        if grid[i][j] == 0:
            direction = -1
        
        j += direction

    
    if not showProgressBar:
        timeWastageStart = time.time()
        outputHeader()
        print ('\nSolution in progress...')
        print (DataFrame(grid).to_string(index=False, header=False).replace('0', '_'))              
        timeWasted += time.time() - timeWastageStart
    
    i += direction

timeNow = time.time()
timeTaken = timeNow - ts - timeWasted

sys.stdout.write("\n")
sys.stdout.flush()

if not showProgressBar:
    outputHeader()
    
print ("\nFinal Output:")
print (DataFrame(grid).to_string(index=False, header=False))
print ("\nTime taken: " + str(timeTaken) + " seconds")
print ("Original Time: ", ts)
print ("Time Now: ", timeNow)
print ("Time Wasted: ", timeWasted)