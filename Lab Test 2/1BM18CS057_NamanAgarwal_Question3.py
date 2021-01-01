# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:44:33 2021

@author: Naman
"""

#kb ->  (~QvR)^(~Pv~Q)^(RvQ)
#Query -> R

def evaluate(i,val1,val2):
    if i== '^':
        return val2 and val1
    return val2 or val1

def isOperand(c):
    return c.isalpha() and c!='v'

def hasLessOrEqualPriority(c1,c2):
    priority = {'~':3,'^':1,'v':2}
    try:
        return priority[c1] <= priority[c2]
    except KeyError:
        return False

def toPostfix(infix):
    stack = []
    postfix = ''
    for c in infix:
        if isOperand(c):
            postfix += c
        else:
            if c == '(':
                stack.append(c)
            elif c == ')':
                operator = stack.pop()
                while operator != '(':
                    postfix += operator
                    operator = stack.pop()
            else:
                while (len(stack)!=0) and hasLessOrEqualPriority(c,stack[-1]):
                    postfix += stack.pop()
                stack.append(c)
    while (len(stack)!=0):
        postfix += stack.pop()
    return postfix

def evaluatePostfix(exp,comb):
    stack = []
    variable = {'P':0,'Q':1,'R':2}
    for i in exp:
        if isOperand(i):
            stack.append(comb[variable[i]])
        elif i == '~':
            val1 = stack.pop()
            stack.append(not val1)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(evaluate(i,val1,val2))

    return stack.pop()

def Check(postfix_kb,postfix_q):
    combinations = [[True,True,True],[True,True,False],
                    [True,False,True],[True,False,False],
                    [False,True,True],[False,True,False],
                    [False,False,True],[False,False,False]]
    print("\n------------------------|---------------|-------------")
    for combination in combinations:
        eval_kb = evaluatePostfix(postfix_kb,combination)
        eval_q = evaluatePostfix(postfix_q,combination)
        
        if(combination == [True,True,True]):
            print(combination,"\t\t| kb = ",eval_kb,"\t| q = ",eval_q)
        else:
            print(combination,"\t| kb = ",eval_kb,"\t| q = ",eval_q)

        if eval_kb == True and eval_q == False:
            return False
    return True

def main():
    kb=(input("Enter the knowledge base:  "))
    query=(input("Enter the query:  "))
    postfix_kb = toPostfix(kb)
    postfix_q = toPostfix(query)
    
    if(Check(postfix_kb,postfix_q)):
        print("------------------------|---------------|-------------")
        print("\nEntails")
    else:
        print("------------------------|---------------|-------------")
        print("\nDoesnt Entail")
main()
