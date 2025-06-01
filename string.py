# string ke har word ko sort krarna 

s="hello ansh goel"
# print(s)
a=s.split(" ")
# print(len(a[0]))

# for x in a:
    # b=list(x)
    # for y in b:
    #     print(y,end=" ")
    #     if ord(y)>=65 and ord(y)<=92:
    #         y=y.upper()
    # print("")
n=[]
for x in a:
    b=list(x)
#     b[0]=b[0].upper()
#     q=("").join(b)
#     n.append(q)
# print(n)
    # b.sort()
    o = len(b)

    for i in range(o):
        for j in range(0, o - i - 1):
            if b[j] > b[j + 1]:
                # Swap if current char is greater than next char
                b[j], b[j + 1] = b[j + 1], b[j]

    q=("").join(b)
                # print(q)
    n.append(q)
print(n)




