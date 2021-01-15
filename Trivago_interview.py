# Write the program to accept 1 input and print this number pattern
# input=4
# 1
# 4 7
# 0 3 6
# 9 2 5 8

# input=3
# 1
# 4 7
# 0 3 6

# input=6
# 1
# 4 7
# 0 3 6
# 9 2 5 8
# 1 4 7 0 3
# 6 9 2 5 8 1

def triple(n):
    counter = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(counter, end= ' ')
            counter = (counter + 3) % 10
        print()

# triple(3)

def triple2(n):
    counter = 0
    result = [1, 4, 7, 0, 3, 6, 9, 2, 5, 8]
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(result[counter], end= ' ')
            counter = (counter + 1) % 10
        print()

triple2(15)

def print3x3():
    for i in range(1, 10):
        if i % 3 == 0:
            print(i)
        else:
            print(str(i) + ' ', end='')

# print3x3()

def printSquare(n):
    for i in range(n):
        for j in range(n):
            print(n * i + j + 1, end=' ')
        print()

# printSquare(4)

def printLadder(n):
    counter = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # prevCount = i * (i - 1) / 2
            # print(int(prevCount + j), end=' ')
            print(counter, end=' ')
            counter = counter + 1
        print()

# printLadder(6)

def printLadder2(n):
    counter = 1
    for i in range(1, n + 1):
        for j in range(1, i + 2):
            print(counter, end=' ')
            counter = counter + 1
        print()

# printLadder2(3)

def printLadder3(n):
    counter = 1
    desc = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1 - desc):
            print(counter, end=' ')
            counter = counter + 1
        desc = desc + 1
        print()

# printLadder3(6)

def printLadder4(n):
    counter = 1
    for i in range(1, n + 1):
        for j in range(1, n + 2 - i):
            print(counter, end=' ')
            counter = counter + 1
        print()

# printLadder4(5)

# 1
# 1 2
# 3 5 8
# 13 21 34 55
# ...

def val(n):
    return 2 + (n * 2)

def val_ladder(n):
    counter = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(val(counter), end=' ')
            counter = counter + 1
        print()

# val_ladder(6)

def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def fibo_ladder(n):
    counter = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(fibo(counter), end=' ')
            counter = counter + 1
        print()

def fibo_ladder2(n):
    result = []
    for i in range(int((n + 1) * n / 2)):
        result.append(fibo(i))
    print(result)
    counter = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(result[counter], end=' ')
            counter = counter + 1
        print()

# fibo_ladder(6)
# fibo_ladder2(6)


def double_ladder(n):
    counter = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(2**(counter), end=' ')
            counter = counter + 1
        print()

# double_ladder(5)