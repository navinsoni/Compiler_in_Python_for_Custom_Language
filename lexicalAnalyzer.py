import re
import time
import parser
import variables

print "Name: Navin Soni, Email: nsoni@clemson.edu"
print "Name: Vishwanath Chennuru, Email: vchennu@clemson.edu"
print "Timestamp :",time.asctime(time.localtime(time.time())) 

identifier = {'start':'1', 'prog':'2', 'body':'3', 'declpart':'4', 'decllist':'5', 'declstat':'6', 'type':'7', 'procpart':'8', 'proclist':'9', 'proc':'10', 'prochead':'11', 'procname':'12', 'fparmlist':'13', 'calltype':'14', 'execpart':'15', 'exechead':'16', 'statlist':'17', 'stat':'18', 'inputstat':'19', 'outputstat':'20', 'callstat':'21', 'callname':'22', 'aparmlist':'23', 'ifstat':'24', 'ifthen':'25', 'ifhead':'26', 'whilestat':'27', 'whileexpr':'28', 'whilehd':'29', 'astat':'30', 'bexpr':'31', 'andexpr':'32', 'notexpr':'33', 'relexpr':'34', 'aexpr':'35', 'term':'36', 'primary':'37', 'constant':'38','var':'41','integer':'44','string':'59','real':'83'}

keyword = {'END':'39', 'PROGRAM':'40', 'DECLARE':'42', 'REAL':'47', 'INTEGER':'46', 'PROCEDURE':'49', 'VALUE':'52', 'REFERENCE':'53', 'MAIN':'54', 'INPUT':'58', 'OUTPUT':'60', 'CALL':'61', 'ELSE':'62', 'IF':'63', 'THEN':'66', 'DO':'67', 'WHILE':'68'}

single_ascii = {';':'43',':':'57',',':'50','[':'55',']':'56','(':'64',')':'65','<':'73','>':'75','!':'72','+':'79','-':'80','*':'81','/':'82','{':'51','}':'48','|':'70','&':'71'}

multi_ascii = {'==':'77', '!=':'78', '<=':'74', '>=':'76', '<-':'69', '::':'45'}

code = ['59','83','44',single_ascii,multi_ascii,'41',keyword,'85']

def flags(each_line, flag):
    if re.search('\+',each_line) :
        flag[int(each_line.split('+')[1])] = True
    else :
        flag[int(each_line.split('-')[1])] = False


comment = False

hash_c = False

string = False

far = '{:>60}'

conditions = re.compile('(\".*?\")|(\++\d+\.+\d+|\d+\.+\d+|\-+\d+\.+\d+)|(\-+\d+|\++\d+|\d+)|(==|!=|<=|>=|<-|::)|(//|/\*|\*/|##|#|\"|;|:|\[|\]|<|>|!|\+|-|\*|/|{|}|\||&|\(|\)|\.|`|~|\@|=|,)|([a-z][a-zA-Z0-9_]*)|([a-z]+)|([A-Z]+)')

input_file = raw_input("Enter filename: ")

try:
    input_data = open(input_file)
except:

    print "File not present" 
    
    exit()
