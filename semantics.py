'''
CpSc 827: Translation of Programming Languages
Milestone 3: Semantics

- Viswanath Chennuru & Navin Soni
'''

'''Made small change in the test data, confirm it before submitting'''

import variables
import pragmatics

semStack = []

i = 0
r = 0
b = 0
l = 0

loop = []
#loop1 = -1

'''Symbol table entry for variables [type, shape, # of rows, # of cols],
Symbol table entry for variables in procedures [type, shape, # of rows, # of cols, call_type]
'''

def semRed(action, element):
    #print 'element:', element
    global i, r, b, l, loop, loop1
    if(variables.flag[12] == True):
        print '\nThe semantic stack before reduction:', semStack,element
    
    if (action == 1):
        semStack.insert(len(semStack),element)
    
    elif(action == 2):
            
        if(element == 0):

            tuples([semStack[-3],'ENDPROGRAM','-','-'])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
            if(variables.flag[16] == True):
    
                print "\nGlobal symbol table: "
    
                for each in range(0,len(variables.globalSymbolTable),2):
                    print '\n',variables.globalSymbolTable[each],variables.globalSymbolTable[each+1]
        
        elif(element == 1):
            
            tuples([semStack[-1], 'PROGNAME', '-', '-'])
            semStack[-(len(variables.usProductions[element]) - 3):] = semStack[-1:]
        
        elif(element == 2):
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 3):
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 4):
            
            tuples(['-','ENDDECLARATIONS','-','-'])

            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 5):
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]        
        
        elif(element == 6):
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]        
        
        elif(element == 7):
            
            if(chkVar(semStack[-1])):
                print '\nError: Variable already exists the symbol table'+str(element)
            
            else:
                if(variables.scopeFlag == 0):
                    variables.globalSymbolTable.append(semStack[-1])
                    variables.globalSymbolTable.append([semStack[-2],'SCALAR', 1, '-'])     # Symbol table entry [type, shape, # of rows, # of cols]
            
                elif(variables.scopeFlag == 1):
                    variables.localSymbolTable.append(semStack[-1])
                    variables.localSymbolTable.append([semStack[-2],'SCALAR', 1, '-'])
                
                tuples([semStack[-1],'MEMORY',1,0])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 8):
            
            if(chkVar(semStack[-2])):
                print '\nError: Variable already exists the symbol table'+str(element)
            
            else:
                if(variables.scopeFlag == 0):

                    variables.globalSymbolTable.append(semStack[-2])
                    variables.globalSymbolTable.append([semStack[-3], 'VECTOR', semStack[-1], '-'])     # Symbol table entry [type, shape, # of rows, # of cols]
            
                elif(variables.scopeFlag == 1):
                    variables.localSymbolTable.append(semStack[-2])
                    variables.localSymbolTable.append([semStack[-3], 'VECTOR', semStack[-1], '-'])
                
                tuples([semStack[-2],'MEMORY',semStack[-1],0])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 9):
            
            if(chkVar(semStack[-4])):
                print '\nError: Variable already exists the symbol table'+str(element)
                
            else:
                if(variables.scopeFlag == 0):
                    #print "\nAdding to global st", semStack[-4]
                    variables.globalSymbolTable.append(semStack[-4])
                    variables.globalSymbolTable.append([semStack[-5], 'MATRIX', semStack[-3], semStack[-1]])     # Symbol table entry [type, shape, # of rows, # of cols]
            
                elif(variables.scopeFlag == 1):
                    variables.localSymbolTable.append(semStack[-4])
                    variables.localSymbolTable.append([semStack[-5], 'MATRIX', semStack[-3], semStack[-1]])
                
                tuples([semStack[-4],'MEMORY',semStack[-3],semStack[-1]])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 10):

            semStack[-(len(variables.usProductions[element]) - 3):] = ['INTEGER']
            
        elif(element == 11):
            
            semStack[-(len(variables.usProductions[element]) - 3):] = ['REAL']
        
        elif(element == 12):
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]        
        
        elif(element == 13):
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]        
        
        elif(element == 14):
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]        
        
        elif(element == 15):
            
            tuples([semStack[-4],'ENDPROCEDURE','-','-'])
            
            if(variables.flag[14] == True):
                print '\nEntries in local symbol table:'
                for each in range(0,len(variables.localSymbolTable),2):
                    print '\n',variables.localSymbolTable[each],variables.localSymbolTable[each + 1]
            
            variables.scopeFlag = 0
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 16):
            
            tuples([semStack[-3],'ENDPROCEDURE','-','-'])
            
            if(variables.flag[14] == True):
                print '\nEntries in local symbol table:'
                for each in range(0,len(variables.localSymbolTable),2):
                    print '\n',variables.localSymbolTable[each],variables.localSymbolTable[each + 1]
            
            variables.scopeFlag = 0
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 17):
            
            tuples(['-','ENDPARAMETER','-','-'])
            print '\nStack before modification:',semStack
            #semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            semStackMan(element)
            
            print '\nStack after modification:',semStack
        elif(element == 18):
            
            tuples(['-','NOFORMALPARAMETER','-','-'])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 19):
            
            variables.globalSymbolTable.append(semStack[-1])
            variables.globalSymbolTable.append(['PROCEDURE'])
            
            variables.scopeFlag = 1
            variables.localSymbolTable = []
            
            variables.localSymbolTable.append(semStack[-1])
            variables.localSymbolTable.append(['PROCEDURE'])
            
            tuples([semStack[-1],'BEGINPROCEDURE','-','-'])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = semStack[-1:]
            
        elif(element == 20):
            
            variables.localSymbolTable.append(semStack[-1])
            variables.localSymbolTable.append([semStack[-2],'SCALAR',1,'-',semStack[-3]])
            
            if (semStack[-3] == 'VALUE'):
                tuples([semStack[-1],'FORMALVALPARAMETER',1,0])
            elif (semStack[-3] == 'REFERENCE'):
                tuples([semStack[-1],'FORMALREFPARAMETER',1,0])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 21):
            
            variables.localSymbolTable.append(semStack[-2])
            variables.localSymbolTable.append([semStack[-3],'VECTOR',semStack[-1],'-',semStack[-4]])
            
            if (semStack[-4] == 'VALUE'):
                tuples([semStack[-2],'FORMALVALPARAMETER',semStack[-1],0])
            elif (semStack[-4] == 'REFERENCE'):
                tuples([semStack[-2],'FORMALREFPARAMETER',semStack[-1],0])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 22):
            
            variables.localSymbolTable.append(semStack[-4])
            variables.localSymbolTable.append([semStack[-5],'MATRIX',semStack[-3],semStack[-1],semStack[-6]])
            
            if (semStack[-6] == 'VALUE'):
                tuples([semStack[-4],'FORMALVALPARAMETER',semStack[-3],semStack[-1]])
            elif (semStack[-6] == 'REFERENCE'):
                tuples([semStack[-4],'FORMALREFPARAMETER',semStack[-3],semStack[-1]])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 23):
            
            if(chkVar(semStack[-1])):
                print '\nError: Variable already exists in the local symbol table'+str(element)
            
            else:
                variables.localSymbolTable.append(semStack[-1])
                variables.localSymbolTable.append([semStack[-2],'SCALAR',1,'-',semStack[-3]])
            
                tuples(['-','BEGINPARAMETER','-','-'])
            
                if (semStack[-3] == 'VALUE'):
                    tuples([semStack[-1],'FORMALVALPARAMETER',1,0])
                elif (semStack[-3] == 'REFERENCE'):
                    tuples([semStack[-1],'FORMALREFPARAMETER',1,0])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 24):
            
            if(chkVar(semStack[-2])):
                print '\nError: Variable already exists in the local symbol table'+str(element)
            
            else:
                variables.localSymbolTable.append(semStack[-2])
                variables.localSymbolTable.append([semStack[-3],'VECTOR',semStack[-1],'-',semStack[-4]])
            
                tuples(['-','BEGINPARAMETER','-','-'])
            
                if (semStack[-4] == 'VALUE'):
                    tuples([semStack[-2],'FORMALVALPARAMETER',semStack[-1],0])
                elif (semStack[-4] == 'REFERENCE'):
                    tuples([semStack[-2],'FORMALREFPARAMETER',semStack[-1],0])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 25):
            
            if(chkVar(semStack[-4])):
                print '\nError: Variable already exists in the local symbol table'+str(element)
            
            else:
                variables.localSymbolTable.append(semStack[-4])
                variables.localSymbolTable.append([semStack[-5],'MATRIX',semStack[-3],semStack[-1],semStack[-6]])
            
                tuples(['-','BEGINPARAMETER','-','-'])
            
                if (semStack[-6] == 'VALUE'):
                    tuples([semStack[-4],'FORMALVALPARAMETER',semStack[-3],semStack[-1]])
                elif (semStack[-6] == 'REFERENCE'):
                    tuples([semStack[-4],'FORMALREFPARAMETER',semStack[-3],semStack[-1]])
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
            
        elif(element == 26):
            
            semStack[-(len(variables.usProductions[element]) - 3):] = ['VALUE']
            
        elif(element == 27):
            
            semStack[-(len(variables.usProductions[element]) - 3):] = ['REFERENCE']
            
        elif(element == 28):
            
            '''NO SEMANTICS FOR THIS PRODUCTION'''
            
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 29):
            
            tuples(['MAIN', 'LABEL', '-', '-'])
        
        elif(element == 30):
            
            '''NO SEMANTICS FOR THIS PRODUCTIOn'''
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 31):
            
            '''NO SEMANTICS FOR THIS PRODUCTION'''
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 32):
            
            '''NO SEMANTICS FOR THIS PRODUCTION'''
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 33):
            
            '''NO SEMANTICS FOR THIS PRODUCTION'''
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 34):
            
            '''NO SEMANTICS FOR THIS PRODUCTION'''
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 35):
            
            tuples(['SCANF', 'ENDOFINPUTPARAMETERS', '-', '-'])
            
            semStack.pop() 
        
        elif(element == 36):
            
            tuples(['PRINTF', 'ENDOFOUTPUTPARAMETERS', '-', '-'])
            
            semStack.pop()
        
        elif(element == 37):
            
            '''NO SEMANTICS FOR THIS PRODUCTION'''
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 38):
            
            tuples(['-', 'INPUTPARAMETER', semStack[-1], '-']) 
            
            semStack.pop()
            semStack.pop()
        
        elif(element == 39): 
            '''Verify the reduction, not semStack[-6]'''
            
            '''What is to be on the semantic stack after the semantics are performed'''
            if(isInt(semStack[-2])):
                if(variables.localSymbolTable.__contains__(semStack[-4])):
                    
                    tuples(['-', 'INPUTSUBPARAMETER', semStack[-6], semStack[-2]])
                    
                elif(variables.localSymbolTable.__contains__(semStack[-4])):
                    
                    tuples(['-', 'INPUTSUBPARAMETER', semStack[-6], semStack[-2]])
                    
                else:
                    print 'Error: The variable is not declared'+str(element)
            else:
                print 'Error: The subscript of the matrix is not an integer'+str(element)
            
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 40):
            
            '''What is to be on the semantic stack after the semantics are performed'''
            if(isInt(semStack[-4]) and isInt(semStack[-2])):
                if(variables.localSymbolTable.__contains__(semStack[-6])):
                    
                    tuples(['I$'+str(i), 'IMULT', variables.localSymbolTable[variables.localSymbolTable.index(semStack[-6])+1][3], semStack[-4]])
                    i = i+1
                        
                    tuples(['I$'+str(i), 'IADD', 'I$'+str(i-1), semStack[-2]])
                    i = i+1
                    
                    tuples(['-', 'INPUTSUBPARAMETER', semStack[-6], 'I$'+str(i - 1)])
            
                elif(variables.globalSymbolTable.__contains__(semStack[-6])):
                    
                    tuples(['I$'+str(i), 'IMULT', variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][3], semStack[-4]])
                    i = i+1
                        
                    tuples(['I$'+str(i), 'IADD', 'I$'+str(i-1), semStack[-2]])
                    i = i+1
                    
                    tuples(['-', 'INPUTSUBPARAMETER', semStack[-6], 'I$'+str(i - 1)])
                    
                else:
                    print 'Error: The variable is not declared'+str(element)
     
            else:
                print 'Error: The subscripts of the matrix are not integers'+str(element)
            
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 41):
            '''What is to be on the semantic stack after the semantics are performed'''
            
            tuples(['SCANF', 'CALL', '-', '-'])
            tuples(['-', 'INPUTPARAMETER', semStack[-1], '-'])
            
            semStack.pop()
        
        elif(element == 42):
            
            tuples(['-', 'OUTPUTPARAMETER', semStack[-1], '-']) 
            
            semStack.pop()
            semStack.pop()
        
        elif(element == 43):
            
            tuples(['-', 'OUTPUTPARAMETER', semStack[-1], '-'])
            
            semStack.pop()
            semStack.pop()
        
        elif(element == 44):
            
            '''What is to be on the semantic stack after the semantics are performed'''
            if(isInt(semStack[-2])):
                if(variables.localSymbolTable.__contains__(semStack[-4])):
                    tuples(['-', 'OUTPUTSUBPARAMETER', semStack[-4], semStack[-2]])
                    
                elif(variables.globalSymbolTable.__contains__(semStack[-4])):
                    
                    tuples(['-', 'OUTPUTSUBPARAMETER', semStack[-4], semStack[-2]])
                    
                else:
                    print 'Error: The variable is not declared'+str(element)
            else:
                print 'Error: The subscript of the matrix is not an integer'+str(element)
            
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            
        
        elif(element == 45):
            
            '''What is to be on the semantic stack after the semantics are performed'''
            if(isInt(semStack[-4]) and isInt(semStack[-2])):
                if(variables.localSymbolTable.__contains__(semStack[-6])):
                    
                    tuples(['I$'+str(i), 'IMULT', variables.localSymbolTable[variables.localSymbolTable.index(semStack[-6])+1][3], semStack[-4]])
                    i = i+1
                        
                    tuples(['I$'+str(i), 'IADD', 'I$'+str(i-1), semStack[-2]])
                    i = i+1
                    
                    tuples(['-', 'OUTPUTSUBPARAMETER', semStack[-6], 'I$'+str(i - 1)])
            
                elif(variables.globalSymbolTable.__contains__(semStack[-6])):
                    
                    tuples(['I$'+str(i), 'IMULT', variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][3], semStack[-4]])
                    i = i+1
                        
                    tuples(['I$'+str(i), 'IADD', 'I$'+str(i-1), semStack[-2]])
                    i = i+1
                    
                    tuples(['-', 'OUTPUTSUBPARAMETER', semStack[-6], 'I$'+str(i - 1)])
                    
                else:
                    print 'Error: The variable is not declared'+str(element)
     
            else:
                print 'Error: The subscripts of the matrix are not integers'+str(element)   
            
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 46):
            
            tuples(['PRINTF', 'CALL', '-', '-'])
            tuples(['-', 'OUTPUTPARAMETER', semStack[-1], '-'])
            
            semStack.pop()
        
        elif(element == 47):
            '''What is to be on the semantic stack after the semantics are performed'''
            tuples([semStack[-3], 'ENDACTUALPARAMETERLIST', '-', '-'])
            
            semStack.pop()
            semStack.pop()
            
        elif(element == 48):
            
            tuples(['-', 'NOACTUALPARAMETERS', '-', '-'])
        
        elif(element == 49):
            
            if(variables.globalSymbolTable.__contains__(semStack[-1])):
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-1])+1][0] == 'PROCEDURE'):
                    tuples([semStack[-1], 'CALL', '-', '-'])
                    semStack[-2] = semStack[-1]
                    
                else:
                    print 'The variable is not the name of a procedure'+str(element)
                    
            semStack.pop()
        
        elif(element == 50):
            '''What is to be on the semantic stack after the semantics are performed'''
            if(variables.globalSymbolTable.__contains__(semStack[-1])):
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-1])+1][1] == 'SCALAR'):
                    
                    if(semStack[-2] == 'VALUE'):
                        tuples(['-', 'ACTUALVPARAMETER', semStack[-1], '-'])
                    elif(semStack[-2] == 'REFERENCE'):
                        tuples(['-', 'ACTUALRPARAMETER', semStack[-1], '-'])
                        
                else:
                    print 'Error: The variable is not of type SCALAR'+str(element)
            else:
                print 'Error: The variable is not declared'+str(element)
                                        
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 51):
            '''What is to be on the semantic stack after the semantics are performed'''
            if(variables.globalSymbolTable.__contains__(semStack[-4])):
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-4])+1][1] == 'VECTOR'):
                    if(isInt(semStack[-2])):
                        
                        if(semStack[-7] == 'VALUE'):
                            tuples(['-', 'AVCTUALVSUBPARAMETER', semStack[-4], semStack[-2]])
                        
                        elif(semStack[-7] == 'REFERENCE'):
                            tuples(['-', 'AVCTUALRSUBPARAMETER', semStack[-4], semStack[-2]])
                            
                    else:
                        print 'Error: The index of vector are not of type INTEGER'+str(element)
                else:
                    print 'Error: The variable is not of type VECTOR'+str(element)
            else:
                print 'Error: The variable is not declared'+str(element)
                
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
                    
        elif(element == 52):
            '''What is to be on the semantic stack after the semantics are performed'''
            if(variables.globalSymbolTable.__contains__(semStack[-6])):
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][1] == 'MATRIX'):
                    if(isInt(semStack[-4]) and isInt(semStack[-2])):
                        
                        tuples(['I$'+str(i), 'IMULT', variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][3], semStack[-4]])
                        i = i+1
                        
                        tuples(['I$'+str(i), 'IADD', 'I$'+str(i - 1), semStack[-2]])
                        i = i+1
                        
                        if(semStack[-7] == 'VALUE'):
                            tuples(['-', 'AVCTUALVSUBPARAMETER', semStack[-6], 'I$'+str(i-1)])
                        
                        elif(semStack[-7] == 'REFERENCE'):
                            tuples(['-', 'AVCTUALRSUBPARAMETER', semStack[-6], 'I$'+str(i-1)])
                            
                    else:
                        print 'Error: The indexes of matrices are not of type INTEGER'+str(element)
                else:
                    print 'Error: The variable is not of type MATRIX'+str(element)
            else:
                print 'Error: The variable is not declared'+str(element)
            
            semStack.pop()        
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 53):
            '''What is to be on the semantic stack after performing the semantics'''
            
            if(variables.globalSymbolTable.__contains__(semStack[-1])):
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-1])+1][1] == 'SCALAR'):
                    tuples(['-', 'BEGINPERAMETERLIST', '-', '-'])
                    
                    if(semStack[-2] == 'VALUE'):
                        tuples(['-', 'ACTUALVPARAMETER', semStack[-1], '-'])
                    elif(semStack[-2] == 'REFERENCE'):
                        tuples(['-', 'ACTUALRPARAMETER', semStack[-1], '-'])
                        
                else:
                    print 'Error: The variable is not of type SCALAR'+str(element)
            else:
                print 'Error: The variable is not declared'+str(element)
                                        
            semStack.pop()
            semStack.pop()
            
        elif(element == 54):
            '''What is to be on the semantic stack after performing the semantics'''
            if(variables.globalSymbolTable.__contains__(semStack[-4])):
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-4])+1][1] == 'VECTOR'):
                    if(isInt(semStack[-2])):
                        tuples(['-', 'BEGINACTUALPARAMETERLIST', '-', '-'])
                        
                        if(semStack[-7] == 'VALUE'):
                            tuples(['-', 'AVCTUALVSUBPARAMETER', semStack[-4], semStack[-2]])
                        
                        elif(semStack[-7] == 'REFERENCE'):
                            tuples(['-', 'AVCTUALRSUBPARAMETER', semStack[-4], semStack[-2]])
                            
                    else:
                        print 'Error: The index of vector are not of type INTEGER'+str(element)
                else:
                    print 'Error: The variable is not of type VECTOR'+str(element)
            else:
                print 'Error: The variable is not declared'+str(element)
                
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 55):
            '''What is to be on the semantic stack after performing the semantics'''
            if(variables.globalSymbolTable.__contains__(semStack[-6])):
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][1] == 'MATRIX'):
                    if(isInt(semStack[-4]) and isInt(semStack[-2])):
                        tuples(['-', 'BEGINACTUALPARAMETERLIST', '-', '-'])
                        
                        tuples(['I$'+str(i), 'IMULT', variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][3], semStack[-4]])
                        i = i+1
                        
                        tuples(['I$'+str(i), 'IADD', 'I$'+str(i - 1), semStack[-2]])
                        i = i+1
                        
                        if(semStack[-7] == 'VALUE'):
                            tuples(['-', 'AVCTUALVSUBPARAMETER', semStack[-6], 'I$'+str(i-1)])
                        
                        elif(semStack[-7] == 'REFERENCE'):
                            tuples(['-', 'AVCTUALRSUBPARAMETER', semStack[-6], 'I$'+str(i-1)])
                            
                    else:
                        print 'Error: The indexes of matrices are not of type INTEGER'+str(element)
                else:
                    print 'Error: The variable is not of type MATRIX'+str(element)
            else:
                print 'Error: The variable is not declared'+str(element)
                    
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 56):
            
            tuples(['L$'+str(loop[-1]),'LABEL', '-', '-'])
            loop.pop()
            
            semStack.pop()
            semStack.pop()
            #semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 57):
            
            tuples(['L$'+str(loop[-1]), 'LABEL', '-', '-'])
            loop.pop()
                
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 58):
            
            tuples(['L$'+str(l), 'JUMP', 'TRUE', '-'])            
            
            tuples(['L$'+str(loop[-1]),'LABEL', '-', '-'])
            loop.pop()
            loop.append(l)
            
            l = l+1
            
            semStack.pop()
            semStack.pop()
        
        elif(element == 59):
            
            tuples(['L$'+str(l), 'CJUMP', semStack[-3], '-'])
            loop.append(l)
            l = l + 1
            
            semStack[-5] = semStack[-3]
            
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            
            #semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 60):
            if(isBoolean(semStack[-3])):
                tuples(['L$'+str(loop[-2]), 'JUMP', '-', '-'])
                tuples(['L$'+str(loop[-1]), 'LABEL', '-', '-'])
                #tuples(['L$'+str(l-(loop1-loop+1)), 'CJUMP', semStack[-3], '-'])
            
                loop.pop()
                loop.pop()
            
            semStack.pop()
            semStack.pop()
        
        elif(element == 61):
            if(isBoolean(semStack[-3])):
                
                tuples(['L$'+str(l), 'CJUMP', semStack[-3], '-'])
                loop.append(l)
                l = l + 1
                
            else:
                print ('\nError: The argument to while is not a boolean expression')
            
            semStack[-5] = semStack[-3]
            
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            
            #semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 62):
            
            tuples(['L$'+str(l), 'LABEL', '-', '-'])
            loop.append(l)
            l = l + 1
                
            semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 63):
            
            if(variables.localSymbolTable.__contains__(semStack[-3])):
                
                if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-3])+1][0] == 'INTEGER' and isReal(semStack[-1])):
                    tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-1], '-'])
                    semStack[-1] = 'I$'+str(i)
                    i = i+1
                    
                elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-3])+1][0] == 'REAL' and isInt(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                    semStack[-1] = 'R$'+str(r)
                    r = r+1
                    
                if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-3])+1][0] == 'INTEGER' and isInt(semStack[-1])):
                    tuples([semStack[-3], 'ISUBASSIGN', semStack[-1], '-'])
                
                elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-3])+1][0] == 'REAL' and isReal(semStack[-1])):
                    tuples([semStack[-3], 'RSUBASSIGN', semStack[-1], '-'])
                    
                semStack[-3] = semStack[-1]
                
            elif(variables.globalSymbolTable.__contains__(semStack[-3])):
                
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-3])+1][0] == 'INTEGER' and isReal(semStack[-1])):
                    tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-1], '-'])
                    semStack[-1] = 'I$'+str(i)
                    i = i+1
                    
                elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-3])+1][0] == 'REAL' and isInt(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                    semStack[-1] = 'R$'+str(r)
                    r = r+1
                    
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-3])+1][0] == 'INTEGER' and isInt(semStack[-1])):
                    tuples([semStack[-3], 'ISUBASSIGN', semStack[-1], '-'])
                
                elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-3])+1][0] == 'REAL' and isReal(semStack[-1])):
                    tuples([semStack[-3], 'RSUBASSIGN', semStack[-1], '-'])
                    
                semStack[-3] = semStack[-1]
                
            else:
                print 'Error: variables is not declared'+str(element)
                
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 64):
            
            if(isInt(semStack[-4])):
                if(variables.localSymbolTable.__contains__(semStack[-6])):
                    if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-6])+1][0] == 'INTEGER' and isReal(semStack[-1])):
                        tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-1], '-'])
                        semStack[-1] = 'I$'+str(i)
                        i = i+1
                    
                    elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-6])+1][0] == 'REAL' and isInt(semStack[-1])):
                        tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                        semStack[-1] = 'R$'+str(r)
                        r = r+1
                    
                    if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-6])+1][0] == 'INTEGER' and isInt(semStack[-1])):
                        tuples([semStack[-6], 'ISUBASSIGN', semStack[-1], semStack[-4]])
                        
                    elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-6])+1][0] == 'REAL' and isReal(semStack[-1])):
                        tuples([semStack[-6], 'RSUBASSIGN', semStack[-1], semStack[-4]])
                        
                    semStack[-6] = semStack[-1]
                    
                elif(variables.localSymbolTable.__contains__(semStack[-6])):
                    if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][0] == 'INTEGER' and isReal(semStack[-1])):
                        tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-1], '-'])
                        semStack[-1] = 'I$'+str(i)
                        i = i+1
                    
                    elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][0] == 'REAL' and isInt(semStack[-1])):
                        tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                        semStack[-1] = 'R$'+str(r)
                        r = r+1
                    
                    if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][0] == 'INTEGER' and isInt(semStack[-1])):
                        tuples([semStack[-6], 'ISUBASSIGN', semStack[-1], semStack[-4]])
                        
                    elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][0] == 'REAL' and isReal(semStack[-1])):
                        tuples([semStack[-6], 'RSUBASSIGN', semStack[-1], semStack[-4]])
                        
                    semStack[-6] = semStack[-1]
                     
                else:
                    print 'Error: The array is not declared'+str(element)
            else:
                print 'Error: The index to the array is not an Integer'+str(element)
            
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            
        elif(element == 65):
            
            if(isInt(semStack[-6]) and isInt(semStack[-4])):
                
                if(variables.localSymbolTable.__contains__(semStack[-8])):
                    if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-8])+1][0] == 'INTEGER' and isReal(semStack[-1])):
                        tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-1], '-'])
                        semStack[-1] = 'I$'+str(i)
                        i = i+1
                        
                    elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-8])+1][0] == 'REAL' and isInt(semStack[-1])):
                        tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                        semStack[-1] = 'R$'+str(r)
                        r = r+1
                        
                    tuples(['I$'+str(i), 'IMULT', variables.localSymbolTable[variables.localSymbolTable.index(semStack[-8])+1][3], semStack[-6]])
                    i = i+1
                    
                    tuples(['I$'+str(i), 'IADD', 'I$'+str(i-1), semStack[-4]])
                    i = i+1
                    
                    if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-8])+1][0] == 'INTEGER' and isInt(semStack[-1])):
                        tuples([semStack[-8], 'ISUBASSIGN', semStack[-1], 'I$'+str(i-1)])
                        
                    elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-8])+1][0] == 'REAL' and isReal(semStack[-1])):
                        tuples([semStack[-8], 'RSUBASSIGN', semStack[-1], 'I$'+str(i-1)])
                    
                    semStack[-8] = semStack[-1]
                        
                elif(variables.globalSymbolTable.__contains__(semStack[-8])):
                    if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-8])+1][0] == 'INTEGER' and isReal(semStack[-1])):
                        tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-1], '-'])
                        semStack[-1] = 'I$'+str(i)
                        i = i+1
                        
                    elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-8])+1][0] == 'REAL' and isInt(semStack[-1])):
                        tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                        semStack[-1] = 'R$'+str(r)
                        r = r+1
                        
                    tuples(['I$'+str(i), 'IMULT', variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-8])+1][3], semStack[-6]])
                    i = i+1
                    
                    tuples(['I$'+str(i), 'IADD', 'I$'+str(i-1), semStack[-4]])
                    i = i+1
                    
                    if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-8])+1][0] == 'INTEGER' and isInt(semStack[-1])):
                        tuples([semStack[-8], 'ISUBASSIGN', semStack[-1], 'I$'+str(i-1)])
                        
                    elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-8])+1][0] == 'REAL' and isReal(semStack[-1])):
                        tuples([semStack[-8], 'RSUBASSIGN', semStack[-1], 'I$'+str(i-1)])
                    
                    semStack[-8] = semStack[-1]
                    
                else:
                    print 'Error: The matrix is not declared'+str(element)
            else:
                print 'Error: The indexes to the matrix are not integers'+str(element)
            
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            
        elif(element == 66):
            
            if(variables.localSymbolTable.__contains__(semStack[-4])):
                
                if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-4])+1][0] == 'INTEGER' and isReal(semStack[-2])):
                    tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-2], '-'])
                    semStack[-2] = 'I$'+str(i)
                    i = i+1
                    
                elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-4])+1][0] == 'REAL' and isInt(semStack[-2])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-2], '-'])
                    semStack[-2] = 'R$'+str(r)
                    r = r+1
                    
                if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-4])+1][0] == 'INTEGER' and isInt(semStack[-2])):
                    tuples([semStack[-4], 'ISUBASSIGN', semStack[-2], '-'])
                
                elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-4])+1][0] == 'REAL' and isReal(semStack[-2])):
                    tuples([semStack[-4], 'RSUBASSIGN', semStack[-2], '-'])
                    
                semStack[-4] = semStack[-2]
                
            elif(variables.globalSymbolTable.__contains__(semStack[-4])):
                
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-4])+1][0] == 'INTEGER' and isReal(semStack[-2])):
                    tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-2], '-'])
                    semStack[-2] = 'I$'+str(i)
                    i = i+1
                    
                elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-4])+1][0] == 'REAL' and isInt(semStack[-2])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-2], '-'])
                    semStack[-2] = 'R$'+str(r)
                    r = r+1
                    
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-4])+1][0] == 'INTEGER' and isInt(semStack[-2])):
                    tuples([semStack[-4], 'ISUBASSIGN', semStack[-2], '-'])
                
                elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-4])+1][0] == 'REAL' and isReal(semStack[-2])):
                    tuples([semStack[-4], 'RSUBASSIGN', semStack[-2], '-'])
                    
                semStack[-4] = semStack[-2]
                
            else:
                print 'Error: variables is not declared'+str(element)+semStack[-5]
                
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 67):
            
            if(isInt(semStack[-5])):
                
                if(variables.localSymbolTable.__contains__(semStack[-7])):
                    if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-7])+1][0] == 'INTEGER' and isReal(semStack[-2])):
                        tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-2], '-'])
                        semStack[-2] = 'I$'+str(i)
                        i = i+1
                    
                    elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-7])+1][0] == 'REAL' and isInt(semStack[-2])):
                        tuples(['R$'+str(r), 'CONVERTITOR', semStack[-2], '-'])
                        semStack[-2] = 'R$'+str(r)
                        r = r+1
                    
                    if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-7])+1][0] == 'INTEGER' and isInt(semStack[-2])):
                        tuples([semStack[-7], 'ISUBASSIGN', semStack[-2], semStack[-5]])
                        
                    elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-7])+1][0] == 'REAL' and isReal(semStack[-2])):
                        tuples([semStack[-7], 'RSUBASSIGN', semStack[-2], semStack[-5]])
                        
                    semStack[-7] = semStack[-2]
                    
                elif(variables.globalSymbolTable.__contains__(semStack[-7])):
                    if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-7])+1][0] == 'INTEGER' and isReal(semStack[-2])):
                        tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-2], '-'])
                        semStack[-2] = 'I$'+str(i)
                        i = i+1
                    
                    elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-7])+1][0] == 'REAL' and isInt(semStack[-2])):
                        tuples(['R$'+str(r), 'CONVERTITOR', semStack[-2], '-'])
                        semStack[-2] = 'R$'+str(r)
                        r = r+1
                    
                    if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-7])+1][0] == 'INTEGER' and isInt(semStack[-2])):
                        tuples([semStack[-7], 'ISUBASSIGN', semStack[-2], semStack[-5]])
                        
                    elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-7])+1][0] == 'REAL' and isReal(semStack[-2])):
                        tuples([semStack[-7], 'RSUBASSIGN', semStack[-2], semStack[-5]])
                        
                    semStack[-7] = semStack[-2] 
                else:
                    print 'Error: The array is not declared'+str(element)
            else:
                print 'Error: The index to the array is not an Integer'+str(element)
            
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            
        elif(element == 68):
            
            if(isInt(semStack[-7]) and isInt(semStack[-5])):
                
                if(variables.localSymbolTable.__contains__(semStack[-9])):
                    if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-9])+1][0] == 'INTEGER' and isReal(semStack[-2])):
                        tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-2], '-'])
                        semStack[-2] = 'I$'+str(i)
                        i = i+1
                        
                    elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-9])+1][0] == 'REAL' and isInt(semStack[-2])):
                        tuples(['R$'+str(r), 'CONVERTITOR', semStack[-2], '-'])
                        semStack[-2] = 'R$'+str(r)
                        r = r+1
                        
                    tuples(['I$'+str(i), 'IMULT', variables.localSymbolTable[variables.localSymbolTable.index(semStack[-9])+1][3], semStack[-7]])
                    i = i+1
                    
                    tuples(['I$'+str(i), 'IADD', 'I$'+str(i-1), semStack[-5]])
                    i = i+1
                    
                    if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-9])+1][0] == 'INTEGER' and isInt(semStack[-2])):
                        tuples([semStack[-9], 'ISUBASSIGN', semStack[-2], 'I$'+str(i-1)])
                        
                    elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-9])+1][0] == 'REAL' and isReal(semStack[-2])):
                        tuples([semStack[-9], 'RSUBASSIGN', semStack[-2], 'I$'+str(i-1)])
                    
                    semStack[-9] = semStack[-2]
                        
                elif(variables.globalSymbolTable.__contains__(semStack[-9])):
                    if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-9])+1][0] == 'INTEGER' and isReal(semStack[-2])):
                        tuples(['I$'+str(i), 'CONVERTRTOI', semStack[-2], '-'])
                        semStack[-2] = 'I$'+str(i)
                        i = i+1
                        
                    elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-9])+1][0] == 'REAL' and isInt(semStack[-2])):
                        tuples(['R$'+str(r), 'CONVERTITOR', semStack[-2], '-'])
                        semStack[-2] = 'R$'+str(r)
                        r = r+1
                        
                    tuples(['I$'+str(i), 'IMULT', variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-9])+1][3], semStack[-7]])
                    i = i+1
                    
                    tuples(['I$'+str(i), 'IADD', 'I$'+str(i-1), semStack[-5]])
                    i = i+1
                    
                    if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-9])+1][0] == 'INTEGER' and isInt(semStack[-2])):
                        tuples([semStack[-9], 'ISUBASSIGN', semStack[-2], 'I$'+str(i-1)])
                        
                    elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-9])+1][0] == 'REAL' and isReal(semStack[-2])):
                        tuples([semStack[-9], 'RSUBASSIGN', semStack[-2], 'I$'+str(i-1)])
                    
                    semStack[-9] = semStack[-2]
                    
                else:
                    print 'Error: The matrix is not declared'+str(element)
            else:
                print 'Error: The indexes to the matrix are not integers'+str(element)
            
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 69):
            '''Verify the check for boolean expression'''
                
            if(isBoolean(semStack[-3]) and isBoolean(semStack[-1])):
                tuples(['B$'+str(b), 'OR', semStack[-3], semStack[-1]])
                semStack[-3] = 'B$'+str(b)
                b = b+1
                
            else:
                print 'Error: The operands to the operator & are not boolean'+str(element)
                
            semStack.pop()
            semStack.pop()
        
        elif(element == 70):
            
            '''NO SEMANTICS FOR THIS REDUCTION'''
            #semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 71):
            '''Verify the check for boolean expression'''
                
            if(isBoolean(semStack[-3]) and isBoolean(semStack[-1])):
                tuples(['B$'+str(b), 'AND', semStack[-3], semStack[-1]])
                semStack[-3] = 'B$'+str(b)
                b = b+1
                
            else:
                print 'Error: The operands to the operator & are not boolean'+str(element)
                
            semStack.pop()
            semStack.pop()
        
        elif(element == 72):
            
            '''NO SEMANTICS FOT THIS REDUCTION'''
            #semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 73):
            '''Verify the check for boolean expression'''
            
            if(isBoolean(semStack[-1])):
                
                tuples(['B$'+str(b), 'NOT', semStack[-1], '-'])
                semStack[-2] = 'B$'+str(b)
                b = b+1
                
            else:
                print 'Error: The operand to ! is not a boolean value'+str(element)
            
            semStack.pop()
        
        elif(element == 74):
            
            '''NO SEMANTICS FOR THIS REDUCTION'''
            #semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 75):
            
            if((variables.localSymbolTable.__contains__(semStack[-3]) or variables.globalSymbolTable.__contains__(semStack[-3]) or isInt(semStack[-3]) or isReal(semStack[-3])) and (variables.localSymbolTable.__contains__(semStack[-1]) or variables.globalSymbolTable.__contains__(semStack[-1]) or isInt(semStack[-1]) or isReal(semStack[-1]))):
            
                if(isInt(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['B$'+str(b), 'ILT', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
                
                elif(isInt(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3], '-'])
                    semStack[-3] = 'R$'+str(r)
                    r = r+1
                
                elif(isReal(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                    semStack[-1] = 'R$'+str(r)
                    r = r+1
                
                if(isReal(semStack[-3]) and isReal(semStack[-1])):
                
                    tuples(['B$'+str(b), 'RLT', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
            else:
                print ("\nError: The operands for the binary operator are not declared")
                
            semStack.pop()
            semStack.pop()
        
        elif(element == 76):
            
            if((variables.localSymbolTable.__contains__(semStack[-3]) or variables.globalSymbolTable.__contains__(semStack[-3]) or isInt(semStack[-3]) or isReal(semStack[-3])) and (variables.localSymbolTable.__contains__(semStack[-1]) or variables.globalSymbolTable.__contains__(semStack[-1]) or isInt(semStack[-1]) or isReal(semStack[-1]))):
            
                if(isInt(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['B$'+str(b), 'ILE', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
                
                elif(isInt(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3], '-'])
                    semStack[-3] = 'R$'+str(r)
                    r = r+1
                
                elif(isReal(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                    semStack[-1] = 'R$'+str(r)
                    r = r+1
                
                if(isReal(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['B$'+str(b), 'RLE', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
            
            else:
                print ("\nError: The operands for the binary operator are not declared")
                
            semStack.pop()
            semStack.pop()
        
        elif(element == 77):
            
            if((variables.localSymbolTable.__contains__(semStack[-3]) or variables.globalSymbolTable.__contains__(semStack[-3]) or isInt(semStack[-3]) or isReal(semStack[-3])) and (variables.localSymbolTable.__contains__(semStack[-1]) or variables.globalSymbolTable.__contains__(semStack[-1]) or isInt(semStack[-1]) or isReal(semStack[-1]))):
                
                if(isInt(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['B$'+str(b), 'IGT', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
                
                elif(isInt(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3], '-'])
                    semStack[-3] = 'R$'+str(r)
                    r = r+1
                
                elif(isReal(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                    semStack[-1] = 'R$'+str(r)
                    r = r+1
                
                if(isReal(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['B$'+str(b), 'RGT', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
                    
            else:
                print ("\nError: The operands for the binary operator are not declared")
            
            semStack.pop()
            semStack.pop()
        
        elif(element == 78):
            
            if((variables.localSymbolTable.__contains__(semStack[-3]) or variables.globalSymbolTable.__contains__(semStack[-3]) or isInt(semStack[-3]) or isReal(semStack[-3])) and (variables.localSymbolTable.__contains__(semStack[-1]) or variables.globalSymbolTable.__contains__(semStack[-1]) or isInt(semStack[-1]) or isReal(semStack[-1]))):
            
                if(isInt(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['B$'+str(b), 'IGE', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
                
                elif(isInt(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3], '-'])
                    semStack[-3] = 'R$'+str(r)
                    r = r+1
                
                elif(isReal(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                    semStack[-1] = 'R$'+str(r)
                    r = r+1
                
                if(isReal(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['B$'+str(b), 'RGE', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
                        
            else:
                print ("\nError: The operands for the binary operator are not declared")
            
            semStack.pop()
            semStack.pop()
        
        elif(element == 79):
            
            if((variables.localSymbolTable.__contains__(semStack[-3]) or variables.globalSymbolTable.__contains__(semStack[-3]) or isInt(semStack[-3]) or isReal(semStack[-3])) and (variables.localSymbolTable.__contains__(semStack[-1]) or variables.globalSymbolTable.__contains__(semStack[-1]) or isInt(semStack[-1]) or isReal(semStack[-1]))):
                
                if(isInt(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['B$'+str(b), 'IEQ', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
                
                elif(isInt(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3], '-'])
                    semStack[-3] = 'R$'+str(r)
                    r = r+1
                
                elif(isReal(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                    semStack[-1] = 'R$'+str(r)
                    r = r+1
                
                if(isReal(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['B$'+str(b), 'REQ', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
            else:
                
                print ("\nError: The operands for the binary operator are not declared")     
            
            semStack.pop()
            semStack.pop()
        
        elif(element == 80):
            
            if((variables.localSymbolTable.__contains__(semStack[-3]) or variables.globalSymbolTable.__contains__(semStack[-3]) or isInt(semStack[-3]) or isReal(semStack[-3])) and (variables.localSymbolTable.__contains__(semStack[-1]) or variables.globalSymbolTable.__contains__(semStack[-1]) or isInt(semStack[-1]) or isReal(semStack[-1]))):
            
                if(isInt(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['B$'+str(b), 'INE', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
                
                elif(isInt(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3], '-'])
                    semStack[-3] = 'R$'+str(r)
                    r = r+1
                
                elif(isReal(semStack[-3]) and isInt(semStack[-1])):
                    tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1], '-'])
                    semStack[-1] = 'R$'+str(r)
                    r = r+1
                
                if(isReal(semStack[-3]) and isReal(semStack[-1])):
                    tuples(['B$'+str(b), 'RNE', semStack[-3], semStack[-1]])
                    semStack[-3] = 'B$'+str(b)
                    b = b+1
                        
            else:
                
                print ("\nError: The operands for the binary operator are not declared")
            
            semStack.pop()
            semStack.pop()
        
        elif(element == 81):
            
            '''NO Semantics for this reduction'''
            #semStack[-(len(variables.usProductions[element]) - 3):] = [variables.symbols[variables.usProductions[element][-1:][0] - 1]]
        
        elif(element == 82):
            
            '''Verify the type checking of variables for this case'''
            
            if(isInt(semStack[-1]) and isInt(semStack[-3])):
                tuples(['I$'+str(i), 'IADD', semStack[-3], semStack[-1]])
                semStack[-3] = 'I$'+str(i)
                i = i+1
                
            elif(isInt(semStack[-1]) and isReal(semStack[-3])):
                tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1],'-'])
                semStack[-1] = 'R$'+str(r)
                r = r+1
                
            elif(isReal(semStack[-1]) and isInt(semStack[-3])):
                tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3],'-'])
                semStack[-3] = 'R$'+str(r)
                r = r+1
                
            if(isReal(semStack[-1]) and isReal(semStack[-3])):
                tuples(['R$'+str(r), 'RADD', semStack[-3], semStack[-1]])
                semStack[-3] ='R$'+str(r)
                r = r+1
                
            semStack.pop()
            semStack.pop()
                    
        elif(element == 83):
            
            '''Verify the type checking of variables for this case'''
            
            if(isInt(semStack[-1]) and isInt(semStack[-3])):
                tuples(['I$'+str(i), 'ISUB', semStack[-3], semStack[-1]])
                semStack[-3] = 'I$'+str(i)
                i = i+1
                
            elif(isInt(semStack[-1]) and isReal(semStack[-3])):
                tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1],'-'])
                semStack[-1] = 'R$'+str(r)
                r = r+1
                
            elif(isReal(semStack[-1]) and isInt(semStack[-3])):
                tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3],'-'])
                semStack[-3] = 'R$'+str(r)
                r = r+1
                
            if(isReal(semStack[-1]) and isReal(semStack[-3])):
                tuples(['R$'+str(r), 'RSUB', semStack[-3], semStack[-1]])
                semStack[-3] ='R$'+str(r)
                r = r+1
                
            semStack.pop()
            semStack.pop()
        
        elif(element == 84):
            
            '''Verify the type checking of variables for this case'''
            
            if(isInt(semStack[-1])):
                tuples(['I$'+str(i), 'ISUB', 0, semStack[-1]])
                semStack[-2] = 'I$'+str(i)
                i = i+1
                
            '''elif(isInt(semStack[-1]) and isReal(semStack[-3])):
                tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3],'-'])
                semStack[-3] = 'R$'+str(r)
                r = r+1
                
            elif(isReal(semStack[-1]) and isInt(semStack[-3])):
                tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1],'-'])
                semStack[-1] = 'R$'+str(r)
                r = r+1'''
                
            if (isReal(semStack[-1])):
                tuples(['R$'+str(r), 'RSUB', 0, semStack[-1]])
                semStack[-2] ='R$'+str(r)
                r = r+1
                
            #semStack.pop()
            semStack.pop()
        
        elif(element == 85):
            
            ''' It has no semantics'''
        
        elif(element == 86):
            
            '''Verify the type checking of variables for this case'''
            
            if(isInt(semStack[-1]) and isInt(semStack[-3])):
                tuples(['I$'+str(i), 'IMUL', semStack[-3], semStack[-1]])
                semStack[-3] = 'I$'+str(i)
                i = i+1
                
            elif(isInt(semStack[-1]) and isReal(semStack[-3])):
                tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1],'-'])
                semStack[-1] = 'R$'+str(r)
                r = r+1
                
            elif(isReal(semStack[-1]) and isInt(semStack[-3])):
                tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3],'-'])
                semStack[-3] = 'R$'+str(r)
                r = r+1
                
            if(isReal(semStack[-1]) and isReal(semStack[-3])):
                tuples(['R$'+str(r), 'RMUL', semStack[-3], semStack[-1]])
                semStack[-3] ='R$'+str(r)
                r = r+1
                
            semStack.pop()
            semStack.pop()
        
        elif(element == 87):
            
            '''Verify the type checking of variables for this case'''
            
            if(isInt(semStack[-1]) and isInt(semStack[-3])):
                tuples(['I$'+str(i), 'IDIV', semStack[-3], semStack[-1]])
                semStack[-3] = 'I$'+str(i)
                i = i+1
                
            elif(isInt(semStack[-1]) and isReal(semStack[-3])):
                
                tuples(['R$'+str(r), 'CONVERTITOR', semStack[-1],'-'])
                semStack[-1] = 'R$'+str(r)
                r = r+1
                
            elif(isReal(semStack[-1]) and isInt(semStack[-3])):
                tuples(['R$'+str(r), 'CONVERTITOR', semStack[-3],'-'])
                semStack[-3] = 'R$'+str(r)
                r = r+1
                
            if(isReal(semStack[-1]) and isReal(semStack[-3])):
                tuples(['R$'+str(r), 'RDIV', semStack[-3], semStack[-1]])
                semStack[-3] ='R$'+str(r)
                r = r+1
                
            semStack.pop()
            semStack.pop()
                        
        elif(element == 88):
            
            '''NO SEMANTICS'''
        
        elif(element == 89):
            
            semStack[-3] = semStack[-2]
            
            semStack.pop()
            semStack.pop()
                
        elif(element == 90):
            
            if(isInt(semStack[-2]) and isInt(semStack[-4])):
                
                if(variables.localSymbolTable.__contains__(semStack[-6])):
                    
                    tuples(['I$'+str(i), 'IMULT', variables.localSymbolTable[variables.localSymbolTable.index(semStack[-6])+1][3], semStack[-4]])
                    i = i+1
                        
                    tuples(['I$'+str(i), 'IADD', 'I$'+str(i-1), semStack[-2]])
                    i = i+1
                        
                    if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-6])+1][0] == 'INTEGER'):
                        tuples(['I$'+str(i), 'SUBLOAD', semStack[-6], 'I$'+str(i-1)])
                        semStack[-6] = 'I$'+str(i)
                        i = i+1
                        
                    elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-6])+1][0] == 'REAL'):
                        tuples(['R$'+str(r), 'SUBLOAD', semStack[-6], 'I$'+str(i-1)])
                        semStack[-6] = 'R$'+str(r)
                        r = r+1
                    
                elif(variables.globalSymbolTable.__contains__(semStack[-6])):
                        
                    tuples(['I$'+str(i), 'IMULT', variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][3], semStack[-4]])
                    i = i+1
                        
                    tuples(['I$'+str(i), 'IADD', 'I$'+str(i-1), semStack[-2]])
                    i = i+1
                        
                    if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][0] == 'INTEGER'):
                        tuples(['I$'+str(i), 'SUBLOAD', semStack[-6], 'I$'+str(i-1)])
                        semStack[-6] = 'I$'+str(i)
                        i = i+1
                        
                    elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-6])+1][0] == 'REAL'):
                        tuples(['R$'+str(r), 'SUBLOAD', semStack[-6], 'I$'+str(i-1)])
                        semStack[-6] = 'R$'+str(r)
                        r = r+1
                
                else:
                
                    print 'The variable is not declared'+str(element)
                
            else:
                
                print 'The subscripts of the arrays are not integers'+str(element)
             
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
            semStack.pop()
                
        elif(element == 91):
        
            if(isInt(semStack[-2])):
                
                if(variables.localSymbolTable.__contains__(semStack[-4])):
                    
                    if(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-4]) + 1][0] == 'INTEGER'):
                        tuples(['I$'+str(i), 'SUBLOAD', semStack[-4], semStack[-2]])
                        semStack[-4] = 'I$'+str(i)
                        i = i+1
                        
                    elif(variables.localSymbolTable[variables.localSymbolTable.index(semStack[-4]) + 1][0] == 'REAL'):
                        tuples(['R$'+str(r), 'SUBLOAD', semStack[-4], semStack[-2]])
                        semStack[-4] = 'R$'+str(r)
                        r = r+1
                        
                elif(variables.globalSymbolTable.__contains__(semStack[-4])):
                    
                    if(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-4]) + 1][0] == 'INTEGER'):
                        tuples(['I$'+str(i), 'SUBLOAD', semStack[-4], semStack[-2]])
                        semStack[-4] = 'I$'+str(i)
                        i = i+1
                        
                    elif(variables.globalSymbolTable[variables.globalSymbolTable.index(semStack[-4]) + 1][0] == 'REAL'):
                        tuples(['R$'+str(r), 'SUBLOAD', semStack[-4], semStack[-2]])
                        semStack[-4] = 'R$'+str(r)
                        r = r+1 
                    
                else:
                    print 'Error: The variable is not declared'+str(element)
                
            else:
                print 'Error: The type of the subscript is not integer'+str(element)
                
            semStack.pop()
            semStack.pop()
            semStack.pop()
        
        elif(element == 92):
            
            '''NO SEMANTICS'''
        
        elif(element == 93):
            
            '''NO SEMANTICS'''
        
        elif(element == 94):
            
            '''NO SEMANTICS'''
        
        elif(element == 95):
            
            '''NO SEMANTICS'''
            
    if(variables.flag[12] == True):
        print '\n The semantic stack after reduction:', semStack
    #print '\n',semStack, element
            
