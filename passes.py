programCounterX = 0
lines = []
symbol_Table=[]
ErrorFlag = False
ErrorList = []
opCode_Table = {'CLA':0,'LAC':1,'SAC':2,'ADD':3,'SUB':4,'BRZ':5,'BRN':6,'BRP':7,'INP':8,'DSP':9,'MUL':10,'DIV':11,'STP':12, 'DW':13}

def lineCheck(line):
    if line[0][-1]==':':
        return 1
    else:
        return 2

def passOne(text):
    global programCounterX
    STP_found = 0
    # symbolX = {'name': '', 'isUsed': False, 'isFound': False, 'variableAddress': -1}
    
    for i in text:
        if i == '':
            text.remove(i)
    # programCounter = 0
    for line in text:
        
        foundFlag = False
        flag = True
        line = line.split(' ')
        for i in line:
            if i == '':
                line.remove(i)
        # print(line)
        lines.append(line)
        # print(line)
        if len(line) == 2:
            # pass
            # print("2"+ str(line))
            '''Check for line[1] in the list if its a variable add to symbol table'''
            val = lineCheck(line)
            # print(val)
            if val ==1:
                '''check label with STP and CLA'''
                label_name = line[0][:len(line[0])-1]
                # print(label_name)
                for i in symbol_Table:
                    if i['name'] == label_name:
                        if i['isFound'] == False:
                            i['isFound'] = True
                            i['variableAddress'] = programCounterX
                            foundFlag = True
                        else:
                            ErrorFlag = True
                            ErrorList.append('Label Cannot Be declared Again in Line: ' + str(programCounterX))
                if foundFlag==False:
                    symbol_Table.append({'name': label_name, 'isUsed': False, 'isFound': True, 'variableAddress': programCounterX})
                if line[1]=='STP':
                    STP_found=1
            elif val ==2:
                for i in symbol_Table:
                    if line[1] == i['name']:
                        flag = False
                if flag:
                    symbol_Table.append({'name': line[1], 'isUsed': True, 'isFound': False, 'variableAddress': -1})
            

        elif len(line) == 3:
            '''Check two if's either it has ':' or it has DW in line(1) either way program counter will add to symbol'''
            # print(line)
            if line[0][-1]==':':
                # print("hello We are here :P found a label")
                label_name = line[0][:len(line[0])-1]
                # print(label_name)
                for i in symbol_Table:
                    if i['name'] == label_name:
                        if i['isFound'] == False:
                            i['isFound'] = True
                            i['variableAddress'] = programCounterX
                            foundFlag = True
                        else:
                            ErrorFlag = True
                            ErrorList.append('Label Cannot Be declared Again in Line: ' + str(programCounterX))
                if foundFlag==False:
                    symbol_Table.append({'name': label_name, 'isUsed': False, 'isFound': True, 'variableAddress': programCounterX})
                if line[1]=='STP':
                    STP_found=1
            elif line[1] == 'DW':
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
            # is   Found = True
            # variableAddress = programCounter
        elif len(line) == 1:
            '''check Stp command'''
            # print(line[0])
            if line[0] == 'CLA':
                pass
            elif line[0] == 'STP':
                STP_found = 1
            else:
                ErrorFlag = True
                ErrorList.append("Invalid Command in Line:" + str(programCounterX))
                # print("Er)

        '''DOUBT - how to know we are at end of file'''
        '''also include STP not found error'''
        #     if the program reaches at end and don't got 'STP' then error
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

finalOutput = []

def checkSTP_CLA(line, lineY):
        if line[0]=='CLA':
            lineY += bin(programCounterP2)[2:] +" "
            lineY += bin(opCode_Table['CLA'])[2:]
            return False, lineY
        elif line[0]== 'STP':
            lineY += bin(programCounterP2)[2:] + " "
            lineY += bin(opCode_Table['STP'])[2:]
            return False, lineY
        return True, lineY
    
def checkTwo(line, lineX):
        if line[0]=='CLA' or line[0]=='STP':
            lineX = ''
            ErrorFlagPass2 = True
            ErrorListPass2.append("Inavalid opCode with extra Argument at: " + bin(programCounterP2)[2:])
        else:
            if line[0][-1]==':':
                # print("checking this")
                boolX, lineX = checkSTP_CLA(line[1:],lineX)
                # print(lineX)
                if boolX:
                    # lineX = ''
                    ErrorFlagPass2 = True
                    ErrorListPass2.append("Invalid Opcode or Extra Arguements at:" + bin(programCounterP2)[2:])
            else:
                
                try:
                    lineX += bin(programCounterP2)[2:]+" "
                    lineX += bin(opCode_Table[line[0]])[2:] +" "
                    if RepresentsInt(line[1]):
                        lineX +=bin(int(line[1]))[2:]
                    else:   
                        for symbol in symbol_Table:
                            if symbol['name']==line[1]:
                                lineX += bin(symbol['variableAddress'])[2:]
                                foundSymbol = True
                        if foundSymbol==False:
                            lineX = ''
                            ErrorFlagPass2 = True
                            ErrorListPass2.append("Could not Find Symbol in the Table:" + line[1])
                except KeyError:
                    lineX = ''
                    ErrorFlagPass2 = True
                    ErrorListPass2.append("Invalid Opcode at: " + bin(programCounterP2)[2:])

        return lineX


def passTwo():
    global programCounterP2
    for line in lines:
        lineX = ''
        foundSymbol = False
        if len(line)==1:
            boolX, lineX = checkSTP_CLA(line,lineX)
            if boolX:
                ErrorFlagPass2 = True
                ErrorListPass2.append("Invalid OpCode in at: "+ bin(programCounterP2))[2:]
        elif len(line)==2:
            lineX = checkTwo(line,lineX)

        elif len(line)==3:
            if line[0][-1]==':':
                print("here")
                lineX = checkTwo(line[1:],lineX)
            elif line[1]=='DW':
                lineX = ''
            else:
                ErrorFlagPass2 = True
                ErrorListPass2.append("Invalid Opcode or Extra Arguements at:" + bin(programCounterP2))[2:]
        finalOutput.append(lineX)
        programCounterP2+=1
        # lineX = ''


