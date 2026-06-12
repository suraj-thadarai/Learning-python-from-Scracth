"""
Write the recursive form of sumSeries(). This function should use recur-
sive function calls instead of a loop.

"""

def sumSeriesRecursive(number):
    
    # base case
    if(number <= 0):
        return 0
    
    #recursive case
    else:
        return number + sumSeriesRecursive(number-1)
    
print(sumSeriesRecursive(5))