def tuples(tup):
    #print semStack
    if tup[1]=='MEMORY':
        if variables.scopeFlag == 0:
            tup.append(variables.globalSymbolTable[-1][0])
        else:
            tup.append(variables.localSymbolTable[-1][0])
    #print pragmatics.assem[-1]
    #print 'flag',variables.scopeFlag
    if(variables.flag[13] == True):
        print '\nTuples: ',tup
       
    if(variables.flag[15] == True and variables.scopeFlag == 0):
        print '\nGlobal Symbol Table entry: ',variables.globalSymbolTable[-2],variables.globalSymbolTable[-1]
    elif(variables.flag[15] == True and variables.scopeFlag == 1):
        print '\nLocal Symbol Table entry: ',variables.localSymbolTable[-2],variables.localSymbolTable[-1]
    
    
    pragmatics.tuples(tup, variables.scopeFlag)
        
def chkVar(var):
    if(variables.scopeFlag == 0):
        #print '\nChecking in global symbol table',var,variables.globalSymbolTable.__contains__(var)
        return(variables.globalSymbolTable.__contains__(var))
    
    elif(variables.scopeFlag == 1):
        # print '\nChecking in global symbol table'
        return(variables.localSymbolTable.__contains__(var))
    
def semStackMan(el):
    global semStack
    if (len(variables.usProductions[el][2:-1]) > 1):
        semStack = semStack[:-(len(variables.usProductions[el][2:-1]) - 1)]
        
