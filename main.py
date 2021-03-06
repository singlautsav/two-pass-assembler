from passes import *

fileName = input("Input file address")        # get the input from filename
try:
    file = open(fileName, 'r')
except NameError:
    print("No File Found, Kindly Retry")
text = file.read()                              # read from the file
text = text.split('\n')                         # split them


if passOne(text) == 0:
    ErrorFlag = True                            # if there is an error in pass one pass then there is an error
    ErrorList.append("Stop Command not found")  # error successfully added to the error list
else:
    variableAddress_counter = 0
    for i in symbol_Table:
        if i['isFound'] == False:               # if isFound is false then there is an error
            ErrorFlag = True                    # make error flag True
            ErrorList.append('error- Symbol Address not Defined: '+ i['name']) # successfully added to error list
        elif i['isUsed'] == False:              # if isUsed is false then there is an error
            ErrorFlag = True
            ErrorList.append('error- Symbol Defined But Not Used: '+ i['name'])  # successfully added to error list
        elif i['variableAddress'] == -1:        # if variableAddress is positive then there is an error  - more than one symbol missing with variableAddress missing
            if variableAddress_counter == 0:
                variableAddress_counter += 1
            elif variableAddress_counter >= 1:
                ErrorFlag = True
                ErrorList.append('error - more than one symbol with variableAddress missing')      # successfully added to error list

        if i['variableAddress']>=256:
            ErrorFlag = True
            ErrorList.append("Address more than 256 bits")         # successfully added to error list


f_symboltable = open('Symboltable.txt', 'w')
print(symbol_Table)                             # print symbol table and write them in file
for i in symbol_Table:
    f_symboltable.write(i['name'] + " " + str(i['variableAddress']) + '\n') # append the symbol in table
f_symboltable.close()
f_output = open("Output.txt", 'w')          # open the file in write mode
f_error = open('Errorfile.txt', 'w')        # open the file in write mode
if ErrorFlag: 
    for err in ErrorList:                       # here we are printing all the error and write and close the file
        print(err)
        f_error.write(err + '\n')            # write in the error file
    
else:
    passTwo()                           # call pass2
    if len(ErrorListPass2)>0:
        for err in ErrorListPass2:
            print(err)
            f_error.write(err +'\n')         # write in the error file
    else:
        for i in finalOutput:                       # else print the final output
            if i != "":
                print(i)
                f_output.write(i+'\n')         # write in the output file
f_error.close()                                  # close the file
f_output.close()                                 # close the file
