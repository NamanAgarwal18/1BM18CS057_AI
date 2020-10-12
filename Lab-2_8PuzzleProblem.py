# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:10:04 2020

@author: Naman
"""

# Date :  09.10.2019
import random as r
puzzle=[[1,2,3],[-1,4,6],[7,5,8]]



#Puzzle -> [[1,2,3],[4,5,6],[7,8,None]]
#Arr[] -> [Puzzle, depth, hValue]
#ArrStore[] -> [Puzzle, depth, hValue]
#duplicateUp / duplicateDown / duplicateLeft / duplicateRight -> [Puzzle,hValue]
#Assend[] -> [duplicateUp]

def compare():
    count = 0
    counter = 1
    for i in range(3):
        for j in range(3):
            if counter == 9:
                break
            if puzzle[i][j] != counter:
                count = count +1
            counter  = counter + 1
    if counter == 0:
        return True
    return count

def findBlank():
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == -1:
                return (i,j)
            
def copy():
    global puzzle
    duplicate = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            duplicate[i][j] = puzzle[i][j]
    return duplicate

def copying(abc,cde):
    for i in range(3):
        for j in range(3):
            abc[i][j] = cde[i][j]
    return abc
        

def Assending(duplicateUp,duplicateDown,duplicateRight,duplicateLeft):
    #assend = [duplicateUp,duplicateDown,duplicateRight,duplicateLeft]
    assend = []
    if duplicateUp[2] == True:
        assend.append(duplicateUp)
    if duplicateDown[2] == True:
        assend.append(duplicateDown)
    if duplicateLeft[2] == True:
        assend.append(duplicateLeft)
    if  duplicateRight[2] == True:
        assend.append(duplicateRight)
    for i in range(assend.__len__()):
        for j in range(i+1,assend.__len__(),1):
            if assend[i][1] == assend[j][1]:
                if r.choice([True,False]):
                    temp = assend[i] 
                    assend[i] = assend[j]
                    assend[j] = temp
            if assend[i][1] >assend[j][1]:
                temp = assend[i] 
                assend[i] = assend[j]
                assend[j] = temp
    #for i in range(len(assend)):
     #   printed(assend[i][0])
    #print("end")
    return assend
    
    

def checkAll(ArrStore,depth,Arr):
    global puzzle
    duplicateUp,duplicateDown,duplicateRight,duplicateLeft = [None,555,False],[None,555,False],[None,555,False],[None,555,False]
    i,j = findBlank()
    if i!=0:
        puzzle[i][j] = puzzle[i-1][j]
        puzzle[i-1][j] = -1
        
        hold  = compare()
        duplicateUp[0] = copy()
        duplicateUp[1] = hold
        #print(hold)
        #printed(duplicateUp[0])
        puzzle[i-1][j] = puzzle[i][j]
        puzzle[i][j] = -1
        #printed(puzzle)
        duplicateUp[2] = True
    if j!=0:
        puzzle[i][j] = puzzle[i][j-1]
        puzzle[i][j-1] = -1
        hold  = compare()
        duplicateLeft[0] = copy()
        duplicateLeft[1] = hold
        #print(hold)
        puzzle[i][j-1] = puzzle[i][j]
        puzzle[i][j] = -1
        duplicateLeft[2] = True
    if i!=2:
        puzzle[i][j] = puzzle[i+1][j]
        puzzle[i+1][j] = -1
        hold  = compare()
        duplicateDown[0] = copy()
        duplicateDown[1] = hold
        #print(hold)
        puzzle[i+1][j] = puzzle[i][j]
        puzzle[i][j] = -1
        duplicateDown[2] = True
    if j!=2:
        puzzle[i][j] = puzzle[i][j+1]
        puzzle[i][j+1] = -1
        hold  = compare()
        duplicateRight[0] = copy()
        duplicateRight[1] = hold
        #print(hold)
        puzzle[i][j+1] = puzzle[i][j]
        puzzle[i][j] = -1
        duplicateRight[2] = True
    depth = depth+1
    Assend = Assending(duplicateUp = duplicateUp, duplicateDown = duplicateDown, duplicateRight = duplicateRight, duplicateLeft = duplicateLeft)
    #printed(Assend[0][0])
    Arr.append([Assend[0][0],depth,Assend[0][1]])
    
    for i in range(1,len(Assend),1):
        ArrStore.append([Assend[Assend.__len__() -  i][0],depth, Assend[Assend.__len__() -  i][1]])
    #ArrStore.append([Assend[3],depth])
    #ArrStore.append([Assend[2],depth])
    #ArrStore.append([Assend[1],depth])
    return (Arr,ArrStore)
        
def depthEfficient(ArrStore,Arr):
    
    global puzzle
    #depth = 0
    current = Arr[len(Arr)-1]
    #copying( abc = puzzle, cde = current[0])
    temp = current[0]
    for i in range(3):
        for j in range(3):
            puzzle[i][j] = temp[i][j]
    depth = current[1]
    h = current[2]
    
    if depth >= 15:
        #Abcde = [[-1],[Arr],[ArrStore]]
        #return Abcde
        #return (-1,Arr,ArrStore)
        return True
    elif h == 0:
        #Abcde = [[depth],[Arr],[ArrStore]]
        #return Abcde
        #return (depth,Arr,ArrStore)
        return False
    (Arr,ArrStore) = checkAll(ArrStore = ArrStore, depth = depth, Arr = Arr)
    puzzle = Arr[len(Arr)-1][0]
    depthEfficient(ArrStore = ArrStore, Arr = Arr)
    
def depthNonEfficient(ArrStore,Arr):
    global puzzle
    #foundOrNotFound,Arr,ArrStore = depthEfficient(ArrStore = ArrStore, Arr = Arr)
    #Abcde = []
    #Abcde = depthEfficient(ArrStore = ArrStore, Arr = Arr)
    #Arr = Abcde[1][0]
    #ArrStore = Abcde[2][0]
    #foundOrNotFound = Abcde[0][0]
    foundOrNotFound = depthEfficient(ArrStore = ArrStore, Arr = Arr)
    
    if foundOrNotFound:
        Arr.pop()
        printing(ArrStore)
        if len(ArrStore)==0:
            return False
        
        temp  = ArrStore.pop()
        
        while temp[2]>14:
            temp  = ArrStore.pop()
        Arr.pop()
        Arr.append(temp)
        puzzle = temp[0]
        depthNonEfficient(ArrStore = ArrStore, Arr = Arr) 
    else:
        printing(Arr = Arr)
        print("Found")
        return True
        
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
        print("Depth is: ", temp[1] , "And h = ", temp[2])
        
def printed(Arr):
    for i in range(3):
            for j in range(3):
                if Arr[i][j] == -1:
                    print(" ",end= '\t')
                else:
                    print(Arr[i][j],end='\t')
            print('\n')
        #print("Depth is: ", temp[1] , "And h = ", temp[2])
                
    
def depth():
    global puzzle
    Arr = [[puzzle,0,compare()]]
    ArrStore = []
    #printing(Arr)
    if depthNonEfficient(ArrStore = ArrStore, Arr = Arr):
        return
    else:
        print("Couldn't find")
        return

def  main():
    global puzzle
    print("Enter the Values")
   
   # for i in range(3):
    #    for j in range(3):
     #       d = int(input("Enter: "))
            
      #      puzzle[i][j] = d
            
    printed(puzzle)      
    depth()
main()
    
    
    
    
    
    


    
    

