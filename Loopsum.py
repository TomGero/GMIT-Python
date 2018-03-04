#Tomas Geraghty 03/03/2018
# Summ of total of all even numbers between 1 and 100

sum = 0
i = 0

while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print("The sum of the numbers between 1 and 100 amounts to:", sum)