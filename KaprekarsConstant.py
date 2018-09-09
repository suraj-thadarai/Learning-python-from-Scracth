#this function checks, in how many steps can we reach the kaprekars constant
#with the 4 digit number, consisting of 2 distinct digits

def KaprekarsConstant(string):

    distinct = []
    if string.isdigit():
        #making sure we have a 4 digit number
        length = len(string)
        while length != 4:
            string = "0" + string
            length = length + 1

        #this is to check whether we have 2 or more distinct digits in a
        #4 digits number
        for i in range(len(string)):
            for j in range(i):
                if string[j]!= string[i]:
                    distinct.append(string[j])

        #from here the search starts for in how many steps
        if len(distinct)>=2:
            steps = 0
            while string != "6174":
                length = len(string)
                while length != 4:
                    string = "0" + string
                    length = length + 1

                ascending = "".join(sorted(string))
                temp = list(ascending)
                temp.reverse()
                descending = "".join(temp)
                difference = int(descending) - int(ascending)
                string = str(difference)
                steps = steps + 1

            return steps

        
print(KaprekarsConstant(input("Enter a Number: ")))
