#example of how to spilt the information returned in openfilewith.py 

#using the instructions from openfilewith.py 
#with open("data/iris.csv") as f:
   # contents = f.read()
   # print(contents)

#you can change this as folows;
with open("data/iris.csv") as f:
    for line in f:#this allows you to print each line of the file
        print(line.split(',')[3])#by using the .split() after the line it allows you to split the contents
  #by adding the following [] brackets to after the () you can call out the line you want displayed 
  # depending on the number you enter into the [] depends on the row returned
  # the (',') in the functions tells it to use the , as the identied seperator   