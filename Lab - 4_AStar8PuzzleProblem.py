# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:42:22 2020

@author: Naman
"""

import random as r
puzzle=[[-1,1,3],[4,2,5],[7,8,6]]
result=[[1,2,3],[4,5,6],[7,8,-1]]


#Puzzle -> [[1,2,3],[4,5,6],[7,8,-1]]
#Arr[] ->[puzzle,depth,h,action,fn]


def compare(puz):
    count = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != -1:          
                if puz[i][j] != result[i][j]:
                    count = count+1
    return count

def findBlank():
    global puzzle
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == -1:
                return (i,j)
            
def copy(puz):
    duplicate = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            duplicate[i][j] = puz[i][j]
    return duplicate

def checkAll(Arr,depth,past):
    global puzzle,result
    #arrPuzzle = [[]]
    fn = 999
    (i,j) = findBlank()
    
    if i!=0 and past!='D' :                                                     #Move Up 
        arrPuzzle = copy(puzzle)
        arrPuzzle[i][j] = arrPuzzle[i-1][j]
        arrPuzzle[i-1][j] = -1
        hold  = compare(arrPuzzle)
        action  = 'U'
        if fn > (depth+1+hold): 
            array = copy(arrPuzzle)
            h = hold
            newAction = action
            fn = depth+1+hold
        elif fn == (depth+1+hold) and r.choice([True,False]):
            array = copy(arrPuzzle)
            h = hold
            newAction = action
            fn = depth+1+hold
        
    if j!=0 and past!='R':                                                      #Move Left
        arrPuzzle = copy(puzzle)
        arrPuzzle[i][j] = arrPuzzle[i][j-1]
        arrPuzzle[i][j-1] = -1
        hold  = compare(arrPuzzle)
        action  = 'L'
        if fn > (depth+1+hold): 
            array = copy(arrPuzzle)
            h = hold
            newAction = action
            fn = depth+1+hold
        elif fn == (depth+1+hold) and r.choice([True,False]):
            array = copy(arrPuzzle)
            h = hold
            newAction = action
            fn = depth+1+hold
            
    if i!=2 and past!='U':                                                      #Move Down
        arrPuzzle = copy(puzzle)
        arrPuzzle[i][j] = arrPuzzle[i+1][j]
        arrPuzzle[i+1][j] = -1
        hold  = compare(arrPuzzle)
        action  = 'D'
        if fn > (depth+1+hold): 
            array = copy(arrPuzzle)
            h = hold
            newAction = action
            fn = depth+1+hold
        elif fn == (depth+1+hold) and r.choice([True,False]):
            array = copy(arrPuzzle)
            h = hold
            newAction = action
            fn = depth+1+hold
            
    if j!=2 and past!='L':                                                      #Move Right
        arrPuzzle = copy(puzzle)
        arrPuzzle[i][j] = arrPuzzle[i][j+1]
        arrPuzzle[i][j+1] = -1
        hold  = compare(arrPuzzle)
        action  = 'R'
        if fn > (depth+1+hold): 
            array = copy(arrPuzzle)
            h = hold
            newAction = action
            fn = depth+1+hold
        elif fn == (depth+1+hold) and r.choice([True,False]):
            array = copy(arrPuzzle)
            h = hold
            newAction = action
            fn = depth+1+hold
            
    depth = depth+1   
    puzzle = copy(array)
    Arr.append([puzzle,depth,h,newAction,fn])
    return Arr

def printing(Arr):
    for k in range(len(Arr)):
        temp = Arr[k]
        puz = temp[0]
        for i in range(3):
            for j in range(3):
                if puz[i][j] == -1:
                    print(" ",end= '\t')
                else:
                    print(puz[i][j],end='\t')
            print('\n')
        print("g(n) is: ", temp[1] , ", h(n) = ", temp[2], ", F(n): ", temp[4],"And Moved: ", temp[3])
    
def aStar(Arr):
    temp = Arr[len(Arr)-1]
    puz = temp[0]
    depth = temp[1]
    h = temp[2]
    action = temp[3]
    fn = temp[3]
    #printing(Arr)
    #print("\n\n\n")
    if h == 0:
        printing(Arr)
        return True
    elif depth > 15:
        printing(Arr)
        return False
    
    Arr = checkAll(Arr = Arr, depth = depth, past = action)
    aStar(Arr = Arr)
    
def depth():
    global puzzle,result
    Arr = [[puzzle,0,compare(puzzle),'_',compare(puzzle)]]
    #printing(Arr)
    Arr = aStar(Arr)
    if Arr == False:
        print("Unsuccessful")
    else:
        #printing(Arr)
        print("Successful")
    return

def main():
    global puzzle
    print("Enter the puzzle")
    for i in range(3):
        for j in range(3):
            d = int(input("Enter: "))
            puzzle[i][j] = d
    depth()
main()
    
    
    
    
    