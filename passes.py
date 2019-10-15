programCounterX = 0
lines = []
symbol_Table=[]
ErrorFlag = False
ErrorList = []
opCode_Table = {'CLA': 0, 'LAC': 1, 'SAC': 2, 'ADD': 3, 'SUB': 4, 'BRZ': 5, 'BRN': 6, 'BRP': 7, 'INP': 8, 'DSP': 9, 'MUL': 10, 'DIV': 11, 'STP': 12, 'DW':13}


def lineCheck(line):
    # used to check if line[0] is a label or symbol
    if line[0][-1] == ':':         # it will have ':' at its end for label
        return 1
    else:
        return 2                   # else it would be a symbol


def passOne(text):
    global programCounterX
    STP_found = 0                         # flag to check STP is present in the code
    # symbolX = {'name': '', 'isUsed': False, 'isFound': False, 'variableAddress': -1}
    
    for i in text:
        if i == '':
            text.remove(i)
    # programCounter = 0
    for line in text:
        foundFlag = False
        flag = True
        line = line.split(' ')   # done splitting about " "(space)
        for i in line:
            if i == '':
                line.remove(i)
        # print(line)
        lines.append(line)     # here we are inserting the line list in the main list
        # print(line)

        '''The len of the line can be 1,2,3 and we will now proceed to them'''
        if len(line) == 2:
            # here all instruction of two words will be handled like 'ADD l1' , 'SUB l2' etc
            # print("2"+ str(line))
            '''Check for line[1] in the list if its a variable add to symbol table or label'''
            val = lineCheck(line)
            # print(val)
            if val == 1:
                '''check label with STP and CLA'''
                label_name = line[0][:len(line[0])-1]
                # print(label_name)
                for i in symbol_Table:
                    if i['name'] == label_name:          # check if symbol is already present in the symbol table
                        if i['isFound'] == False:        # as it is a label its 'isFound' must be false and then make it true else error
                            i['isFound'] = True
                            i['variableAddress'] = programCounterX  # here we get the address and save it
                            foundFlag = True           # make the foundFlag true
                        else:
                            ErrorFlag = True           # error if isfound is already true because its address can't be redecclareed again
                            ErrorList.append('Label Cannot Be declared Again in Line: ' + str(programCounterX))
                if foundFlag==False:
                    # if the foundflag is false then add the new symbol in the table
                    symbol_Table.append({'name': label_name, 'isUsed': False, 'isFound': True, 'variableAddress': programCounterX})
                if line[1] == 'STP':
                    STP_found = 1      # shows that STP is present in file else it would be an error
            elif val == 2:
                # it is a symbol and check if its already in the symTable else add it
                for i in symbol_Table:
                    if line[1] == i['name']:
                        flag = False
                if flag:
                    symbol_Table.append({'name': line[1], 'isUsed': True, 'isFound': False, 'variableAddress': -1})   # symbol added to the symbolTable
            

        elif len(line) == 3:
            '''Check two if's either it has ':' or it has DW in line(1) either way program counter will add to symbol'''
            # print(line)
            if line[0][-1] == ':':
                # print("hello We are here :P found a label")
                label_name = line[0][:len(line[0])-1]        # check for label
                # print(label_name)
                for i in symbol_Table:
                    if i['name'] == label_name:           # check if already in symTable
                        if i['isFound'] == False:         # isFound must be false else error
                            i['isFound'] = True
                            i['variableAddress'] = programCounterX
                            foundFlag = True
                        else:
                            ErrorFlag = True             # error because symbol can't be redeclared
                            ErrorList.append('Label Cannot Be declared Again in Line: ' + str(programCounterX))
                if foundFlag == False:         # if not found, add in the symbol table
                    symbol_Table.append({'name': label_name, 'isUsed': False, 'isFound': True, 'variableAddress': programCounterX})
                if line[1]=='STP':
                    STP_found=1
            elif line[1] == 'DW':
                '''DW statement is used to assign the variableAddress to symbol and instruction len will be 3'''
                label_name = line[0]
                # print(label_name)
                for i in symbol_Table:
                    if i['name'] == label_name:
                        if i['isFound'] == False:
                            i['isFound'] = True
                            i['variableAddress'] = programCounterX
                        else:
                            ErrorFlag = True
                            ErrorList.append('Label Cannot Be declared Again in Line: ' + str(programCounterX))
                    # else:
                    #     print('error - undefined label')

        elif len(line) == 1:
            '''check Stp command, if not found will give error'''
            # print(line[0])
            if line[0] == 'CLA':
                pass
            elif line[0] == 'STP':
                STP_found = 1
            else:
                ErrorFlag = True
                ErrorList.append("Invalid Command in Line:" + str(programCounterX))
                # print("Er)

        # print(symbol_Table)
        programCounterX += 1

    return STP_found


