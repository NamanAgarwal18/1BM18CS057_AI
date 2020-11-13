# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:19:00 2020

@author: Naman Agarwal
"""
#Date: 13/11/2020
#Lab Test 1
#AI
#1BM18CS057

def  fill(Cup4,Cup3,Arr,depth):
    depth=depth + 1
    if depth == 10:                             #Max Depth
        #print()                                #If we went too deep
        return False
    if Cup4 == 2:   
        #print()
        #print(Cup4, " -> ", Cup3)              #if we hit the goal state
        return True
    
    if Cup4 !=4 and Cup3 != 0 : 
        #print("From Cup3 to Cup4")             #Transfer from 3L cup to 4L as much as possible
        temp1 = Cup4
        temp2 = Cup3
        Cup4 = Cup4 + Cup3
        if Cup4 > 4:
            Cup3 = Cup4 - 4
            Cup4 = 4
        else:
            Cup3 = 0
        if fill(Cup4,Cup3,Arr,depth):
            #Arr.append("From Cup3 to Cup4")
            stri = ""
            stri = (stri + "Cup 3L: \t" + "%d") %Cup3 
            stri = (stri + "\t Cup 4L: \t" + "%d" + "\t From Cup 3L to Cup 4L") %Cup4
            Arr.append(stri)
            return True
        Cup4 = temp1
        Cup3 = temp2
        
    if Cup3 !=3 and Cup4!=0:            
        #print("From Cup4 to Cup3")              #Transfer from 4L cup to 3L as much as possible
        temp1 = Cup4
        temp2 = Cup3
        Cup3 = Cup4 + Cup3
        if Cup3 > 3:
            Cup4 = Cup3 - 3
            Cup3 = 3
        else:
            Cup4 = 0
        if fill(Cup4,Cup3,Arr,depth):
            #print("--------Ahead--------")
            #Arr.append("From Cup4 to Cup3")
            stri = ""
            stri = (stri + "Cup 3L: \t" + "%d") %Cup3 
            stri = (stri + "\t Cup 4L: \t" + "%d" + "\t From Cup 4L to Cup 3L") %Cup4
            Arr.append(stri)
            return True
        Cup4 = temp1
        Cup3 = temp2
    
    if Cup4 !=4:  
        #print("Pumped Cup4")                    #Using Pump to fill cup with 4L to full
        temp1 = Cup4
        temp2 = Cup3
        Cup4 = 4 
        if fill(Cup4,Cup3,Arr,depth):
            #print("--------Ahead--------")
            #Arr.append("Pumped Cup4")
            stri = ""
            stri = (stri + "Cup 3L: \t" + "%d") %Cup3 
            stri = (stri + "\t Cup 4L: \t" + "%d" + "\t Pumped Cup 4L") %Cup4
            Arr.append(stri)
            return True
        Cup4 = temp1
        Cup3 = temp2
        
    if Cup3 !=3: 
        #print("Pumped Cup3")                   #Using Pump to fill cup with 3L to full
        temp1 = Cup4
        temp2 = Cup3
        Cup3 = 3 
        if fill(Cup4,Cup3,Arr,depth):
            #print("--------Ahead--------")
            #Arr.append("Pumped Cup3")
            stri = ""
            stri = (stri + "Cup 3L: \t" + "%d") %Cup3 
            stri = (stri + "\t Cup 4L: \t" + "%d" + "\t Pumped Cup 3L") %Cup4
            Arr.append(stri)
            return True
        Cup4 = temp1
        Cup3 = temp2
    
    if Cup4 !=0:  
        #print("Thowing Cup4")                    #Throwing Out Cup4
        temp1 = Cup4
        temp2 = Cup3
        Cup4 = 0 
        if fill(Cup4,Cup3,Arr,depth):
            #print("--------Ahead--------")
            #Arr.append("Throwing Cup4")
            stri = ""
            stri = (stri + "Cup 3L: \t" + "%d") %Cup3 
            stri = (stri + "\t Cup L4: \t" + "%d" + "\t Thowing Cup 4L") %Cup4
            Arr.append(stri)
            return True
        Cup4 = temp1
        Cup3 = temp2
        
    if Cup3 !=0:  
        #print("Thowing Cup3")                      #Throwing Out Cup3
        temp1 = Cup4
        temp2 = Cup3
        Cup3 = 0 
        if fill(Cup4,Cup3,Arr,depth):
            #print("--------Ahead--------")
            #Arr.append("Throwing Cup3")
            stri = ""
            stri = (stri + "Cup 3L: \t" + "%d") %Cup3 
            stri = (stri + "\t Cup 4L: \t" + "%d" + "\t Thowing Cup 3Lclear") %Cup4
            Arr.append(stri)
            return True
        Cup4 = temp1
        Cup3 = temp2

    #print("----------------------------")   
    return False


def main():
    Arr = []
    Cup4 = 0
    Cup3 = 0
    depth = 0
    finding = fill(Cup4, Cup3, Arr, depth)
    if finding:
        print()
        print()
        print()
        for i in reversed(Arr):
            print(i)
    else:
        print("Not Found")
main()
        
                              
        
    
    