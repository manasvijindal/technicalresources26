#Question 3
t=int(input("How many times would you like to test the numbers= "))
p=2
k=0

while t>0:
    n=int(input("Enter a number= "))
    while n>p:
        if n%p==0:
            k=k+1
        
        p=p+1
    p=2
    if k>0:
        print("Not Prime")
    
    else:
        print("Prime")
        
    t=t-1
