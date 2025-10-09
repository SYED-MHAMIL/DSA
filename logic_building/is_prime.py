#Given a positive integer, check if the number is prime or not. A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Examples of the first few prime numbers are {2, 3, 5, ...}



def isPrime(n):
    if n<=1:
       return False
    if n==2:
        return True
    for  i in range(2,n):
        if n%i == 0:
            return False
    return True

print(isPrime(2))