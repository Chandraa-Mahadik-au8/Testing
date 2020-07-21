
def add(n, sum, i):
  if i <= n:
    sum += i
    i += 1
    add(n, sum, i)
  return sum  

add(5, 0, 1)