def fibon(n):
    first_number = 0
    second_number = 1
    for n in range(0, n+1):
        print(first_number, end=" ")
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
    return n

print("5th Fibonacci term: " , fibon(5))
print("10th Fibonacci term: " , fibon(10))
print("5th Fibonacci term: " , fibon(15))
