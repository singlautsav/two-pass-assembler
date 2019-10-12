fileName = input("Input file address")
try:
    file = open(fileName,'r')
except NameError:
    print("No File Found, Kindly Retry")
text = file.read()
text = text.split('\n')
lines = []
symbol_Table=[]
print(text)
def passOne(text):
    
    STP_found = False
    symbolX = {'name': '', 'isUsed': False, 'isFound': False, 'variableAddress': 0}
    for i in text:
        if i == '':
            text.remove(i)
    programCounter = 0
    for line in text:
        flag = True
        line = line.split(' ')
        for i in line:
            if i == '':
                line.remove(i)
        lines.append(line)
        print(line)
        if len(line) == 2:
            # pass
            '''Check for line[1] in the list if its a variable add to symbol table'''
            for i in symbol_Table:
                print(str(i))
                if line[1] == i['name']:
                    # print("Flag changed")
                    flag = False
                # print('flag: '+ str(flag))
            if flag:
                symbol_Table.append({'name': line[1], 'isUsed': True, 'isFound': False, 'variableAddress': 0})


        elif len(line) == 3:
            '''Check two if's either it has ':' or it has DW in line(1) either way program counter will add to symbol'''
            if line[0][-1] == ':':
                # its a label
                print("hello We are here :P found a label")
                label = {}
                label_name = line[0][:len(line[0])-1]
                print(label_name)
                for i in symbol_Table:
                    if i['name'] == label_name:
                        label = i
                        if i['isFound'] == False:
                            i['isFound'] = True
                            i['variableAddress'] = programCounter
                        else:
                            print('error - label already found')
                    

            # isfound
            elif line[1] == 'DW':
                # label = {}
                label_name = line[1]
                for i in symbol_Table:
                    if i['name'] == label_name:
                        if i['isFound'] == False:
                            i['isFound'] = True
                            i['variableAddress'] = line[2]
                        else:
                            print('error - label already found')
                    else:
                        print('error - undefined label')

            # isFound = True
            # variableAddress = programCounter

        elif len(line) == 1:
            '''check Stp command'''
            if line[0] != 'CLA' or line[0] != 'STP':
                print('error - not the instruction command')
            elif line[0] == 'STP':
                STP_found = 1

        '''DOUBT - how to know we are at end of file'''
        '''also include STP not found error'''
        #     if the program reaches at end and don't got 'STP' then error
        if STP_found != 1:
            print('STP not found in program')


        #now iteration on the symbol table

        programCounter += 1



def passTwo():
    pass



passOne(text)

variableAddress_counter = 0
for i in symbol_Table:
    if i['isFound'] == False or i['isUsed'] == False:
        print('error - they must be true')
    elif i['variableAddress'] == 0:
        if variableAddress_counter == 0:
            variableAddress_counter += 1
            i[3] = programCounter
        elif variableAddress_counter >= 1:
            print('error - more than one symbol with variableAddress missing')


print(symbol_Table)



