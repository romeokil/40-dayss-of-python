# day - 29 functions in python.

# Ye niche 2 property functions ka characteristics bol skte hai.
# Abstraction ->  functions me abstractions hote hai like function ke andr ky ho rha hai i dont mind but hmlog usko use krte hai ex - print function aisa hai ki uske andr ky likha hai i dont know , hmko sirf call krne se mtlb hota hai jbbhi hmko kuch print krna hota hai.


# Decomposition -> mtlb for example koi bht bada wala application hai toh uske andr bht saare functions milke wo pura application chala rhe hoge like ek application me user login, register , update , or bhi bht kuch.


# function me ky ky hota hai.
# def <function_name> (paramter,argument):
    # docstring
    # """
    # description about the function ki ky kr rha hai ye function.
    # """
    # function _code 

    # return value (if any)


# General syntax of function 

def is_Even(no):
    """ 
    This function checks for a no whether it is odd or even.
    Input -> a valid Integer.
    Output -> Prints Odd or Even.
    Created by -> Rahul
    Last Updated by -> 22-10-2026


    """
    if no%2==0:
        return "Even"
    else:
        return "Odd"


for i in range(1,11):
    print(is_Even(i))

# generally jb hmko koi function ka description print krna hota hai toh kaaam aata hai.
# general syntax below -> 
# <function_name>.__doc__
print(is_Even.__doc__)

# Interstiing Facts
# C:\Python314\Lib
# ab dekho agr tm lets suppose es above particular location me jaake apna koi random function bana ke usko agr save krta hai toh phir tm apne program me usko aaram se use kr skta hai ex- hmlog import random likhte hai wo aajata hai , same waise apna function jo banaye hai wo likh skte hai and wo aaram se use kr skte hai.


# jb bhi function call hua ya hamara program start hua toh ek global frame bolke ek container bnta hai jiske andr apka sara functions/ variables sb store rehte hai or maan ke chalo ek function call hua toh ex - apka ram ek city hai then apka ghr ek global frame hai and apka ek local frame us ghr ke andr ek room hai and esme sara variable, function sb kuch kaam ho jaane ke baad ye room destroy ho jata hai, and function ka sara code es room ke andr hi chalege.


# Agr kuch function kuch return ni kr rha hai toh bhi by default wo None return krta hai python me.


# parameter vs argument ->
# jb koi function define hota hai and uske input me jo variables hote hai uske parameter bolege and jb actually function call hota hai jo variable yaha se hmlog pass krte hai wo argument hota hai.

# there are 4 types of argument ->
# 1. Default argument
# 2. Positional argument
# 3. Keyword argument
# 4. arbitrary argument


# 1. Default argument ->

def power(a=1,b=2):
    return a**b
# 8
print(power(2,3))

# ab dekho esme hm ek hi argument bheje but qki default argument diya hua tha toh hmlog bach gy otherwise code crash kr jata 
# 4
print(power(2))

# same esme bhi hmlog koi bhi argument ni diye hue hai toh code crash kr jata but bach gy default argument ke wajah se.
# 1
print(power())


# 2.  Positional Argument
# mtlb hai ki tm jis order me argument call kroge usi order me paramter usko recieve bhi krega.

# 3. Keyword Arguement
# ye bolta hai ki hmko position se koi bhi lena dena ni hai hmko keyword se lena dena hai jaise ki power(a,b) but call krte time hm like argument me power(b=2,a=3) toh eska answer 9 aaega naaki 8 because hm explicitly mention kiye ki bhai b=2 milna chahiye and a=3 toh chahe kisi bhi orders me paramter ho agr hmlog argument explicitly mention kr diye ki esko ye do , usko wo value do , toh phir wo positional ka koi mtlb ni rehta hai, ye tb kaam aa skta hai incase agr bht saara paratmers toh hmko thodi na yaad rhega ki hmlog kis order me chizen rkhe whi reason hai, and ye keyword argument positional argument ko override kr jata hai.


# flexible function ->
# ye ky bolta hai ki bhai hmko no of arguments se mtlb hi ni hai hmko ap kitna bhi argument do , hm sbka kaaam kr dege, qki basically ap jitna bhi element de rhe ho es case me ek tuple ke roop me store ho rha hai toh , example agr hmlog mutliplication ka lete hai.


def flexi(*numbers):
    print(type(numbers))
    product=1
    for i in numbers:
        product*=i
    return product
# <class 'tuple'>
# 2
print(flexi(2))
# <class 'tuple'>
# 24
print(flexi(2,3,4))
# <class 'tuple'>
# 720
print(flexi(1,2,3,4,5,6))


# global variable and local variable

# Gyaan -1 
# jo arguments hote hai wo ek global variable hota hai and jo parameters hote hai wo local variable hota hai and ye hm ek function ke respect me bol rhe hai.

# Gyaan -2
# ap dekho agr same variable ap globally us kr rhe ho and whi locally bhi use kr rhe ho but bina wo locally wo function call me define kiye , toh aisa hai ki wo local variable jo value global me pada hai wo pick kr lega but afcorse wo usko change ni kr paega na toh apne local function ke andr na hi khi bhi, afcrose ap print kr skte ho , but kisi bhi type ka modification allowed ni hai.

# Gyaan conclusion ->
# ek jo variable hai jo main progam ke andr hai usko koi bhi function use kr skta hai but changes/modification ni kr skta hai.

# koi function ke pass agr apna variable ni hai toh wo global variable ko use kr skta hai but usko modify ni kr skta hai.

# sirf use kr skta hai but changes ni kr skta hai.

# ab agr tm badmoss aadmi ho toh tm ek local function ke andr se global variable ko change kr skte ho with the help of keyword global x or y ,whatever ap likhna chahte ho.


# hamara nested/inner function jo hota hai wo main program se hidden/abstracted hota hai.

# python me sara chiz objects hai variable , functions , sb kuch.

# renaming a function
# deleting a function
# storing a function
# returning a function
# function as argument


# benefits of function ->
# code modularity -> koi bhi bada logic ko hmlog break kr skte hai smaller parts me jaise login , register sb alg alg modules hai.

# code resuability -> ek baar code likho uske baad mn bhr ke use kro.

# code readability -> code organized and coherent
