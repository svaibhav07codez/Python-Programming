def matsq(mat):
 for i in range(len(mat)):
  for j in range(len(mat)):
   mat[i][j]=mat[i][j]**2

def printmat(mat):
 for i in range(len(mat)):
  for j in range(len(mat)):
   print "\t",mat[i][j]
   print "\n"


m=int(input("Enter the no.of rows in the first matrix: "))
n=int(input("Enter the no. of columns in the first matrix: "))

a=[[0 for i in range(0,m)] for j in range(0,n)]
print "Enter elements in the second matrix: "
for i in range(0,m):
 for j in range(0,n):
  a[i][j]=int(input("Enter the element: "))
matsq(a)
printmat(a)
