# Write a Python Program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum 
def sum(a,b,c):
  return(a+b+c)
def pro(k):
  return(k*k*k)

x=int(input())
y=int(input())
z=int(input())
if(x==y==z):
  print(pro(x))
else:
  print(sum(x,y,z))