#sum of na natural numbers using while loop
N= int(input("enter number"))

i= N
sum=0
while(i>=1):
    sum +=i
    i=i-1
print("sum of "+str(N) +" natural numbers is " + str(sum))