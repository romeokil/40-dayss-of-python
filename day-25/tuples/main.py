# Tuples in Python

# tuples are read-only datatype while list is read and write datatype.

# create
# access
# edit 
# add 
# delete
# operations 
# functions

# initialization of tuple
t1=(8,9)
# homogenous tuple
t2=(1,2,3,4,5)
# heterogenious tuple
t3=(1,"world",3.4,True)
# 2-d tuple
t4=(2,4,(6,7))

# ab dekho single item ka tuple aise generally ni bana skte hai ye syntax follow krna pdega.

# agr tm aise likhta hai toh wo single int element hota hai ek tuple ni proof dekho jb tm type of t5 kroge.
t5=(1)
t6=(1,)
# <class 'tuple'>
print(type(t4))
# <class 'int'>
print(type(t5))
# <class 'tuple'>
print(type(t6))

# aise explicitly bhi mention kr skte hai
t7=tuple('Goa')
# ('G', 'o', 'a')
print(t7)

t8=tuple([1,2,3,4,5])
# (1, 2, 3, 4, 5)
print(t8)




# access in tuple same hi hai jaise index se ya phir slicing wala
# 1
print(t2[0])
# world
print(t3[1])
# (6, 7)
print(t4[-1])
# 6
print(t4[2][0])



# edit in tuples

# tuples me hmlog edit ni kr skte hai chahe kuch bhi 
# tuples are immutable.
# ye niche wala list me change ho gy tha but tuple me change ni kr skte hai.
# t2[0]=100


# add in tuples

# since tuples are immutable so hmlog new item add bhi ni kr skte hai

# delete in tuples

# since tuples are immutable so hmlog agr item delete kr rhe hai toh eska mtlb ye hai ki hmlog existing tuple me changes kr rhe hai toh eslie wo bhi allowed ni hai.


# operations in tuple
# (1, 2, 3, 4, 5, 1, 'world', 3.4, True)
print(t2+t3)
# (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(t2*2)
# 1
# 2
# 3
# 4
# 5
for i in t2:
    print(i)

# membership operator
# True
print(1 in t2)

# functions in tuple
# 5
print(max(t2))
# 1
print(min(t2))
# 15
print(sum(t2))
# [1, 2, 3, 4, 5]
print(sorted(t2))
# [5, 4, 3, 2, 1]
print(sorted(t2,reverse=True))
