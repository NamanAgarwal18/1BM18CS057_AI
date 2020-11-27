# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:32:53 2020

@author: Naman
"""

kb = []

    
def TELL(sentence):
    global kb
    if isClause(sentence):                       # If the sentence is a clause, insert directly.
        kb.append(sentence)
    else:                                        # If not, convert to CNF, and then insert clauses one by one.
        sentenceCNF = convertCNF(sentence)
        if not sentenceCNF:
            print("Illegal input")
            return
        if isAndList(sentenceCNF):               # Insert clauses one by one when there are multiple clauses
            for s in sentenceCNF[1:]:
                kb.append(s)
        else:
            kb.append(sentenceCNF)
            
def ASK(sentence):
    global kb
    if isClause(sentence):                      # Negate the sentence, and convert it to CNF accordingly.
        neg = negation(sentence)
    else:
        sentenceCNF = convertCNF(sentence)
        if not sentenceCNF:
            print("Illegal input")
            return
        neg = convertCNF(negation(sentenceCNF))

    ask_list = []                                   # Insert individual clauses that we need to ask to ask_list.
    if isAndList(neg):
        for n in neg[1:]:
            nCNF = makeCNF(n)
            if type(nCNF).__name__ == 'list':
                ask_list.insert(0, nCNF)
            else:
                ask_list.insert(0, nCNF)
    else:
        ask_list = [neg]                            # Create a new list combining the asked sentence and kb.
    clauses = ask_list + kb[:]                      # Resolution will happen between the items in the list.

    while True:                                     # Recursivly conduct resoltion between items in the clauses list until it produces an empty list or there's no more pregress.
        new_clauses = []
        for c1 in clauses:
            for c2 in clauses:
                if c1 is not c2:
                    resolved = resolve(c1, c2)
                    if resolved == False:
                        continue
                    if resolved == []:
                        return True
                    new_clauses.append(resolved)

        if len(new_clauses) == 0:
            return False

        new_in_clauses = True
        for n in new_clauses:
            if n not in clauses:
                new_in_clauses = False
                clauses.append(n)

        if new_in_clauses:
            return False
    return False


def resolve(arg_one, arg_two):                          # Conduct resolution on two CNF clauses.
    resolved = False

    s1 = make_sentence(arg_one)
    s2 = make_sentence(arg_two)

    resolve_s1 = None
    resolve_s2 = None

    for i in s1:                                        # Two for loops that iterate through the two clauses.
        if isNotList(i):
            a1 = i[1]
            a1_not = True
        else:
            a1 = i
            a1_not = False

        for j in s2:
            if isNotList(j):
                a2 = j[1]
                a2_not = True
            else:
                a2 = j
                a2_not = False

            if a1 == a2:                                # cancel out two literals such as 'a' $ ['not', 'a']
                if a1_not != a2_not:
                    
                    if resolved:                        # Return False if resolution already happend but contradiction still exists.
                        return False
                    else:
                        resolved = True
                        resolve_s1 = i
                        resolve_s2 = j
                        break

    if not resolved:                                     # Return False if not resolution happened
        return False

    s1.remove(resolve_s1)                                # Remove the literals that are canceled
    s2.remove(resolve_s2)

    result = clear_duplicate(s1 + s2)                    # Remove duplicates

    if len(result) == 1:                                 # Format the result.
        return result[0]
    elif len(result) > 1:
        result.insert(0, 'or')

    return result

def make_sentence(arg):                                  # Prepare sentences for resolution.
    if isLiteral(arg) or isNotList(arg):
        return [arg]
    if isOrList(arg):
        return clear_duplicate(arg[1:])
    return

def clear_duplicate(arg):
    result = []
    for i in range(0, len(arg)):
        if arg[i] not in arg[i+1:]:
            result.append(arg[i])
    return result

def isClause(sentence):                                  # Check whether a sentence is a legal CNF clause.
    if isLiteral(sentence):
        return True
    if isNotList(sentence):
        if isLiteral(sentence[1]):
            return True
        else:
            return False
    if isOrList(sentence):
        for i in range(1, len(sentence)):
            if len(sentence[i]) > 2:
                return False
            elif not isClause(sentence[i]):
                return False
        return True
    return False


def isCNF(sentence):                                    # Check if a sentence is a legal CNF.
    if isClause(sentence):
        return True
    elif isAndList(sentence):
        for s in sentence[1:]:
            if not isClause(s):
                return False
        return True
    return False

def negation(sentence):                                 # Negate a sentence.
    if isLiteral(sentence):
        return ['not', sentence]
    if isNotList(sentence):
        return sentence[1]

    if isAndList(sentence):                             # DeMorgan:
        result = ['or']
        for i in sentence[1:]:
            if isNotList(sentence):
                result.append(i[1])
            else:
                result.append(['not', sentence])
        return result
    if isOrList(sentence):
        result = ['and']
        for i in sentence[:]:
            if isNotList(sentence):
                result.append(i[1])
            else:
                result.append(['not', i])
        return result
    return None


def convertCNF(sentence):
    while not isCNF(sentence):
        if sentence is None:
            return None
        sentence = makeCNF(sentence)
    return sentence

def makeCNF(sentence):                                  # Help make a sentence into CNF.
    if isLiteral(sentence):
        return sentence

    if (type(sentence).__name__ == 'list'):
        operand = sentence[0]
        if isNotList(sentence):
            if isLiteral(sentence[1]):
                return sentence
            cnf = makeCNF(sentence[1])
            if cnf[0] == 'not':
                return makeCNF(cnf[1])
            if cnf[0] == 'or':
                result = ['and']
                for i in range(1, len(cnf)):
                    result.append(makeCNF(['not', cnf[i]]))
                return result
            if cnf[0] == 'and':
                result = ['or']
                for i in range(1, len(cnf)):
                    result.append(makeCNF(['not', cnf[i]]))
                return result
            return "False: not"
        
        if operand == 'implies' and len(sentence) == 3:              # Implication Elimination:
            return makeCNF(['or', ['not', makeCNF(sentence[1])], makeCNF(sentence[2])])

        if operand == 'biconditional' and len(sentence) == 3:        # Biconditional Elimination:
            s1 = makeCNF(['implies', sentence[1], sentence[2]])
            s2 = makeCNF(['implies', sentence[2], sentence[1]])
            return makeCNF(['and', s1, s2])

        if isAndList(sentence):
            result = ['and']
            for i in range(1, len(sentence)):
                cnf = makeCNF(sentence[i])
                
                if isAndList(cnf):                                   # Distributivity:
                    for i in range(1, len(cnf)):
                        result.append(makeCNF(cnf[i]))
                    continue
                result.append(makeCNF(cnf))
            return result

        if isOrList(sentence):
            result1 = ['or']
            for i in range(1, len(sentence)):
                cnf = makeCNF(sentence[i])
                
                if isOrList(cnf):                                   # Distributivity:
                    for i in range(1, len(cnf)):
                        result1.append(makeCNF(cnf[i]))
                    continue
                result1.append(makeCNF(cnf))

            while True:                                              # Associativity:
                result2 = ['and']
                and_clause = None
                for r in result1:
                    if isAndList(r):
                        and_clause = r
                        break

                if not and_clause:                          # Finish when there's no more 'and' lists inside of 'or' lists
                    return result1

                result1.remove(and_clause)

                for i in range(1, len(and_clause)):
                    temp = ['or', and_clause[i]]
                    for o in result1[1:]:
                        temp.append(makeCNF(o))
                    result2.append(makeCNF(temp))
                result1 = makeCNF(result2)
            return None
    return None


def isLiteral(item):                                        # Below are 4 functions that check the type of a variable
    if type(item).__name__ == 'str':
        return True
    return False


def isNotList(item):
    if type(item).__name__ == 'list':
        if len(item) == 2:
            if item[0] == 'not':
                return True
    return False


def isAndList(item):
    if type(item).__name__ == 'list':
        if len(item) > 2:
            if item[0] == 'and':
                return True
    return False


def isOrList(item):
    if type(item).__name__ == 'list':
        if len(item) > 2:
            if item[0] == 'or':
                return True
    return False


def main():
    global kb
    kb = []
    
   
    TELL(['implies', 'p', 'q'])
    TELL(['implies', 'r', 's'])
    print("For first test case: ", ASK(['implies',['or','p','r'], ['or', 'q', 's']]))
    
    kb = []
    TELL('a')
    TELL('b')
    TELL('c')
    TELL('d')
    print("For second test case: ", ASK(['or', 'a', 'b', 'c', 'd']))
    
    kb = []
    TELL('a')
    TELL('b')
    TELL(['or', ['not', 'a'], 'b'])
    TELL(['or', 'c', 'd'])
    TELL('d')
    print("For third test case: " , ASK('c'))
    
main()
    