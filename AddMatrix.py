def printmat(matrix):
 for i in range(len(matrix)):
  for j in range(len(matrix[0])):
   print(matrix[i][j], end="\t")
  print ("\n")

def addmat(a,b):
 restmat=[[0 for i in range(0,m)] for j in range(0,n)]
 for i in range(0,len(restmat)):
  for j in range(0,len(restmat[0])):
   restmat[i][j]=mat1[i][j]+mat2[i][j]
 return restmat

m=int(input("Enter the no. of rows: "))
n=int(input("Enter the no. of columns: "))

mat1=[[0 for i in range(0,m)] for j in range(0,n)]

print ("Enter elements in first matrix: ")
for i in range(0,len(mat1)):
 for j in range(0,len(mat1[0])):
  mat1[i][j]=int(input("Enter the element: "))


mat2=[[0 for i in range(0,m)] for j in range(0,n)]
print ("Enter elements in the second matrix: ")
for i in range(0,len(mat2)):
 for j in range(0,len(mat2[0])):
  mat2[i][j]=int(input("Enter the element: "))



result=addmat(mat1,mat2)
printmat(result)
