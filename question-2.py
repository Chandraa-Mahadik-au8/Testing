def subStringFn (s):
    def singleChar(i):
        i = 0
        if i < len(s):
            print(s[i])
            i += 1
            singleChar(i)
subStringFn('abc')

#Need to work on this code.