m=int(input("enter number"))
sum=0
for i in range(1,m):
    if(m%i==0):
        sum=sum+i
if (sum==m):
    print("this is a perfect number")
else:
    print("this is not a perfect number")
    
