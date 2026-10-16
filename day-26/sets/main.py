# sets in python
# ye jo hmlog maths pe sets padhe the na whi hai bs python me as an datatype bhi ek hai ye.

# ye 4 golden rules hai set ke baare me yaad rkhiye.

# 1.sets do not allow duplicates.
# 2.sets have no indexing and index ni hai toh slicing bhi ni kr paega.
# 3.sets don't allow mutable data types.
# 4.sets itself is a mutable datatype.



# creating a set

# ye empty set hai but ky hai ki dictionary and set dono hi curly braces use krte hai toh please dhyan rkhiyega ki ap agr aise declare krege toh empty set ni empty dictionary initialize ho jaega , qki python by default isko dictionary smjhta hai.
s1={}
# <class 'dict'>
print(type(s1))


s2=set()
# <class 'set'>
print(type(s2))

# homogenous set 
s1={1,2,3,4,5}
# {1, 2, 3, 4, 5}
print(s1)
# heterogenous set
s3={"hello",4.5,3,7,bool}
# {3, 4.5, 7, <class 'bool'>, 'hello'}
print(s3)


s4={1,1,2,3,3,4,4,4,5,6,6,7,7,7,7,7}
# {1, 2, 3, 4, 5, 6, 7}
print(s4)

s5={(1,2,3),"Hello"}
# ab dekho esme hmlog immutable datatype daale hai ek tuple dusra string
# or jaruri ni hai ki jis order me element hai same whi order me element set me dikhega qki yaha pe indexing ke jagah hashing use hota hai.
# {(1, 2, 3), 'Hello'}
print(s5)
# ye bhi allowed ni hai qki set ke andr set ni daal skte hai or naahi list daal skte hai.
# s5={{2,3},{3,5}}


# acccess items in the set via indexing.
# s3[0],s2[1] -> invalid hai ye.


# editing items in the set via indexing, ye bhi ni kr skte hai.

# add items in the set via .add method

s1.add(9)
# {1, 2, 3, 4, 5, 9}
print(s1)

# delete in set
# del -> del s2 pura set hi delete kr dega.
# remove -> s2.remove(4) ye element delete kr dega.
# pop -> s2.pop() ye item pop kr dega last wala.


# set operations


s6={1,2,3,4,5}
s7={5,6,7,8,9}

# ap yaha pe 2 sets ko jor ni skte ho.
# s1+s2 ye error de dega.
# s1*3 ye multiplication but ye error de dega.

# ye chal jaega memebership operator
# 1 in s6

# functions in sets

# len
# min
# max
# sum
# sorted
# union -> s1.union(s2) -> sara elements de dega.
# intersection -> s1.intersection(s2) -> common elements de dega.
# difference -> s1.difference(s2) -> jo s1 me hai.
# symmetric_difference -> s1.symmetric_difference(s2) -> intersection ka ulta
# isdisjoint -> s1.isdisjoint(s2) -> 2 sets ke beech me ek bhi item common na ho toh.
# issubset -> s1.issubset(s2) -> ye toh maths wala term hai
# issuperset -> s1.issuperset(s2) -> ye toh maths walaa term hai.






