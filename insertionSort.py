def inssort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    print("Sorted list is:\n")
    print(arr)

n=int(input("Enter the no. of elements in the list: "))
A=[]
for i in range(0,n):
 x=int(input("Enter a number: "))
 A.append(x)

inssort(A)
