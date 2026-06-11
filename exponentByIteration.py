def exponentByIteration(number, power):
    result = 1
    for i in range(1, power+1):
        print(f"i is {i}")
        result *= number
        
    return result

print(exponentByIteration(3, 7))
    