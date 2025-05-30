# arr=[1,2,3,4,5]
# # agr hum poori list print krana chahte hai toh
# for i in arr:
#     print(i)
    
# # hum isme agr koi part chahte h print krana toh slicing ka use kar skte hai 
# for j in arr[::-1]:
#     print(j)

# for k in arr[-1:2:-1]:
#     print(k)
    
    
# # Check if element exists in list in Python
# a=0
# num=int(input("enter the number"))
# for x in arr:
#     if num==x:
#         print(" exixst")
#         a=1
#         break
    
# if(a==0):
#     print("not exist")



# # Reversing a List in Python
# b=[1,2,3,4,5,6,7,8]
# for x in b[::-1]:
#     print(x)




# import copy

# a = [[1, 2], [3, 4],3,4,5]
# b = a  # shallow copy

# b[2]= 100

# print(a)  # Output: [[100, 2], [3, 4]]  👈 a bhi change ho gaya
# print(b)  # Output: [[100, 2], [3, 4]]  



# # occurence of element in list 
# a=[1,2,3,4,4,5,6,6,7,7,2,3,2,4,2,5,6,4]
# b=[]
# for x in a:
#     if x not in b:
#         b.append(x)
# # print(b)
# for y in b:
#     print(a.count(y))
    
# # Sum of number digits in List in Python
# a=[12,4445,56,78,988,23,45]
# for x in a:
#     sum=0
#     while x!=0:
#         r=x%10
#         sum=sum+r
#         x=x//10
#     print(sum)

# find smallest number in a list

# a=[2,3,4,2,6,8,4,2,3,5,67]
# min=float('inf')
# for i in range(len(a)):
#     if a[i]<min:
#         min=a[i]
# print(min)



# find largest number in a list
# a=[1,6,8,9,5,78,65,32,98,2,4,6,8]
# max=float('-inf')
# for x in range(len(a)):
#     if a[x]>max:
#         max=a[x]
# print (max)
    
    
# find second largest number in a list
a=[1,3,5,6,8,7,6,5,4,9,7,76,5,67,54,98,78]
a.sort()
l=len(a)-1
for i in range(l,-1,-1):
    if a[l]!=a[l-1]:
        break
print(a[l-1])