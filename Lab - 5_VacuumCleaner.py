# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:18:48 2020

@author: Naman
"""

import random as r

def randGenerator(n,m):
    arr = []
    for i in range(n):
        array = []
        for j in range(m):
            array.append(r.choice([0,1]))
        arr.append(array)
    return arr

def printing(arr,n,m,a,b):
    for i in range(n):
        for j in range(m):
            if a==i and b==j and b==0:
                if j==0:
                    print("", end="")
                print("<",end="")
                print(arr[i][j], end=">  ")
           
            elif a == i and b == j+1:
                if j==0:
                    print(" ", end="")
                print(arr[i][j], end="  <")
            elif a == i and b == j:
                if j==0:
                    print(" ", end="")
                print(arr[i][j], end=">  ")
            else:
                if j==0:
                    print(" ", end="")
                print(arr[i][j], end="   ")
        print()
       
def cleaner(arr,n,m):
    pos = 0;
    for i in range(n):
        if pos==0:
            for j in range(m):
                pos = j
                printing(arr = arr, n = n, m = m, a = i, b = j)
                if arr[i][j] == 1:
                    print("Percepting Dirt....CLeaning....moving ahead")
                    arr[i][j]=0
                else:
                    print("Already clean....moving ahead")
        else:
            for j in range(m):
                pos = m-j-1;
                printing(arr = arr, n = n, m = m, a = i, b = m -j -1)
                if arr[i][m-j-1] == 1:
                    print("Percepting Dirt....CLeaning....moving ahead")
                    arr[i][m -j -1]=0
                else:
                    print("Already clean....moving ahead")
    
    
def main():
    print("Enter the values of: ")
    n=int(input("N = "))
    m=int(input("M = "))
    arr = randGenerator(n = n, m = m)
    #printing(arr = arr, n = n, m = m,a=1,b=0)
    cleaner(arr=arr, n = n, m=m)
    print()
    printing(arr = arr, n = n, m = m, a = n+1, b = m+1)
    print("Everything Cleaned")
main()
    