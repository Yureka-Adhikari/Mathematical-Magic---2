from math import sqrt

def check_prime(n):
    
    if n > 1:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
        
num = int(input("Enter a number: "))
check_prime(num)