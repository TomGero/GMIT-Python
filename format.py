#how to format whats printed to screen
#{} these brackest are important to be placed
#.format() is also important

for i in range(1, 11):
   #print(i)
   # print(i**2) prints the square of the number 
   # print(i**3) #prints the cubed of the number 
   # print(i**4) #prints the power of 4 of the number 
    print("{:2d} {:3d} {:4d} {:5d}".format(i, i**2, i**3, i**4)) #prints all together 
    #by adding the curly brackest and the ,format() you can begin to format the output
#by adding the :2d and :3d and :4d and :5d in the curly brackets this aligns each of the numbers