def RepresentsInt(s):

    try:
        int(s)
        return True
    except ValueError:
        return False

programCounterP2 = 0
ErrorFlagPass2 = False
ErrorListPass2 = []

finalOutput = []            # list to display the final output


def checkSTP_CLA(line, lineY):
        if line[0] == 'CLA':        # check CLA
            lineY += convertbin(str(bin(programCounterP2)[2:]),1) + " "    # convert programCounter to binary and add to the line
            lineY += convertbin(str(bin(opCode_Table['CLA'])[2:]),2)       # convert opCode_Table 'CLA' into binary as machine code conatins the oppcode
            return False, lineY
        elif line[0] == 'STP':
            lineY += convertbin(str(bin(programCounterP2)[2:]),1) + " "  # convert programCounter to binary and add to the line
            lineY += convertbin(str(bin(opCode_Table['STP'])[2:]),2)    # convert opCode_Table 'CLA' into binary as machine code conatins the oppcode
            return False, lineY
        return True, lineY

def convertbin(line,value):
    if value == 1:        # convert the binary value to 12 bit
        alen = len(line)
        b = ''
        c = 12 - alen
        for i in range(c):
            b += str(0)
        b += line
        line = b
        return line
    elif value == 2 :      # convert binary value to 4 bit
        alen = len(line)
        b = ''
        c = 4 - alen
        for i in range(c):
            b += str(0)
        b += line
        line = b
        return line

def checkTwo(line, lineX):
        if line[0] == 'CLA' or line[0] == 'STP':    # check whether CLA and STP are present else error
            lineX = ''
            ErrorFlagPass2 = True
            ErrorListPass2.append("Inavalid opCode with extra Argument at: " + convertbin(str(bin(programCounterP2)[2:])),1)
        else:
            if line[0][-1] == ':':
                # print("checking this")
                boolX, lineX = checkSTP_CLA(line[1:], lineX)
                # print(lineX)
                if boolX:
                    # lineX = ''
                    ErrorFlagPass2 = True
                    ErrorListPass2.append("Invalid Opcode or Extra Arguements at:" + convertbin(str(bin(programCounterP2)[2:])),1)
            else:
                
                try:
                    lineX += convertbin(str(bin(programCounterP2)[2:]), 1) + " "     # convert pc2 to binary
                    lineX += convertbin(str(bin(opCode_Table[line[0]])[2:]), 2) + " "   # convet oppcode to binary
                    if RepresentsInt(line[1]):
                        lineX += convertbin(str(bin(int(line[1]))[2:]), 1)
                    else:   
                        for symbol in symbol_Table:
                            if symbol['name'] == line[1]:         # check for the symbol and if true
                                lineX += convertbin(str(bin(symbol['variableAddress'])[2:]),1)  # add the binary of variableAdd to lineX
                                foundSymbol = True
                        if foundSymbol == False:
                            lineX = ''
                            ErrorFlagPass2 = True           # else error as symbol couldn't be found
                            ErrorListPass2.append("Could not Find Symbol in the Table:" + line[1])
                except KeyError:
                    lineX = ''
                    ErrorFlagPass2 = True
                    ErrorListPass2.append("Invalid Opcode at: " + convertbin(str(bin(programCounterP2)[2:])),1)

        return lineX


def passTwo():
    global programCounterP2
    for line in lines:
        lineX = ''
        foundSymbol = False
        if len(line) == 1:       # for len = 1 checkX - if true - error
            boolX, lineX = checkSTP_CLA(line, lineX)
            if boolX:
                ErrorFlagPass2 = True
                ErrorListPass2.append("Invalid OpCode in at: " + convertbin(str(bin(programCounterP2))[2:]),1)
        elif len(line) == 2:
            lineX = checkTwo(line, lineX)

        elif len(line) == 3:
            if line[0][-1] == ':':
                print("here")
                lineX = checkTwo(line[1:], lineX)
            elif line[1] == 'DW':
                lineX = ''
            else:
                ErrorFlagPass2 = True
                ErrorListPass2.append("Invalid Opcode or Extra Arguements at:" + convertbin(str(bin(programCounterP2))[2:]),1)
        finalOutput.append(lineX)
        programCounterP2 += 1
        # lineX = ''


