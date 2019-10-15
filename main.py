from passes import *


fileName = input("Input file address")        # get the input from filename
try:
    file = open(fileName, 'r')
except NameError:
    print("No File Found, Kindly Retry")
text = file.read()                              # read from the file
text = text.split('\n')                         # split them
# text = text.split('\t')


# print(text)                                   # print the line

if passOne(text) == 0:
    ErrorFlag = True                            # if there is an error in pass one pass then there is an error
    ErrorList.append("Stop Command not found")
else:
    variableAddress_counter = 0
    for i in symbol_Table:
        if i['isFound'] == False:               # if isFound is false then there is an error
            ErrorFlag = True
            ErrorList.append('error- Symbol Address not Defined: '+ i['name'])
        elif i['isUsed'] == False:              # if isUsed is false then there is an error
            ErrorFlag = True
            ErrorList.append('error- Symbol Defined But Not Used: '+ i['name'])
        elif i['variableAddress'] == -1:        # if variableAddress is positive then there is an error  - more than one symbol missing with variableAddress missing
            if variableAddress_counter == 0:
                variableAddress_counter += 1
                # i[3] = programCounterX
            elif variableAddress_counter >= 1:
                ErrorFlag = True
                ErrorList.append('error - more than one symbol with variableAddress missing')
f_symboltable = open('Symboltable.txt', 'w')
print(symbol_Table)                             # print symbol table and write them in file
for i in symbol_Table:
    f_symboltable.write(i['name'] + " " + str(i['variableAddress']) + '\n')
f_symboltable.close()
print(lines)
f_output = open("Output.txt", 'w')
f_error = open('Errorfile.txt', 'w')
if ErrorFlag:
    for err in ErrorList:                       # here we are printing all the error and write and close the file
        print(err)
        f_error.write(err + '\n')
else:
    passTwo()
    for i in finalOutput:                       # else print the final output
        if i != "":
            print(i)
            f_output.write(i+'\n')
f_error.close()
f_output.close()
