# Day - 17 Built in Functions

# print kisi bhi chiz ko print krega
print("rahul")

# input kisi bhi chiz input lega
a1=int(input("Enter your No: "))
print(a1)

# type mtlb kisi ka bhi datatype bataega
print(type(a1))

# int,float,list,tuple,str me explicitly type casting krne ke liye
print(int(5.6))

# abs mtlb negative ko positive me convert kr deta hai ye toh tu c++ me padha hi hai

print(abs(4.5))

# pow mtlb whi power

print(pow(2,3))

# min/max mtlb whi max ya min no nikalne ke liye 

print(min(2,3,5,6))
print(max(3,4,6,8))

# round mtlb agr loat value point ke baad toh kitna bhi digit ho skta hai correct toh agr tm round krna chahta hai result toh tm kr skta hai

a= 22 /7
print(round(a,3))

# divmod mtlb x//y (integer division)and x%y (modulus division)

print(divmod(2,3))

# bin/oct/hex value chahiye toh ye func use kr skte ho

print(bin(2))

# id mtlb wo variable ka memory address  of your native machine de deta hai
a = 10
print(id(a))

# ord basically character ka ascii value nikal ke de deta hai ex - 'a' -> 97 , 'A' -> 65

print(ord('A'))
print(ord('a'))

# len ye basically length nikal ke de deta hai
lt = [1,2,3]
print(len(lt))

# sum basically sum nikal ke de deta hai
print(sum(lt))

# help function me kisi bhi function ke baare me puch skte ho ki ye ky krta hai

print(help(print))