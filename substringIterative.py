def substringIterative(needle, haystack):
    i = 0
    while i < len(haystack):
        if (haystack[i: i+len(needle)] == needle):
            return i # needle found
        i = i + 1
        
    return -1 #needle not found


substringIterative('cat', 'My cat Zophie')