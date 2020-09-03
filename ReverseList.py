def rev(lst):
   revlst=[]
   for i in range(1,len(lst)+1):
      revlst.append(lst[-i])
   print("Reverse list is:\n")
   print(revlst)


list=[]
n=int(input("Enter the no. of values in the list: "))
for i in range(0,n):
   list.append(raw_input("Enter the element: "))
rev(list)
