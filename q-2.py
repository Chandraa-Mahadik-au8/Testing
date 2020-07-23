#Write a program which takes two integers n and m and compute (n^m) n to the power m.

n = int(input("Enter the number for base: "))
m = int(input("Enter the number for index: "))

value = 1
def powerFn(n, m, value):
    if(m == 0):
        print("The answer is {}".format(value))
    elif(m == 1):
        temp = n
        value *= temp
        print("The answer is {}".format(value))
    else:
        temp = n   
        value *= temp
        m -= 1
        powerFn(n, m, value)

powerFn(n, m, value)