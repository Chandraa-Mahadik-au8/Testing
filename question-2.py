def reverseString(s):
    l = len(s)
    if l > 0:
        print(s[slice(l - 1, l)])
        s = slice(-1)
        reverseString(s)
        
reverseString("abcd")