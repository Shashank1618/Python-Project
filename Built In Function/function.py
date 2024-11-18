#strings are immutable and list are mutable

x1='rrgi'; y1='rrgi'
p=[10,20,30]; q=[10,20,30]

print(x1==y1, p==q)
print(x1 is y1, p is q)

x1=x1+y1
print(x1)
x1+=y1
print(x1)

