# 3rd step

# exercise: write a progam to display even numbers 1 - 10, use range(), use counter to track number of even numbers


counter = 0                 # use a counter to hold the number of even numbers
for number in range(1, 10):  # create a sequence of numbers 1 - 10, ten not included
    if number % 2 == 0:      # if number is evenly divisible by 2, number is even
        counter += 1         # in number is even, increment counter varialble by one
        print(number)       # print even numbers if any

print(f"We have {counter} even numbers")


# 1st step: write code to test even number

is_ten_even = 10
if (is_ten_even % 2 == 0):
    print("ten is even")
# output number is even

for number in range(1, 10, 2):
    print(number)

# 2nd step: print numbers 1 - 10

# use range function, range function to create a sequence of numbers from 0 - 10
# note between 1 and 10, not including 10
# for number in range(10):
#    print(number)
# output: 0 1 2 3 4 5 6 7 8 9
