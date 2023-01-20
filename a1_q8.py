#Question 8
n=int(input("Enter a number= "))
k=int(input("How many times would you like to rotate the number= "))
r=0
p=0

while n!=0:
    r=n%10
    p=p+1
    n=n//10
    
print(p)#lenght of n

r=0
n=int(input("Enter your number again= "))

if n==0:
    print("Invalid input")
    
elif n>0:
    while k>0:
        r=n%10
        n=n//10
        n=r*10**(p-1)+n
        k=k-1
        r=0
            
print(n)
