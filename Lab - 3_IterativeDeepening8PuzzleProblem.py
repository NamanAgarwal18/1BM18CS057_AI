# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 09:45:32 2020

@author: Naman
"""

src = [[1,2,3],[-1,4,6],[7,5,8]]    
target = [[1,2,3],[4,5,6],[7,8,-1]] 

def equate(src,target):
    for i in range(3):
        for j in range(3):
            if src[i][j] != target[i][j]:
                return False
    return True

def find(state):
    
    for i in range(3):
        for j in range(3):
            if state[i][j] == -1:
                return (i,j)

def dfs(src,target,limit,visited_states):
    if equate(src,target):
        #for move in visited_states:
         #   display(move)
        return True
    if limit <= 0:
        return False
    visited_states.append(src)
    (moves,moving) = possibleMoves(src,visited_states)   
    i = 0
    for move in moves:
        display(move,moving[i])
        i = i+1
        if dfs(move, target, limit-1, visited_states):
            return True
    print("------------------------------------------")
    return False

def duplicate(state):
    temp = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            temp[i][j] = state[i][j]
    return temp

def possibleMoves(state,visited_states): 
    (i,j) = find(state)  
    allPossibleMoves = []
    moving = []
    if i != 0 :                             #move up
        temp1 = duplicate(state)
        temp1[i][j] = temp1[i-1][j]
        temp1[i-1][j] = -1
        allPossibleMoves.append(temp1)
        moving.append("Up")
    if i != 2:                              #move down
        temp2 = duplicate(state)
        temp2[i][j] = temp2[i+1][j]
        temp2[i+1][j] = -1
        allPossibleMoves.append(temp2)
        moving.append("Down")
    if j != 2:                              #move right
        temp3 = duplicate(state)
        temp3[i][j] = temp3[i][j+1]
        temp3[i][j+1] = -1
        allPossibleMoves.append(temp3)
        moving.append("Right")
    if j!= 0:                               #move left
        temp4 = duplicate(state)
        temp4[i][j] = temp4[i][j-1]
        temp4[i][j-1] = -1
        allPossibleMoves.append(temp4)
        moving.append("Left")
    return ([move for move in allPossibleMoves if move not in visited_states],moving)



def iddfs(src,target,depth):
    for i in range(depth):
        visited_states = []
        if dfs(src,target,i+1,visited_states):
            #for move in visited_states:
                #display(move)
            return True
    return False

def display(state,move):
    
    for i in range(3):
        for j in range(3):
            if state[i][j]!=-1 :
                print(state[i][j], end='\t')
            else:
                print("_", end='\t')
        print()
    #print("Move: " , move)
    print()
    print()

def main():
    for i in range(1, 100):
        val = iddfs(src,target,i)
        if val == True:
            #val = iddfs(src,target,i)
            print("------------------------------------------")
            print("Depth - ",i," -> ", val)
            print("------------------------------------------")
            break
        print("Depth - ",i," -> ", val)
        print("------------------------------------------")
main()