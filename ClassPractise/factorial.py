# fact(7) == 7*6*5*4*2*1
# fact(n) = n * n-1 * n-2 * n-3 * n-4 * n-5 * n-6 * n-7
def factorial(num):
    if (num < 0):
        print("Please pass in positive integer value.")
    elif num == 0:
        return 1
    else:
        result = 1
        while (num > 0):
            result *= num
            num -= 1
        return result


print(f"Result:", factorial(10))
print("Result:", factorial(1))
print("Result:", factorial(0))
print("Result:", factorial(5))
print("Result:", factorial(7))


def get_factorial(num):
    result = 1
    if (num > 0):
        prod = 0
        while (num > 0):
            prod = num * (num-1)
            num -= 2
            if (prod != 0):
                result *= prod
        return result
    else:
        return "Pass in number greator than 0."


print("-------------------------")
print("Result:", get_factorial(10))
print("Result:", get_factorial(1))
print("Result:", get_factorial(0))
print("Result:", get_factorial(5))
