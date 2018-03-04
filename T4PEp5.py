#Tom Geraghty 03/03/2018
#To solve problem number 5 of Project Euler
# I may need to souce material from google as I have only seen range in the listloop demonstartion so far.abs

#Q: 2,520 is the smallest number that can be divided by each of the numbers from 
# 1 to 10 without any remainder. Write a Python program using for and range to 
# calculate the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20. 




#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def find_smallest_number():
    import time # just for benchmarking
    i = 2 # all numbers are divisible by 1, so we start with the next integer

    list_of_int = range(2,21) # we want the number to be divisible by each of 2-20
    smallest_number = 2 #232792560 for 1-20; 2520 for 1-10; the loop can be made faster by declaring it as 2520

    found_smallest_number = False

    start_time=time.time()
 
    while found_smallest_number==False:
    
        while i < list_of_int[-1]:
            if (smallest_number) % i == 0:
                found_smallest_number=True
                i+=1
            else:
                i=2
                smallest_number+=1
                found_smallest_number=False

    print("smallest_number= ", smallest_number)
    end_time=time.time()

    print(end_time-start_time) # 122.6 - could be better with Cython

find_smallest_number()
   