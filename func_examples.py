#1 greatest no using function
'''
def greatest(a,b,c):
    if (a>b and a>c):
        print(a,"is greater")
    elif (b>a and b>c):
        print(b,"is greater")
    else :
        print(c,"is greater")
x=int(input("Enter a no "))
y=int(input("Enter a no "))
z=int(input("Enter a no "))
greatest(x,y,z)
'''


#2 convertion of temp from celcius to fahrenhite
'''
def cel(c):
    f=((9/5)*c)+32
    print(f,"`F")
x=int(input("Enter temperature in Celsius: "))
cel(x)
'''


#3 Multiplication table
'''
def table(d):
    for i in range(1,11):
        e=d*i
        print(d,"x",i,"=",e)
x=int(input("Enter a no: "))
table(x)
'''


#4 Average of no using function
'''
def avg(*n):
    sum=0
    for i in n:
        sum=sum+i
    print("Average of numbers is: ",sum/len(n))
avg(5,4,7)
'''


