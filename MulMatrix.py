def printmat(matrix):
 for i in range(len(matrix)):
  for j in range(len(matrix[0])):
   print(matrix[i][j], end="\t")
  print ("\n")


m=int(input("Enter the no.of rows in the first matrix: "))
n=int(input("Enter the no. of columns in the first matrix: "))

X=[[0 for i in range(0,m)] for j in range(0,n)]

print ("Enter elements in first matrix: ")
for i in range(0,len(X)):
 for j in range(0,len(X[0])):
  X[i][j]=int(input("Enter the element: "))

nn = int(input("Enter the no.of columns in the second matrix: "))

Y=[[0 for i in range(0,n)] for j in range(0,nn)]
print ("Enter elements in the second matrix: ")
for i in range(0,len(Y)):
 for j in range(0,len(Y[0])):
  Y[i][j]=int(input("Enter the element: "))

result=[[0 for i in range(0,m)] for j in range(0,nn)]
for i in range(0,len(X)):
   for j in range(0,len(Y[0])):
       for k in range(0,len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
printmat(result)
