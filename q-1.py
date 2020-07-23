#Question: Given a sorted array arr[] of N integers and a number K is given.
# The task is to check if the element K is present in the array or not.

n = int(input("Enter count for number of elements: "))
list = []
for i in range(0, n):
        #NOTE: Question mentions that array is already sorted. So Enter elements in sorted form
    eachElement = int(input())
    list.append(eachElement)
print(list)
target = int(input("Enter the element to search in array: "))
left = 0
right = (n - 1)

def searchingFn(left, right, target):
    mid = (left + right)//2
    if(list[mid] == target):
        print("Target found at index: ", mid)
    elif(list[mid] < target):
        searchingFn(mid + 1, right, target)
    elif(list[mid] > target):
        searchingFn(left, mid - 1, target)
    #return print("Target found at index: ", mid)

searchingFn (left, right, target)