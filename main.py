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
    




