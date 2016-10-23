num = 1

while num <= 100:
    if 0 == num % 3 and 0 == num % 5:
        print("fizzbuzz")
    elif 0 == num % 3:
        print("fizz")
    elif 0 == num % 5:
        print("buzz")
    else:
        print(num)
    num = num + 1
