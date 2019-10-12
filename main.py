fileName = input("Input file address")
try:
    file = open(fileName,'r')
except NameError:
    print("No File Found, Kindly Retry")
text = file.read()
text = text.split('\n')
# text = text.split('\t')
lines = []
symbol_Table=[]
ErrorFlag = False
ErrorList = []
programCounterX = 0
print(text)


def checkSymbolLabel(lineX,pc):
    if lineX[0][-1]==':':
        # print("hello We are here :P found a label")
        label_name = lineX[0][:len(lineX[0])-1]
        print(label_name)
        for i in symbol_Table:
            if i['name'] == label_name:
                if i['isFound'] == False:
                    i['isFound'] = True
                    i['variableAddress'] = pc
    # if lineX[1]=='STP':

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
        print(line)
        lines.append(line)
        # print(line)
        if len(line) == 2:
            # pass
            # print("2"+ str(line))
            '''Check for line[1] in the list if its a variable add to symbol table'''
            val = lineCheck(line)
            print(val)
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

def passTwo():
    pass



if passOne(text)==0:
    ErrorFlag = True
    ErrorList.append("Stop Command not found")
else:
    variableAddress_counter = 0
    for i in symbol_Table:
        if i['isFound'] == False:
            ErrorFlag = True
            ErrorList.append('error- Symbol Address not Defined: '+ i['name'])
        elif i['isUsed'] == False:
            ErrorFlag = True
            ErrorList.append('error- Symbol Defined But Not Used: '+ i['name'])
        elif i['variableAddress'] == -1:
            if variableAddress_counter == 0:
                variableAddress_counter += 1
                # i[3] = programCounterX
            elif variableAddress_counter >= 1:
                ErrorFlag = True
                ErrorList.append('error - more than one symbol with variableAddress missing')

print(symbol_Table)
print(lines)
if ErrorFlag:
    for err in ErrorList:
        print(err)
else:
    passTwo()