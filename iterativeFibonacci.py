def iterativeFibonacci(nthNumber):
    a, b = 0, 1
    for i in range(1, nthNumber + 1):
        if(i == 1):
            print(f"{i}st term is {a}")
        elif(i == 2):
            print(f"{i}nd term is {b}")
        else:
            a, b = b, a+b
            if(i == 3):
                print(f"{i}rd term is {b}")
            else:
                print(f"{i}th term is {b}")


iterativeFibonacci(10)