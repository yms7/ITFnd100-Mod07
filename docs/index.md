# Title
**Dev:** *YSon*
**Date:** *12.01.2020*

## Assignment 07
## SAVE DATA USING BINARY FORMAT AND UTILIZE EXCEPETION FUNCTIONS
Pickle is one of the python module used to serializing and de-serializing a Python object structure.  
Structure error handling uses built-in class that contains information about a common errors. 

## Pickling and Exception error handing
Picking is the process to convert the data into binary format.  
Pickle module stores data into a binary format and pickle can obscure the file’s content and may reduce the file’s size.  
Exception is different from syntax error.  
Syntax error occurs when the program detects an incorrect statement but an Exception error happens only if certain condition occurs such as when the number is divided by zero or input value is non-numeric.  
Python’s Exception statement automatically detects and creates an Exception object when the error occurs. 

```
# ------------------------------------------------- #
# Title: Assignment 07
# Description: A example of using pickling and exception errors
# ChangeLog: (Who, When, What)
# <Y. Son>,<11.29.2020>,Create example script from internet
# ------------------------------------------------- #
#Code source from: https://www.journaldev.com/15638/python-pickle-example
import pickle

# Data: take user input to take the amount of data
data = []
# Process: take input of the data and dump
def dumpData():
    for i in range(number_of_data):
        raw = input('Enter data '+str(i)+' : ')
        data.append(raw)
    # open a file, where you want to store the data
    file = open('important', 'wb')
    # dump information to that file
    pickle.dump(data, file)
    # close the file
    file.close()
# read dumped data from the file
def loadData():
    # for reading also binary mode is important
    file = open('important', 'rb')
    db = pickle.load(file)
    for rows in db:
        print(rows)
    file.close()

# Presentation: Show I/O
while True:
    number_of_data = input('\nEnter the number of data : ')
    try:
        number_of_data = int(number_of_data)
        break
    except ValueError as e:
        print("Non numeric input!")
        print(e, e.__doc__, type(e), sep='\n')
        continue
    break

dumpData()
print("\nBinary data imported from file: ")
loadData()
```
#### Listing 7-4
![Result of Assignment 07](https://github.com/yms7/ITFnd100-Mod07/blob/main/docs/Figure%207-4.png "Result of Assignment 07") 
#### Figure 7-4. Result of Listing 7-4

## Summary
I used different examples from multiple websites to write a script that uses Pickle module and Exception error classes.  
Using Pickle module was very easy to use since there are only two commands to remember “dump” and “load”.  
However, working with binary formatted file was a quite challenging.  
Mac applications were not binary friendly at all.  
I had to find different program to open binary file since text file does not support to ready any binary information. 

Learning Exception class was interesting but at the same time it was quite of challenging work for me.  
As a programmer, I had to plan ahead and think of any possible errors that may occur during the operation of my code.  
Writing Exception code is based on the possible errors that may occur and it was difficult to visualize what type of error may occur during the usage of my program.  
I used most common Exception error on my script but once I build more experiences in coding I would be able to use multiple exception classes on my script. 
