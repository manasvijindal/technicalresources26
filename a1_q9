#Question 9
n=int(input("Enter first number= "))
m=int(input("Enter second number= "))
hcf=0
lcm=0

for i in range(1,min(n,m)):
    if n%i==0 and m%i==0:
        hcf=i
    
print("HCF=",hcf)

for j in range(max(n,m), 1+(n*m)):
    if j%n==0 and j%m==0:
        lcm=j
        break
        
print("LCM=",lcm)
