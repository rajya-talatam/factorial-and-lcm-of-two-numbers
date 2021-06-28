#Factorial of number
import math
def fact(num):
    if num==1:
        return 1
    else:
        return (num * (math.factorial(num - 1)))
num=int(input("inter the value:"))
a=fact(num)
print("The factorial of {b} is {c}".format(b=num,c=a))

#LCM for two numbers

def lcm(a,b): #function
    if a>b:  #checking
        greater=a
    else:
        greater=b
    while(True):#while the condition is true then it excicuit
        if greater%a==0 and greater%b==0:
            lcm = greater
            break
        greater *= 2
    return lcm
Val=lcm(a=int(input("a:")),
b=int(input("b:")))
print("Lcm of two numbers is:",Val)
