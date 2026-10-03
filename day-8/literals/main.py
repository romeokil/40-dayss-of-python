# literals mtlb ki hmlog kitne tarike se define kr skte hai 
# mainly 4 tarah ke literals hote hai 

# numeric literals
# string literals
# boolean literals
# special literals


# numeric literals

a= 0b1010 #binary literals
b= 100 #decimal literals
c= 0o310 #octal literals
d= 0x12c #hexadecimal literals

# float literals
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e+3

# complex literals
x= 3.14j

print(a,b,c,d)
print(float_1,float_2,float_3)
print(x,x.real,x.imag)


# string literals

string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str ="""This is a multiline string basically used when we have too much content or like if we are writing blogs or something similar content"""
unicode = u"\U0001f923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


# boolean literals

a = True + 1
b = False + 10

print(a)
print(b)

# special literal
# ab dekho aisa hai ki python me toh feature hai ki hmlog at a time jb jarurat ho define kr skte hai variable toh shi chiz hai bada , but in casee hmko jarurat ho toh hm aise kisi variable ko None define krke rkh skte hai
u = None
print(u)