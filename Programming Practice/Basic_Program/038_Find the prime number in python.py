num = 10

if num == 1:
    print("it is not a prime number")

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("not prime")
            break
    else:
        print("Prime number")
