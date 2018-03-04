#Tom Geraghty, 04/03/2018
#Exercise 5

#Using the example given to slpitstrings to return data
#with help from the forum

with open("data/iris.csv") as f: #opens and closes the data file iris once query runs
    for line in f: # allows to go through each line of the file
        print(line.split(',')[:]) #heres where i got help, this prints nicley to the screen using the :