def isInt(var):
    
    try:
        if (type(int(var)) is int):
            return True
    
    except ValueError:
        if(type(var) is str):
        
            if(var[0] == 'I' and var[1] == '$'):
                return True
        
            elif(variables.localSymbolTable.__contains__(var)):
                if(variables.localSymbolTable[variables.localSymbolTable.index(var)+1][0] == 'INTEGER'):
                    return True
        
            elif(variables.globalSymbolTable.__contains__(var)):
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(var)+1][0] == 'INTEGER'):
                    return True
        
        return False

def isReal(var):
    try:
        if (type(float(var)) is float):
            try:
                if(float(var) == int(var)):
                    return False
            except ValueError:
                return True
    
    except ValueError:    
        if(type(var) is str):
    
            if(var[0] == 'R' and var[1] == '$'):
                return True
        
            elif(variables.localSymbolTable.__contains__(var)):
                if(variables.localSymbolTable[variables.localSymbolTable.index(var)+1][0] == 'REAL'):
                    return True
        
            elif(variables.globalSymbolTable.__contains__(var)):
                if(variables.globalSymbolTable[variables.globalSymbolTable.index(var)+1][0] == 'REAL'):
                    return True
        
        return False

def isBoolean(var):
    if(var == 'True' or var == 'False' or (var[0] == 'B' and var[1] == '$')):
        return True
    else:
        return False
        
