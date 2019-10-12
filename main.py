from passes import *


fileName = input("Input file address")
try:
    file = open(fileName,'r')
except NameError:
    print("No File Found, Kindly Retry")
text = file.read()
text = text.split('\n')
# text = text.split('\t')


print(text)

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
    for i in finalOutput:
        if i!="":
            print(i)