arr=[1,2,3,4,5]
# agr hum poori list print krana chahte hai toh
for i in arr:
    print(i)
    
# hum isme agr koi part chahte h print krana toh slicing ka use kar skte hai 
for j in arr[::-1]:
    print(j)

for k in arr[-1:2:-1]:
    print(k)
    
    
# Check if element exists in list in Python
a=0
num=int(input("enter the number"))
for x in arr:
    if num==x:
        print(" exixst")
        a=1
        break
    
if(a==0):
    print("not exist")



# Reversing a List in Python
b=[1,2,3,4,5,6,7,8]
for x in b[::-1]:
    print(x)




import copy

a = [[1, 2], [3, 4],3,4,5]
b = a  # shallow copy

b[2]= 100

print(a)  # Output: [[100, 2], [3, 4]]  👈 a bhi change ho gaya
print(b)  # Output: [[100, 2], [3, 4]]  



# occurence of element in list 
a=[1,2,3,4,4,5,6,6,7,7,2,3,2,4,2,5,6,4]
b=[]
for x in a:
    if x not in b:
        b.append(x)
# print(b)
for y in b:
    print(a.count(y))
    