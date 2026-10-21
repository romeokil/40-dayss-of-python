# day - 28 variable and  memory references.

# apka jo bhi variable hai wo ram me basically ek jagah bnata hai jb bhi ap wo program execute krte ho, toh aisa hai ki uska ek memory address (or ye hexadecimal format me hote hai like 0x1000) hota hai.

# python koi bhi variable ko name bolta hai.

# id(a)
# ye variable ko memory address de dega jaha pe a store hai.

# c++ me hmlog call by value and call by reference padhe the toh same whi python me sb kuch object hai toh ye concept call by object reference krke chizen hai.
# qki jo basically wo variable hai wo ek memory address ko point krta hai , wo bhi jo wha se start ho rha hai.


# Aliasing -> mtlb ki ex a=5 and b=a kr diye tm toh ky hua , basically b bhi whi same memory address pe point krne lg gy, esi ko aliasing bhi bolte hai.


# reference counting -> mtlb ki koi ek variable me uspe kitna log point krke rkhe hai uska count mil jaega hmko niche example likhe hai dekh lijiye but jaruri ni hai ki ye shi count dikhaega qki ye 2 chiz pe depend krta hai pehla apka excution environment and dusra apka python implementation details.

import sys
a="refrefhijkl"
b=a
c=b

print(sys.getrefcount(a))


# garbage collection -> python jo existing program hai usme ek garbage collector program run krta hai or aise chiz ko doondta hai jo memory me space occupy kiya hai but usko koi point ni kr rha hai wo bs faaltu space leke baitha toh aise agr bht saaare variables ya phir koi object faaltu space occupy kr rha hai toh memory toh overhaul ho jaega , toh eske liye garbage collector hmesha ye sb faaltu jo baitha hua hai usko garbage smjh ke collect kr leta hai ye program ya function periodically run hota hai.

# Example 
a=5
b=a
c=b

# and uske baaad hmlog del a, del b ,del c likh diye toh ab wo 5 toh faaltu hi memory me jagah le rha hai qki hmne uska saaara reference a, b , c sbko delete kr diya memory se toh aise values ko garbage collector collect kr leta hai.


# Wierd behaviour in python

# 1st -> whi getrefcount wala pata ni count alg hi aata hai qki there is high chance ki koi or bhi variable hai tmhare program alawa jo ki currently usko utilize kr rha hai and ye count decrease hota hai agr uncommon no like 731 type ka loge toh and agr 2 jaisa no loge toh ye phir count jyada hi dikhaega.

# 2nd -> agr tm koi value lete hai -5 se 256 tk tb toh agr tm same value assign kr rhe hai either by aliasing or by assigning or agr ap id print kroge toh same memory address bataega but agr es range ke baad assignment kroge toh different values bataega and aliasing ke case same id bataega.
# Reason -> ye python ka memory utilization / optimization ka tarika python bola ye range ka no sbse jyada use hota hai toh jbbhi python program run kroge wo already ek memory ye saaare range of no (-5 to 256) bhr deta hai, toh eslie hmlog ko same memory address mil rha tha.

# this is assignment
# a=5
# b=5

# this is aliasing
# a=6
# b=a

# 3rd behaviour -> agr tm string me bhi dekhega toh agr koi string valid identifier hai toh us case me ye apko same memory address dega but whi agr koi different memory address hai toh us case me apko different id's dega.

# example
# valid identifier
a="haldia"
b="haldia"
# 2312500640288
# 2312500640288
print(id(a))
print(id(b))

# not a valid identifier
#  File "C:\Users\ADMIN\Desktop\100_days_of_python\day-28\variablememoryref\main.py", line 64
#     my kingdom="this is my kingdom"
#        ^^^^^^^
# SyntaxError: invalid syntax
my kingdom="this is my kingdom"
my kingdom="this is my kingdom"

print(id(a))
print(id(b))


# python me directly element store ni krte hai bs aisa hai ki wo eleement jaha pda hua hai uska memory address store krte hai list me agr koi list hai toh.



# mutability -> ke help se hmlog edit ya phir change kr skte hai ko bhi data ya element ko uske specific memory location me or eska ulta immutability or kisko ap edit/change kr paoge ye depend krta hai us particular datatype pe, niche list hai mutable/immutable datatype ka.

# upr wala ka conclusion -> bhai dekho ho skta hai tmko dikhe ki tuple me ya string hm element add kiye or ho gy but aisa hai ki basically ek naya tuple or string bn jaata hai agr tm id print kroge toh pata chal jaega qki wo dono hi different location pe milege,but ye kaam mutable data type( list, sets, dictionary me ni hoga) wha pe element add krne ke baad bhi ap dekho toh wo same memory location ko hi point kr rhe hoga or esko hi in-place changes krna bolte hai.

# side effects of mutation -> 

# maan ke chalo apne ek list banaya l=[1,2,3] and phir aliasing kiya l1=l toh afcorse dono hi same memory location ko point krega but ap glti se l1.append(4) and then ye krne ke baad l1 list me toh 4 append ho hi jata hai , as well as l me bhi 4 append ho gy , toh bhai agr koi l ko refe kr rha hoga toh wo toh sr pakad ke baith jaega ki bhai ye kaise ho gy , mere time pe toh sirf [1,2,3] hi tha , ye mutability ka dark fantasy hai, toh es case se bachne ke liye hmlog aisa kr skte hai ki hmlog clone kre l1=l[:] esko cloning bolte hai and ab ap agr id print kroge toh different memory location showcase krega.

# ek or chiz agr immutable datatype ke andr mutable datatype hai toh agr hm usko change krna chahe toh kr skte hai, depend ek hi chiz krta hai ki change kisko krna chahte ho agr wo mutable hai toh change ho jaega agr wo mutable ni hai toh change ni ho paega.



# mutable -> list , dictionary, sets
# immutable -> tuple, strings, bool, complex, float, int



# Conclusion ->>>

# 1 -> getrefcount anamoly
# 2 -> -5 to 256 
# 3-> strings valid and invalid identifier


