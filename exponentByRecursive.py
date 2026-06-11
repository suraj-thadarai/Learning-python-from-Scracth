def exponentByRecursive(power, number):
    #base case
    if(power == 0):
        return 1
    if(power == 1):
        return number
    
    #recursive case
    if(power % 2 == 0):
        result = exponentByRecursive(power // 2, number)
        return result * result
    
    if(power % 2 == 1):
        result = exponentByRecursive(power // 2, number)
        return result * result * number
    
exponentByRecursive(7, 3)