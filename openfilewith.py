#Using with to open and close teh fie when finished
#also simpler lines of code to read contents
# same result as process in openfile.py 

with open("data/iris.csv") as f:
    contents = f.read()
    print(contents)