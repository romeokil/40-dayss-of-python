# Day - 8 Operators in python

# Operators hmlog use krte hai koi operation perform krne ke liye 2 operands ya variables ya values me operation ke liye

# arithmetic Operators
# comparision Operators
# logical Operators
# bitwise Operators
# assignment Operators
# identity Operators
# membership Operators

# 1 -> arithmetic division

x,y=5,2

print(" Arthemetic Division Starts..")
print(x+y)

print(x-y)

print(x*y)

# esko true division bolte hai isme point me no aata hai
print(x/y)

print(x%y)

print(x**y)

# esko integer division bolte hai
print(x//y)

# 2 -> comparision / relational operator
print("Comparision Operator Starts..")
print(x>y)

print(x<y)

print(x>=y)

print(x<=y)

print(x==y)

print(x!=y)


# 3 -> logical operator

x = True
y= False
print("Logical Operator Starts...")
print(x or y)

print(x and y)

print(not x)


# 4 -> Bitwise Operator

# Gyaan ka baat 

# Mainly Hmlog Bitwise operator kb use krte hai jbbhi hmlog image operations/processing krna hota or filter krna hota hai na toh us case me hmlog aaram se bitwise operator use krte hai wha pe jaha pe hmlog images ka bht saara kaam ho , wha pe.

x = 2 
y = 3
print("Bitwise Operator Starts...")
print(x & y)

print(x | y)

print(x >> 2)

print(y << 2)

# esko 1's complement
print(~x)


# 5 -> Assignment Operator

a = 4
print("Without any operation: ",a)
# a++ -> this is not valid in python
a+=4
print("After addition of 4: ",a)
# a-- -> this is not valid in python
a-=3
print("After substraction of 3: ",a)
a*=4
print("After multiplication of 4: ", a)
a/=2
print("After division of 2: ",a)
a%=2
print("After modulus of 2: ",a)

# 6-> Identity Operator 

# ho skta hai value equal ho ok but wo ye bilkul bhi imply ni krta hai ki wo dono same memory location me present ho , may be ho bhi skta hai ni bhi -> is and is not
a=4
b=4
print(a is b) 
# True

a = "Hello"
b = "Hello"

print(a is b)
# True

a = [1,2,3]
b = [1,2,3]

print(a is b)
# False

a = "Hello_world"
b = "Hello_world"

print(a is b)
print(a is not b)
# True


# 7 -> Membership Operator
# koi bhi chiz kisi chiz ke andr hai ya ni hai whi check krta hai ye

# ye chiz hmlog string , list , tuple , dictionary sbme check kr skte hai in and not in 
a ="mumbai"
print("Membership Operator")
print("M" in a)
print("m" in a)

b = [1,2,4]

print(1 in b)
print(3 not in b)
print(3 in b)
