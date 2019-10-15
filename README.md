# two-pass-assembler

## Working?
To run the program. 
* Clone the Repository
* Run main.py 
```
python main.py
```
* Input file Address when asked for

## File type
The program can work with the text file.

## Errors Taken Care of?

Since we were to handle the variables, following errors are handled by the program
* Symbol defined but not used
* Symbol defined more than one time
* Excessive arguments
* Lesser Number of Arguements for said Opcodes
* STOP Command Not Found Error

## Files and There Use Case

* Output.txt
On successful completion of assembly the Output.txt will have the Machine code for the said Assembly code.
* Symboltable.txt
On Successful completion of pass one the Symbol Table will be filled with label name and address
* test.txt
It is the file that contains the assembly code to be tested
* Errorfile.txt
In case of Errors during Pass-One or Pass-Two the Error file will be flooded with the error message and where ever defined the address of the file.
* passes.py
Every method that has to be used for pass-one or pass-two has been coded in that given file 

