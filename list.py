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
# a=[1,3,5,6,8,7,6,5,4,9,7,76,5,67,54,98,78]
# a.sort()
# l=len(a)-1
# for i in range(l,-1,-1):
#     if a[l]!=a[l-1]:
#         break
# print(a[l-1])

# print even numbers in a list
# a=[1,2,3,4,2,1,2,3,4,3,2,1,12,3,2,3]
# b=[]
# for x in a:
#     if x%2==0:
#         b.append(x)
# print(b)



# print odd numbers in a List
# to count Even and Odd numbers in a List
# to print positive numbers in a list
# to print negative numbers in a list
# to count positive and negative numbers in a list



# Remove multiple elements from a list
# a=[1,1,2,3,6,4,3,2,2,6,7,8,9]
# b=[]
# for x in a:
#     if a.count(x)<2:
#         b.append(x)
# print(b)

# Remove empty tuples from a list
# a=[1,2,3,(),5,4,2,3,8,()]
# for x in a:
#     if type(x)==tuple:
#         a.remove(x)
# print(a)
# Program to print duplicates from a list of integers
# Remove first element from list
# To remove duplicates from list
# Get unique values from a list
# Merge Two lists
# Iterate over a list
# Find average of a list
# Perform append at beginning of list
# To find second largest number in a list
# # Intersection Of two lists
# Select random value from a list
# Check if two lists are identical
# Get the last element of list
# Remove None values from list
# Print all common elements of two lists
# Maximum and minimum element's position in a list



# Union of two or more lists
# a=[1,2,3,4,5]
# b=[3,4,5,6,7,8]
# c=[]
# for x in a:
#     c.append(x)
# for y in b:
#     if y not in c:
#         c.append(y)
# print(c)


# a=[
#     [1,2,3],
#     [3,4,5],
#     [4,5,6],
#     [5,6,7]
# ]
# row=len(a)
# col=len(a[0])
# d=[][]
# for i in a:
    
#     for j in range(col):
#         d[i][j]=a[i][j]


# a = [
#   [1, 2, 3],
#   [3, 4, 5],
#   [4, 5, 6],
#   [6, 7, 8]
# ]

# rows = len(a)
# cols = len(a[0])

# transpose = []

# for j in range(cols):
    
#     for i in range(rows):
#         # new_row.append(a[i][j])
#         transpose.append(a[i][j])
#         end=""

# for row in transpose:
#     print(row)






    