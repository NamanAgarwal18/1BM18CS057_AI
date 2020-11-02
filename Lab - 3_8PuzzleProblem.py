# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:07:08 2020

@author: Naman
"""

#puzzle[[]] -> [[1,2,3],[4,5,6], [7,8,-1]]
#final[] -> [puzzle,h,action]
#Arr[] ->[puzzle,depth,h,action]
#Aexarr -> [puzzle,depth,h,action]

import random as r
puzzle = [[1,2,3],[-1,4,6],[7,5,8]]
result = [[1,2,3],[4,5,6],[7,8,-1]]



def find(temp):
    global result
    for i in range(3):
        for j in range(3):
            if temp == result[i][j]:
                return (i,j)

def compare(puz):
    global result
    count = 0
    for i in range(3):
        for j in range(3):
            if puz[i][j]!=-1:
                (iresult,jresult) = find(temp = puz[i][j])
                iresult = iresult - i;
                jresult  = jresult - j;
                if iresult <0:
                    iresult = iresult * -1
                if jresult <0:
                    jresult = jresult * -1
                count = count + iresult + jresult
    return count



def duplicate(arr):
    newarr = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            newarr[i][j] = arr[i][j]
    return newarr

def findBlank(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == -1:
                return (i,j)
            
def Assending(final):
    newfinal = []
    c=-1;
    length = len(final)
    for i in range(length):
        c = 0
        for j in range(1,len(final),1):
            if final[c][1] > final[j][1]:
                c = j
            elif final[c][1] == final[j][1] and r.choice([True,False]):
                c = j
            else:
                continue
        newfinal.append(final[c])
        final.pop(c)
        
        
    return newfinal
       
                            
        

def checkAll(Arr,Auxarr,depth,past):
    global puzzle,result
    #printed(puzzle)
    arrPuzzle = [[]]
    array = [None,555,False]
    final = []
    (i,j) = findBlank(arr = puzzle)
    
    if i!=0 and past!='D' :                                                     #Move Up 
        arrPuzzle = duplicate(puzzle)
        arrPuzzle[i][j] = arrPuzzle[i-1][j]
        arrPuzzle[i-1][j] = -1
        hold  = compare(arrPuzzle)
        action  = 'U'
        array[0] = arrPuzzle
        array[1] = hold
        array[2] = action
        final.append(array)
    if j!=0 and past!='R':                                                      #Move Left
        arrPuzzle = duplicate(puzzle)
        arrPuzzle[i][j] = arrPuzzle[i][j-1]
        arrPuzzle[i][j-1] = -1
        hold  = compare(arrPuzzle)
        action  = 'L'
        array[0] = arrPuzzle
        array[1] = hold
        array[2] = action
        final.append(array)
    if i!=2 and past!='U':                                                      #Move Down
        arrPuzzle = duplicate(puzzle)
        arrPuzzle[i][j] = arrPuzzle[i+1][j]
        arrPuzzle[i+1][j] = -1
        hold  = compare(arrPuzzle)
        action  = 'D'
        array[0] = arrPuzzle
        array[1] = hold
        array[2] = action
        final.append(array)
    if j!=2 and past!='L':                                                      #Move Right
        arrPuzzle = duplicate(puzzle)
        arrPuzzle[i][j] = arrPuzzle[i][j+1]
        arrPuzzle[i][j+1] = -1
        hold  = compare(arrPuzzle)
        action  = 'R'
        array[0] = arrPuzzle
        array[1] = hold
        array[2] = action
        final.append(array)
    depth = depth+1   
    final = Assending(final = final)
    
    Arr.append([final[0][0],depth,final[0][1],final[0][2]])
    #print("Putting in Arr")
    #puzzle = duplicate(final[0][0])
    direction = final[0][2]
    #print(direction)
    (i,j) = findBlank(arr = puzzle)
    if direction == 'U':
        puzzle[i][j] = puzzle[i-1][j]
        puzzle[i-1][j] = -1
    if direction == 'L':
        puzzle[i][j] = puzzle[i][j-1]
        puzzle[i][j-1] = -1
    if direction == 'D':
        puzzle[i][j] = puzzle[i+1][j]
        puzzle[i+1][j] = -1
    if direction == 'R':
        puzzle[i][j] = puzzle[i][j+1]
        puzzle[i][j+1] = -1
    #printed(puzzle)
    
    
    
    final.pop(0)
    for i in range(len(final)):
        Auxarr.append([final[len(final) - i-1][0], depth, final[len(final) - i-1][1], final[len(final) - i-1][2]])
    #puzzle = Arr[len(Arr)-1][0]
    return (Arr,Auxarr)

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
        print("Depth is: ", temp[1] , "And h = ", temp[2], "Moved: ", temp[3],"\n\n")

def efficient(Arr,Auxarr):
    global puzzle,result
    #puzzle = Arr[len(Arr)-1][0]
    depth = Arr[len(Arr)-1][1]
    h = Arr[len(Arr)-1][2]
    action = Arr[len(Arr)-1][3]
    print("Putting in Arr")
    #printed(Arr[len(Arr) -1][0])
    #puzzle = [[0,0,0],[0,0,0],[0,0,0]]
    #temp = Arr[len(Arr)-1]
    #puz = temp[0]
    
    #print(*Arr[len(Arr)-1][0])
    
    #for i in range(3):
     #  for j in range(3):
      #     puzzle[i][j] = puz[i][j]
    #printed(puzzle)
    #return True
    if  h == 0:
        return True
    if depth >= 4:
        return False
    (Arr,Auxarr) = checkAll(Arr = Arr, Auxarr = Auxarr, depth = depth, past = action)
    return efficient(Arr = Arr, Auxarr = Auxarr)
    
def inefficient(Arr,Auxarr):
    global puzzle,result
    
    flag = efficient(Arr = Arr, Auxarr = Auxarr)
    print(flag)
    if flag==True:
        printing(Arr=Arr)
        print("found")
        print(len(Arr))
        #printing(Auxarr)
        return True
    elif flag==False:
        if len(Auxarr)==0:
            return False
        else:
            
            depth = Auxarr[len(Auxarr) - 1][1]
            
            while Arr[len(Arr)-1][1] > depth:
                Arr.pop(len(Arr)-1)
            Arr.pop(len(Arr)-1)
            #while Arr[len(Arr)-1][1]!=depth:
             #   Arr.pop(len(Arr)-1)
            #Arr.pop(len(Arr)-1)
            
            Arr.append(Auxarr[len(Auxarr)-1])
            Auxarr.pop(len(Auxarr)-1)
            
            return inefficient(Arr = Arr, Auxarr = Auxarr)
            
    
def depth ():
    global puzzle,result
    #printed(puzzle)
    Arr = []
    puz  = duplicate(puzzle)
    Arr.append([puz,0,compare(puz),'_'])
    #Arr = [[puzzle,0,compare(puz),'_']]
    Auxarr = []
    #printing(Arr)
    if inefficient(Arr = Arr, Auxarr = Auxarr)==False:
        print("Couldn't find")
        return
    
        
    
def printed(Arr):
    for i in range(3):
            for j in range(3):
                if Arr[i][j] == -1:
                    print(" ",end= '\t')
                else:
                    print(Arr[i][j],end='\t')
            print('\n')
            
def main():
    #puzzle = [[0,0,0],[0,0,0],[0,0,0]]
    #result = [[0,0,0],[0,0,0],[0,0,0]]
    #print("Enter the puzzle")
    #for i in range(3):
     #   for j in range(3):
      #      d = int(input("Enter: "))
       #     puzzle[i][j] = d
    #print("Enter the result")
    #for i in range(3):
     #   for j in range(3):
      #      d = int(input("Enter: "))
       #     result[i][j] = d
            
    #puzzle = [[1,2,3],[-1,4,7],[7,5,8]]
    #result = [[1,2,3],[4,5,6],[7,8,-1]]
    #printed(puzzle)
    depth()
main()
            