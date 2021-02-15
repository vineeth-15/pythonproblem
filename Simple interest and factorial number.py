"""p = int(input("Enter priciple amount: ")) 
n =  int(input("Enter number of year: "))
r = float(input("Enter rate of interest: "))
SI = (p*n*r)/100
print("Simple Interest is: ",SI)
"""

n = int(input("Enter a number: "))
fact = 1
while(n>0):
    fact = fact*n
    n-=1
print(fact)
