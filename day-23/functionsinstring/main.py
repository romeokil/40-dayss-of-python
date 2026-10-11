# Day - 23 Functions in String

# common functions but it is applied to strings ,list , tuple , dictionary

# len
# max
# min
# sorted

a = 'Kolkata'

print(len(a))

print(max(a))

print(min(a))

# ye ascii value ke hisab se sort krta hai
print(sorted(a))
print(sorted(a,reverse=True))



# functions specific to strings only

# and ye jitna bhi function hai tm dekho chahe koi bhi function lagao actual string kabhi bhi change ni ho rha hai mtlb function lagane ke baad agr tm actual string ko print krgea toh wo actual string change ni hone wala 

# 1. Capitalize/ Title / Upper / Lower / Swapcase
# or capitalize jo hai wo first word ke first letter ko capitalize krega
print("it is raining today".capitalize())
# ab dekho title jo hai each word ke first letter ko capital kr diya
print("It is raining today".title())
# ab upper jo hai word ko uppercase me convert kr diya hai
print(a.upper())
# ab lower jo hai word ko lowercase me convert kr diya hai.
print(a.lower())
# swapcase jo hai wo lower ko upper me convert kr dega or uppper ko lower me.
print("KOlkaTa".swapcase())


# Count function jo hai wo char ko hi ni koi substring ko bhi kisi sentence me se count krke batata hai and agr ni present ho toh count = 0 deta hai

print("my name is khan".count("a"))

print("my name is khan".count("khan"))

print("my name is khan".count("x"))

# find/index wo ye hai jo kisi bhi char ya substring jo hai uska index laake de deta and suppose wo char ya phir substring ke multiple occcurences hai toh phir wo first occuerence wala index laake dega dono hi but diff ya hai ki find agr koi element ni hua toh wo -1 dega but index error throw kr dega.

print("my name is khan".find("a"))

print("my name is khan".index("a"))

print("my name is khan".index("khan"))


# startsWith/endsWith ye check krta hai ki wo string us particular string se start ya phir end ho rha hai ky or ye boolean value return krta hai. 

print("it is raining".startswith("it"))

# ye wala case hm check kr rhe the ki agr mera string capital hai toh ky agr hm small doodhe toh ky uska consider krega but wo bola ni bhai wo consider ni ho skta hai,exactly match krna chahiye.
print("It is raining".startswith("it"))

print("it is raining".endswith("ing"))


# Format function basically agr ap close braces dete ho toh us time wo us khaali braces ko bhrne me kaam aata hai ye hmlog jb login functionality sb bnaege toh kaam aaega.

# Different ways of writing this function
print("my name is {} and my age is {}".format("Rahul",25))

# toh dekho esme hmlog jo daale hai ulta daal diye mtlb basically hm ye dikhaana chah rhe the ki hmlog index bhi daal skte hai 0 and 1 daalte toh ok tha but hmlog apne hisab se ulta daale just example ke liye.
print("my name is {1} and my age is {0}".format("Rahul",25))

print("my name is {name} and my age is {age}".format(name="Rahul",age=30))

# isalnum -> checks alphabet and number ho
# isalpha -> checks alphabet
# islower -> lowercase me hai ya ni
# isupper -> uppercase me hai ya ni
# isdigit -> checks wo pura digit hai ya ni

print("flat20".isalnum())

print("flat".isalpha())

print("20".isdigit())

# qki underscore allowed hai but agr tm space de diye beeech toh wo kisi type ka identifier allowed ni hai
print("hello_world".isidentifier())

# split function split krta hai on the basis of jo bhi chiz tm andr daaloge like space, koi letter ya phir koi substring

print("who is the pm of india?".split())

print("who is the pm of india?".split("i"))

print("who is the pm of india?".split("the"))

# join function bilkul hi ulta hai split ka jaise split me hmlog split kr rhe hai on some character or substrig ya pe join kr rhe hai and ek string form kr rhe hai

print(" ".join(['who', 'is', 'the', 'pm', 'of', 'india?']))

print("-".join(['who', 'is', 'the', 'pm', 'of', 'india?']))


# replace function whi kisi chiz ko agr replace krna hai toh

print("my name is rahul".replace("rahul","akash"))

# strip function jo hai apke leading ya trailing spaces ko hatata hai 

print("    my name is rahulllaawwaa   ".strip())




