def fibon(n):
    first_number = 0
    second_number = 1
    for i in range(1, n):  #i represents each number of the sequence, while n acts like n-1 since we start at 1 and this way we avoid duplicates
        print(first_number, end=" ")  #prints the first number
        third_number = first_number + second_number  #calculates the following number and stores it in the variable third_number
        first_number = second_number  #updates these two variables for the next iteration
        second_number = third_number
    return second_number  #returns second_number which represents the last term of the sequence

print("\n5th Fibonacci term: " , fibon(5))
print("\n10th Fibonacci term: " , fibon(10))
print("\n15th Fibonacci term: " , fibon(15))
