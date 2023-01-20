
#Question 5
n= int(input("Enter a number= "))
r=0
k=0

while n!=0:
    r=n%10
    k=k+1
    
    n=n//10
    
print(k)
