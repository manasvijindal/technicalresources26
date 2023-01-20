#Question 4
n= int(input("Enter lower number of your range= "))
m= int(input("Enter higher number of your range= "))
p=2
k=0

while n<=m:
    while n>p:
        if n%p==0:
            k=k+1
            
        p=p+1

    if k==0:
        print(n)
        
    p=2
    k=0
    
    n=n+1
