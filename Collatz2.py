#Tom Geraghty 14/02/2018
# Collatz using example

print("This is The Collatz Sequence")
user = int(input("Enter a number: "))


def collatz(n):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
        else:
            n = n * 3 + 1
            print(n)


collatz(user)