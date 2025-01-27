#!/usr/bin/python3 

rows = int(input("Enter a number: "))

for num in range(rows+1):

    for i in range(num):
        print(num, end="")

    print()
