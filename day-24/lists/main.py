# list me hmlog bht sara element store kr skte hai.

# difference between list and array

# array basically homogenous hai or list heterogenious hai 
# array me continous allocation of elements hote hai list me ni hote hai
# array me continous allocation ke wajah se hmlog faster access kr skte hai elements ko whi list me access slower ho jaata hai
# lists jyada programmer friendly hai bole toh flexibility jyada hai

# Work items in this function
# intialization
# accessing of elements 
# editing in the list
# deleting in the list
# functions in the list


# list ko aise initialize krte hai
list1 = []

list1= [1,2,3,4,5]
# [1, 2, 3, 4, 5]
print(list1)
list2=[1,2,3,[4,5]]
# [1, 2, 3, [4, 5]]
print(list2)
list3=[1,2,3,[4,5],[6,7]]
# [1, 2, 3, [4, 5], [6, 7]]
print(list3)
list4=[8,9]
list5=[[[1,2],[3,4]],[[5,6],[7,8]]]
# 1
# 2
# 3
# 4 5 6 7     
# Accessing the element in the list         



for x in list3:
    if isinstance(x,list):
        for element in x:
            print(element, end=" ")
    else:
        print(x)

# hm chahte hai ki list se hm 4 element jo khud bhi ek list hai uska first element access krna chahte hai
# 4
print(list3[3][0])

# we want to fetch 7 from list5. ye dekho ye 3-d array hai toh agr koi bhi element access krna hai toh ek baat toh clear hi hai ki hmlog ko 3 indices toh likhna hi pdega.
# 7
print(list5[1][1][0])




# Editing in list
# in python list is mutable mtlb you can change the list
# we want to edit list 1 first element we want ki it should be 100 instead of 1 but strings mutable hote hai

# positive indexing
list1[0]=100
# [100, 2, 3, 4, 5]
print(list1) 

# negative indexing
list1[-1]=500
# [100, 2, 3, 4, 500]
print(list1)

# slicing technique se bhi elements hm edit kr skte hai
list1[1:4]=[200,300,400]
# [100, 200, 300, 400, 500]
print(list1)



# add elements in the list
# 3 tarike se insert hote hai list me chizen
# append -> last me kisi bhi exisiting list me add krna.
# extend -> ek saath agr bht saara element insert krna hua toh and kisi bhi type ka string, bool,int , decimal
# insert -> jo apko apne desired location pe chizen add krna ho toh.


# note -> list hmesha ek item insert krne ka try krega as a whole and extend hmesha multiple itema add krne ka try krega.
# append example

list1.append(1000)
# [100, 200, 300, 400, 500, 1000]
print(list1)
# extend example

list1.extend([5000,6000,7000])
# [100, 200, 300, 400, 500, 1000, 5000, 6000, 7000]
print(list1)

# insert example
list1.insert(3,"world")
# [100, 200, 300, 'world', 400, 500, 1000, 5000, 6000, 7000]
print(list1)



# delete item in the list
# del -> element ya pura list bhi delete ho skta hai and hmlog range wise bhi chzien delte kr skte hai.
# remove -> jb apko element pata ho but index ni pata or delete krna hai toh phir ap remove ka use kr skte hai.
# pop -> ye pop apne list ke last element ko delete krta hai
# clear -> koi list ko pura tarah empty krna hai toh clear ka use kro.


# difference between del and clear in list 
# toh del python me pura list hi uda deta hai del list1 and agr ap clear use krte ho toh wo pura list ka element khali kr deta hai but list exist krta hai

del list1[0]
# [200, 300, 'world', 400, 500, 1000, 5000, 6000, 7000]
print(list1)

del list2[1:3]
# [1, [4, 5]]
print(list2)

del list3
# qki ye pura list hi uda diya and hmlog access krne ka koshish kr rhe hai
#   File "C:\Users\ADMIN\Desktop\100_days_of_python\day-24\lists\main.py", line 121, in <module>
#     print(list3)
#           ^^^^^
# NameError: name 'list3' is not defined. Did you mean: 'list1'?
# print(list3)


list1.remove('world')
# [200, 300, 400, 500, 1000, 5000, 6000, 7000]
print(list1)


list1.pop()
# [200, 300, 400, 500, 1000, 5000, 6000]
print(list1)

list2.clear()
# []
print(list2)



# functions in the list
# [200, 300, 400, 500, 1000, 5000, 6000, 8, 9]
print(list1+list4)
# 6000
print(max(list1))
# 200
print(min(list1))
# 7
print(len(list1))
# [200, 300, 400, 500, 1000, 5000, 6000]
print(sorted(list1))
# [6000, 5000, 1000, 500, 400, 300, 200]
print(sorted(list1,reverse=True))

# note -> sorted and sort me ye difference hai ki thoda sa syntax alg hai or most important sorted ek new list bana ke deta hai and sort jo hai wo existing list me hi change kr deta hai so carefully handle krna.


list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)


# index function hmlog ko koi element kon se index pe hai wo laake de deta hai

print(list1.index(6000))


# string problem / excercise.
# problem statement -> maan ke chalo ki hmaare pass string me title function jo saaare words ke first letter ko capitalize kr deta hai agr ye function ni hua toh hmlog ye kaam kaise krege uska core logic hmko likhha hai.


# Hello How Are You
s1=print("hello how are you".title())
sample = "how are you baby"
# solution -> toh idea ye hai ki ap ek kaam kro sbse pehle saara words nikal lo and then phir saare words pe capitalize operation lagao and then phir list me convert kro and then phir usko join kr do.

print(sample.split())
l=[]
for i in sample.split():
    print(i.capitalize())
    l.append(i.capitalize())

print(' '.join(l))






