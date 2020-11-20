# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:15:42 2020

@author: Naman
"""

combinations = [(True, True, True), (True, True, False), (True, False, True), (True, False, False),
                (False, True, True), (False, True, False), (False, False, True), (False, False, False)]
variable = {'p': 0, 'q': 1, 'r': 2}
kb = ''
q = ''
priority = {'~': 3, 'v': 1, '^': 2}


def input_rules():
    global kb, q
    kb = (input("Enter rule: "))
    q = input("Enter the Query: ")


def entailment():
    global kb, q
    print(''*10+"Truth Table Reference"+''*10)
    print('  kb', '\t alpha')
    
    for comb in combinations:
        s = evaluatePostfix(toPostfix(kb), comb)
        f = evaluatePostfix(toPostfix(q), comb)
        print('-'*16)
        print("",s,"\t ", f)
        
        if s and not f:
            return False
    return True

def hasLessOrEqualPriority(c1, c2):
    try:
        return priority[c1] <= priority[c2]
    except KeyError:
        return False


def toPostfix(infix):
    stack = []
    postfix = ''
    for c in infix:
        if c.isalpha() and c != 'v':
            postfix += c
        else:
            if c == '(':
                stack.append(c)
            elif c == ')':
                operator = stack.pop()
                while not operator == '(':
                    postfix += operator
                    operator = stack.pop()
            else:
                while (len(stack) != 0) and hasLessOrEqualPriority(c, stack[-1]):
                    postfix += stack.pop()
                stack.append(c)
    while (len(stack) != 0):
        postfix += stack.pop()

    return postfix


def evaluatePostfix(exp, comb):
    stack = []
    for i in exp:
        if i.isalpha() and i != 'v':
            stack.append(comb[variable[i]])
        elif i == '~':
            val1 = stack.pop()
            stack.append(not val1)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(_eval(i, val2, val1))
    return stack.pop()


def _eval(i, val1, val2):
    if i == '^':
        return val2 and val1
    return val2 or val1

def main():
    input_rules()
    ans = entailment()
    if ans:
        print("The Knowledge Base entails query")
    else:
        print("The Knowledge Base does not entail query")
main()