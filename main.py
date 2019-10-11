fileName = input("Input file address")
try:
    file = open(fileName,'r')
except NameError:
    print("No File Found, Kindly Retry")
text = file.read()
text = text.split('\n')

def assembly(text):
    for i in text:
        if i=='':
            text.remove(i)
    
    for line in text:
        line = text.split(' ')
        for i in line:
            if i=='':
                line.remove(i)
        if len(line)==2:
            pass
            '''Check for second element in the list if its a variable add to symbol table
                isUsed = true:
            '''
        elif len(line)==3:
            '''Check two if's either it has : or it has DW in line(1) either way program counter will add to symbol
                isFound = true:    
            '''
        elif len(line)==1:
            '''check Stp command'''
        