queue = []    
for input_line in input_data:

    if variables.flag[1] == True:
        print input_line
        
    line_check = conditions.findall(input_line)

    for each_line in line_check:
        i=0;
        for each in each_line:
            if(each!=''):
                break;
            else:
                i=i+1;
        dat = ''
        if each_line[i] == '/*' :
            if comment == False :
                comment = True
    
        if each_line[i] == '*/' :
        
            if comment == True :
                comment = False

        if each_line[i] == '//':
            break

        if each_line[i] == '##' and comment == False:
            if hash_c == False :
                hash_c = True
            else :
                hash_c = False
        
        if (hash_c == True and each_line[i] != "##"):
            if re.search('\+[0-9]+|\-[0-9]+', each_line[i]) :
                flags(each_line[i],variables.flag)
                
        if (hash_c == False and re.search('\+', each) and comment == False):
            if (i==1 or i==2):

                dat = "Token : + Code : 79"
                queue.append(79)
                variables.var.append('+')
                if(variables.flag[2] == True):
                    print far.format(dat)
                each = each.split('+')[1]
        
        if (hash_c == False and comment == False and not re.search('##', each_line[i]) and each != '*/'):
            if i == 0:
                dat =  "Token : "+each+" Code : "+code[i];
                queue.append(int(code[i]))
                variables.var.append(each)
                if(variables.flag[2] == True):
                    print far.format(dat)

            if i == 1:
                cr = re.compile('[1-9].*[1-9]')
                try : 
                    fr = cr.findall(each)[0]
                except:
                    fr =''
                if(re.search('\.', fr)) and len(fr)<9 :
                    dat = "Token : "+each+" Code : "+code[i];
                    queue.append(int(code[i]))
                    variables.var.append(each)
                    if(variables.flag[2] == True):
                        print far.format(dat)
                elif len(fr)<8 :
                    dat = "Token : "+each+" Code : "+code[i];
                    queue.append(int(code[i]))
                    variables.var.append(each)
                    if(variables.flag[2] == True):
                        print far.format(dat)
                else:
                    dat = "Invalid Real Number : "+each
                    if(variables.flag[2] == True):
                        print far.format(dat)
            
            if i == 2 and len(each)<10:
                dat = "Token : "+each+" Code : "+code[i];
                queue.append(int(code[i]))
                variables.var.append(each)
                if(variables.flag[2] == True):
                    print far.format(dat)
            
            elif i == 2 and len(each)<11 and re.search('\-', each):
                dat = "Token : "+each+" Code : "+code[i];
                queue.append(int(code[i]))
                variables.var.append(each)
                if(variables.flag[2] == True):
                    print far.format(dat)
            
            elif i==2:
                dat = "Invalid Number : "+each
                if(variables.flag[2] == True):
                    print far.format(dat)
            
            if i == 3 and each in multi_ascii:   
                dat = "Token : "+each+" Code : "+multi_ascii[each];
                queue.append(int(multi_ascii[each]))
                variables.var.append(each)
                if(variables.flag[2] == True):
                    print far.format(dat)
            
            elif i == 3:
                dat = "Invalid Multi Ascii : "+each;
                
                if(variables.flag[2] == True):
                    print far.format(dat)
            
            if i == 4 and each in single_ascii:
                dat = "Token : "+each+" Code : "+single_ascii[each];
                queue.append(int(single_ascii[each]))
                variables.var.append(each)
                if(variables.flag[2] == True):
                    print far.format(dat)
            
            elif i == 4:
                dat = "Invalid Single Ascii : "+each;
                if(variables.flag[2] == True):
                    print far.format(dat)
            
            if i == 5 and len(each)<17:   
                dat = "Token : "+each+" Code : "+code[i];
                queue.append(int(code[i]))
                variables.var.append(each)
                if(variables.flag[2] == True):
                    print far.format(dat)
            
            elif i == 5:
                dat = "Invalid Identifier : "+each;
                if(variables.flag[2] == True):
                    print far.format(dat)
            
            if i == 7 and each in keyword:
                dat = "Token : "+each+" Code : "+keyword[each];
                queue.append(int(keyword[each]))
                variables.var.append(each)
                if(variables.flag[2] == True):
                    print far.format(dat)
            
            elif i == 7:
                dat = "Invalid Keyword : "+each;
                if(variables.flag[2] == True):
                    print far.format(dat)
    

    if (len(queue) > 0):
        parser.reduction(queue[:])                  # Sending symbol queue for reduction if the queue is not empty
        queue = []                                  # Resetting the queue
        
    if comment == False:
        print 
        #print

parser.reduction([])


'''print "\nLocal symbol table: "
for each in range(0,len(variables.localSymbolTable),2):
print '\n',variables.localSymbolTable[each],variables.localSymbolTable[each+1]'''
print '\n',variables.globalSymbolTable
print '\n',variables.localSymbolTable
