# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Date :  28.1.2019

import random as r
ai,player='O','X'
board=[['_','_','_'],['_','_','_'],['_','_','_']]
weights=[[3,2,3],[2,4,2],[3,2,3]]
def init():
    global ai,player,board,weights
    ai,player='O','X'
    board=[['_','_','_'],['_','_','_'],['_','_','_']]
    weights=[[3,2,3],[2,4,2],[3,2,3]]    
    
def move(row,col,ch):
    if row>2 or row<0 or col>2 or col<0 :   #Array Out Of Bounds Check
        return False
    
    if board[row][col]=='_':
         board[row][col],weights[row][col]=ch,0
         return True 
    else : return False

def display(move_type='board'):
    if move_type=='cpu' : print('*'*5+'CPU MOVE'+'*'*5)
    elif move_type=='board': print("*"*5+'  Board of Tic Tac Toe '+'*'*5)    
    else :print('*'*5+'PLAYER MOVE'+'*'*5)
    for i in range(3):
        for j in range(3):
             print(board[i][j],end='\t')
        print('\n')
    print('\n')    
    
def compare_line(s1,ch):
    return '_' in s1 and s1.count(ch)==2 

def compare_diag(s1,ch):
    if ch == ai:
        return s1[1]=='_' and s1.count(ch)==0  and s1.count(player)==1
    else:
        return s1[1]=='_' and s1.count(ch)==0  and s1.count(ai)==1
    
    
     
def get_position():
    max_value=max([max(x) for x in weights])
    positions=[(i,weights[i].index(max_value)) for i in range(3)  if max_value in weights[i]]
    return positions

def has_tied():
    count = 0
    #for row in board:
     #  if '_' in row: count = count + 1 
      # if count == 2:
       #    return False
    for i in range(3):
        for j in range (3):
            if board[i][j] == '_':
                count = count + 1
            if count == 2:
                return False
    return True



def attacking_positiion(ch):
    #sends index (row,col)
        default='_'
        for i in range(3):
            col=[board[0][i],board[1][i],board[2][i]]
            if compare_line(board[i],ch): return ((i,board[i].index(default)),True)
            elif compare_line(col,ch): return ((col.index(default),i),True)  
        #diag1,diag2=[board[0][0],board[1][1],board[2][2]],[board[0][2],board[1][1],board[2][0]]
        #diagnals
        diag1 = [board[0][0],board[1][1],board[2][2]]
        diag2 = [board[0][2],board[1][1],board[2][0]]
        diag3 = [board[0][0],'t',board[2][2]]
        diag4 = [board[0][2],'t',board[2][0]]
        if compare_line(diag1,ch):return ((diag1.index(default),diag1.index(default)),True)
        elif compare_line(diag2,ch): return ((diag2.index(default),2-diag2.index(default)),True)
        #check for trick ones
        elif compare_diag(diag1,ch): return ((diag3.index(default),diag3.index(default)),False)
        elif compare_diag(diag2,ch): return ((diag4.index(default),2-diag4.index(default)),False)
        return (False,False)      

def ai_move():
    global ai,player
    pos,f=attacking_positiion(ch=ai),False
    if pos[0]!=False:
        (row,col),f=pos[0],pos[1]
    else :
        pos=attacking_positiion(ch=player)
        if pos[0]!=False: row,col=pos[0]
        else: row,col=r.choice(get_position())
    move(row,col,ai)
    return f            

def run():
    global ai,player
    move_type=None  
    #tried = False  
    #end = False     
    print('*'*10+ 'Tic Tac Toe'+'*'*10+'\n')
    
    display()
    ch=input('Choose a Character X or O : ')
    #if ch=='O': ai,player=player,ai
    if ch=='O' or ch=='0' or ch=='o':
        ai = 'X'
        player = 'O'
    else:
        ai = 'O'
        player = 'X'
    while(True):
       # if tied:
        #    print('*'*10+'The match is tied, Good Game'+'*'*10)
         #   return 
        #elif end:
        #if end:
         #   print('*'*10+move_type+' has own '+'*'*10) 
          #  return       
        move_type='player'
        r=int(input("\nEnter next move's row (1 to 3): "))
        c=int(input("Enter next move's column (1 to 3): "))
        #r=int(input("\nEnter the (x,y): ("))
        #=int(input(","))
        #print(")");
        
        if not move(r-1,c-1,player):
            print('\nEnter proper positions!!')
        else:   
          display(move_type=move_type)
          #tied=has_tied()          
          #if tied: continue
          if has_tied(): 
              print('*'*10+'The match is tied, Good Game'+'*'*10)
              return
          
          move_type='cpu'     
          #end=ai_move()   
          #display(move_type=move_type)
          if ai_move():
            display(move_type=move_type)
            print('*'*10+move_type+' has own '+'*'*10) 
            return 
          display(move_type=move_type)
          #tied=has_tied()
          if has_tied(): 
              print('*'*10+'The match is tied, Good Game'+'*'*10)
              return
def main():    
    #Can Always get a tie or a win
    run()
    f='Y'
    while(f=='Y'or f=='y'):
        f=input('Do you want to play again Y or N: ')
        init()
        if f=='Y' or f=='y':run()
    print('\n\n'+'*'*10+' Thank You '+'*'*10)    
main()    
