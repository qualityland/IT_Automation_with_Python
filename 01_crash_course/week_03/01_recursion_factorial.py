def factorial(n):
    print("factorial called with " + str(n))
    if n < 2:
        print("returning 1")
        return 1
    result = n * factorial(n-1)
    print("returning " + str(result) + " for factorial of " + str(n))
    return result

print(factorial(4))
#print(factorial(998))
#print(factorial(999))