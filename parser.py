'''
CpSc 827: Translation of Programming Languages
Milestone 2: Parser

- Viswanath Chennuru & Navin Soni
'''

import re

import sys

import variables

import semantics

from operator import itemgetter                         # used while sorting the productions



redStack = []                                           # stack to perform reduction

bStack = []                                             # Backup stack, used for error recovery

vStack = 0


pffile = open("wpfile")

line = 1                                                # Used for line count in reading the wpfile

i=0

for ln in pffile.readlines():
    if (line == 1):
        firstLine = re.findall('[0-9]+',ln)             # first line has # of productions, # of symbols, and # of terminal symbols
        nProduction = int(firstLine[0])                 # # of productions
        nSymbol = int(firstLine[1])                     # # of symbols

    if (line >= 2 and line <= 84):                      # reading the symbols into a list
        variables.symbols.append(ln.split(' ')[len(ln.split(' ')) - 1][:-1])
        i = i + 1
        
    if(line>= 85 and line <= 180):                      # reading the productions into as list
        variables.productions.append([])
        variables.productions[line-85].append(line-84)
        
        variables.usProductions.append([])
        variables.usProductions[line-85].append(line-84)
        
        k = 0
        
        while(k < len(ln.split(' '))):
            if(ln.split(' ')[k] != ''):
                variables.productions[line - 85].append(int(ln.split(' ')[k]))
                variables.usProductions[line - 85].append(int(ln.split(' ')[k]))
            k = k + 1
            
    if (line >= 181):                                   # reading the matrix
        variables.matrix.append([])
        j = 0
        while(j < len(ln)-1):
            variables.matrix[line - 181].append(int(ln[j]))
            j = j + 1
    line = line + 1
variables.matrix[line - 182].append(int(ln[82]))

variables.productions.sort(key = itemgetter(1),reverse = True)            

def reduction(rQueue):
    global vStack
    flag = 0                                            # Used to indicate error
    flag1 = 0
    
    if(len(redStack) == 0):
        redStack.append(rQueue[0])                      # Initializing the reduction stack
        
        semantics.semRed(1,variables.var[0]);
        variables.var.pop(0)
        
        rQueue.pop(0)

    if (len(rQueue) == 0):
        red()
        
    while(len(rQueue) > 0 and flag == 0):
     
        
        ch = variables.matrix[redStack[-1:][0]-1][rQueue[0]-1]    # Finding the entry in symbol matrix
        if(variables.flag[9] == True):                  # Printing the top of the stack, input symbol and relation between them if flag is set
            print '\nTop of the stack:',variables.symbols[redStack[-1:][0]-1],',','Input symbol:',variables.symbols[rQueue[0]-1],',','Relation:',
            if(ch == 1):
                print 'Equal to.'
            elif(ch == 2):
                print'Greater than.'
            elif(ch == 3):
                print 'Less than.'
            elif(ch == 0):
                print 'No relation.'
        
        if(ch == 1 or ch == 3):                         # Stacking the first queue symbol if the relations is "equal to" or "less than"
            redStack.append(rQueue[0])
            
            semantics.semRed(1,variables.var[0]);       # Call to semantic reduction

            variables.var.pop(0)                        # Removing the input variable after inserting it into the semantic stack
            
            rQueue.pop(0)
            
        if(ch == 2):                                    # Performing reduction if reduction is "greater than"
            red()
            
            if(flag1 == 0):
                flag1 = 1
                vStack = len(redStack)
                
        if(ch == 0):                                    
            print '\nError, no relation between top element of the stack and first element in the queue'
            flag = 1                                    # Setting flag to indicate error if entry in symbol matrix not found
    
    if(flag != 1):
        bStack[:] = redStack[:]                         # Backing up reduction stack if symbol queue is parsed successfully
        
    elif(flag == 1):
        print '\nElements removed from the stack:'
        prnt(redStack[vStack:],3)
        print '\nElenents ignored from the input:'
        prnt(rQueue,3)
        redStack[:] = bStack[:]                         # Undoing reductions if error occurs (Panic Recovery)    

def red():
    
    flag = 1    
    for each in variables.productions:
        if(len(redStack) >= (len(each)-3) and redStack[-(len(each)-3):] == each[2:-1]):
            if(variables.flag[10] == True):
                print '\n The matched handel is:',
                prnt(redStack[-(len(each)-3):],3)
                
            if(variables.flag[8] == True):      # Printing stack symbols before reduction if flag is set
                print '\nThe stack before reduction is:'
                prnt(redStack,2)
                
            if (variables.flag[7] == True):       # Printing the reduction if the flag is set
                prnt(each,1)
                
            redStack[-(len(each)-3):] = each[-1:] # Performing reduction on stack
            semantics.semRed(2, each[0] - 1)
            flag = 0                            # Reduction found, reset flag
            
            if(variables.flag[8] == True):      # Printing stack symbols after reduction if flag is set
                print '\n The stack after reduction is:'
                prnt(redStack,2)
                
            break
            
    if(flag ==1):
        print '\nError, reduction not found'
        sys.exit()


def prnt(lst, var):
    if(var == 1):                                       # Printing the reduction
        print '\n',lst[0],',',variables.symbols[int(lst[-1:][0])-1],'<---',
        for j in lst[2:-1]:
            print variables.symbols[j-1],
    
    if(var == 2):                                       # Printing the reduction stack
        for j in lst:
            print '\n',variables.symbols[j-1],
            
    if(var == 3):
        for j in lst:
            print variables.symbols[j-1],

