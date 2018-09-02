#function to find the longest word in a string.
def longestWord(sentence):
    
    arr = []

    #trying to get rid of special characters
    for i in sentence:
        for j in i:
            if j not in "`~!@#$%^&*()_+-=[]\{}\\;':\",./<>?":
                arr.append(j)

    sen = ''.join(arr)
    
    makingListOfWords = sen.split()
    
    findLargestWord = max(makingListOfWords, key=len)
        
    return findLargestWord




print(longestWord(input('Enter Longest String : ')))
