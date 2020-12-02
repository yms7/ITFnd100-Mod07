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
    number_of_data = input('\nEnter the number of data bet 1-3: ')
    try:
        number_of_data = int(number_of_data)
        break
    except ValueError as e:
        print("Non numeric input!")
        print(e, e.__doc__, type(e), sep='\n')
        continue
    break
'''
    except ArithmeticError as e:
        print("Please enter integer value: ")
        print(e, e.__doc__, type(e), sep='\n')
        continue
'''

dumpData()
print("\nBinary data imported from file: ")
loadData()
