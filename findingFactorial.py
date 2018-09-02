#finding the factorial of a given number

def findingFactorial(num):
    
    for i in range(1,num):
        num = num*i

    return num

number = int(input("Enter an Integer: "))
factorial = findingFactorial(number)
print("Factorial of a number is:",factorial)

