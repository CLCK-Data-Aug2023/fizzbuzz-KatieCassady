# list numbers. If divisible by 3 print fizz. If divisible by 5 print buzz. If divisible by 3 and 5 print fizzbuzz
for i in range(1,101):
    if (i % 3 == 0) and (i % 5 != 0):
        print("Fizz")
    if (i % 5 == 0) and (i % 3 != 0):
        print("Buzz")
    if (i % 5 == 0) and (i % 3 == 0):
        print("FizzBuzz")
    else:
        print(i)
