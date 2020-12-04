# ------------------------------------------------- #
# Title: Assignment 07 Rev A
# Description: A example of using pickling and exception errors
# ChangeLog: (Who, When, What)
# <Y. Son>,<11.29.2020>,Create example script from internet
# <Y. Son>,<12.02.2020>,Add more exception examples
# ------------------------------------------------- #
#Code source from: https://www.journaldev.com/15638/python-pickle-example
import pickle

# Data: take user input to take the amount of data
data = []

# Process: take input of the data and dump
def dumpData():
    for i in range(int(number_of_data)):
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
    try:
        file = open('important', 'rb')
        db = pickle.load(file)
        for rows in db:
            print(rows)
        file.close()
    except Exception as e:
        print("There was a random error!")
        print(e, e.__doc__, type(e), sep='\n')

# Presentation: Show I/O
while True:
    number_of_data = input('\nEnter the number of data bet 1-3: ')
    try:
        number_of_data = int(number_of_data)
        if 0 < int(number_of_data) < 4:
            print('Number of data: ', number_of_data)
            break
        else:
            print('Please enter integer value between 1-3')
    except ValueError as e:
        print("Non numeric input!")
        print(e, e.__doc__, type(e), sep='\n')

dumpData()
print("\nBinary data imported from file: ")
loadData()
