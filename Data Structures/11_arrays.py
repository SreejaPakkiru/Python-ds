# def prints():
#     print("Hi")
#     return 1
# a=prints()
# print(a)# prints none if return 1 is not there

# def evenOdd(x):
#     if(x%2==0):
#         print("Even")
#     else:
#         print("odd")
# n=int(input("enter n: "))
# evenOdd(n)# n=4 Even
# print(evenOdd(4)) #Prints Even None(prints inside 1st and then since no return none)


#Pass by value and pass by reference
#Mutable objects: Changes inside the function affect the original object.(like lists, dictionaries)
#Immutable objects: The original value remains unchanged. (like integers, strings, tuples).
# # Function modifies the first element of list
# def myFun(x):
#     x[0] = 20

# lst = [10, 11, 12, 13]
# myFun(lst)
# print(lst)   # list is modified

# # Function tries to modify an integer
# def myFun2(x):
#     x = 20
#     return x

# a = 10
# myFun2(a)
# print(myFun2(a))#a=20
# print(a)     #a=10  integer is not modified

#recursive function
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(3))

#Creating a list
# l=[1,2,3]
# for i in l:
#     print(i,end=" ")
# print("\n")
# print(l[0])
# print(l[1])
# print(l[2])
# ---9/10 done---
#using list keyword
# l=list((1,3,"sree",'a')) #list(tuple,list or)
# print(l)
# c=[2]*2
# d=[3]+[2]
# print(c)
# print(d)
# e=[4]*0
# print(e)#prints[]

#accessing list elements

# l=[1,2,3]
# print(l[-1])
# print(l[:])
# print(l[::-1])

#list operations
# l=[]
# l.append(1)
# l.insert(9,2)# Tries to insert 2 at index 9 Since index 9 is beyond the current length (which is 1),
# # Python will insert it at the end
# # Now l = [1, 2]
# l.extend([3,4,5])
# print(l)#[1,2,3,4,5]
# l.insert(4,6)
# l.extend("s")#int is not iterable so l.extend(2):error
# l.append([1,2,'s'])
# print(l)
# l.clear()
# print(l)
# l.append(3)
# l.remove(3)
# print(l)
# l.append(3)
# l.pop(3)#pop(index)
# print(l)
# l.pop()
# del l[2]
# print(l)
# m=[[1,2],[2,3],[4,5]]
# print(m)
# print(m[2][1])

#list comprehension
# m=[1,3,4]
# l=[i*2 for i in range(5)]
# #l=[i*2 for i in range(m)]#TypeError: 'list' object cannot be interpreted as an integer
# print(l)
# 
# def decrementList(arr):
#     # for i in arr:
#     #     return i-1
#     s=[i-1 for i in arr]
#     return s
# l=[1,2,3]
# for i in range(len(l)):
#     print(l[i])

#linear search
def LinearSearch(target,l):
    for i in range(len(l)):
        if(l[i]==target):
            return i
    return -1
l=[1,2,3]
a=LinearSearch(2,l)
print(a)