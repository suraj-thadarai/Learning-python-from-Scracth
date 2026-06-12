"""
Iteratively calculate the sum of the integer series from 1 to n. This is sim-
ilar to the factorial() function, except it performs addition instead of
multiplication. For example, sumSeries(1) returns 1, sumSeries(2) returns
3 (that is, 1 + 2), sumSeries(3) returns 6 (that is, 1 + 2 + 3), and so on.
This function should use a loop instead of recursion.

"""

def sumSeries(term):
    # edge case when term is 0
    if(term == 0):
        return 0

    result = 0
    for i in range(1, term+1):
        result += i
        
    return result

print(sumSeries(5))
        
    