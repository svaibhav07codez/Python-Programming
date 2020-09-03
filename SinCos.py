import math
def sin(x,n):
   sine=0
   i=0
   for i in range(n+1):
      sign= (-1)**i
      sine=sine+ ((x**(2.0*i+1))/math.factorial(2*i+1))*sign
   return sine

def cos(x,n):
   cosine=0
   i=0
   for i in range(n+1):
      sign= (-1)**i
      cosine=cosine+ ((x**(2.0*i))/math.factorial(2*i))*sign
   return cosine

print("Sum of Sine/Cosine Series")
choice=int(input("Press 0 for Sum of Sine Series, 1 for Sum of Cosine Series."))
if(choice==0):
   x=int(input("Enter the value of x in radians: "))
   n=int(input("Enter the number of terms: "))
   print(sin(x,n))
elif(choice==1):
   x=int(input("Enter the value of x in radians: "))
   n=int(input("Enter the number of terms: "))
   print(cos(x,n))
else:
   print(" operation cannot be performed")
