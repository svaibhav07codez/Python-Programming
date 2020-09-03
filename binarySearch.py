n=int(input("Enter the number of inputs :"))
a=[]
print("Enter distinct numbers in ascending order")
for i in range(n):
	m=int(input())
	a.append(m)

h=int(input("Enter the element to be searched :"))

b,l=0,n-1
m=int(n//2)
while(b<=l):
	if(a[m]==h):
		print(h,"is found at",m+1,"position")

		break
	elif(h<a[m]):
		l=m-1
	else:
		b=m+1
	m=int((b+l)/2)
else:
	print("Element not found!!!")
