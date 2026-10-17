# dictionary in python

# dictionary aisa data structure hai jisme key value pair hote hai.

# rules for dictionary
# dictionary me koi indexing ni hota hai
# dictionary me key immuatable hote hai values mutable hote hai.
# keys unique hona chahiye


# mutable-> list/sets/dictionary
# immutable -> tuple/strings/int/float/boolean/complex

# agr tm immutable object ko edit krne ka try kroge toh uska memory address change hoga and address change hone ka mtlb hai ki ap new object form kr rhe ho.

# create/initialization of dictionary.

d={"name":"rahul","age":30};
# {'name': 'rahul', 'age': 30}
print(d)

# d1={[1,2,3]:"rahul"}

# ye dekho hmlog key jo chune hai wo mutable hai qki hmlog key ko list liye hai jo ki galat hai qki hmlog padhe the ki dictionary me key jo hai wo immutable hona chahiye ex:-tuple/string ye sb type

# d2={(1,2,3):"rahul"}

# ab dekho ye valid hai esme koi dikkat ni hai qki hmlog key ek tuple ko bnae hai toh eslie ye valid hai.

# key hmesha unique rhega dekho niche example mtlb hm ye kehna chah rhe hai ki dekho bhai agr same key but different values present hai toh jo value recent key me hoga usse wo update ho jaega.

d3={"name":"rahul","name":"rohit"}

# toh es case me agr hm same key likhe hai toh baad me jo aaega like rohit for our case wo name (key) value ke liye update ho jaega.

# {'name': 'rohit'}
print(d3)

# 2-d dictionary
d4={"name":"rahul","age":25,"marks":{"m1":40,"m2":60,"m3":78}}
# {'name': 'rahul', 'age': 25, 'marks': {'m1': 40, 'm2': 60, 'm3': 78}}
print(d4)


# accessing items in the dictionary
# rahul
print(d4['name'])
# 25
print(d4['age'])
# 25
# but hmlog ye .get sirf 1-d me laga skte hai 2-d me ni laga skte hai.
print(d4.get('age'))


# edit items in the dictionary

d4['marks']['m2']=70
# {'name': 'rahul', 'age': 25, 'marks': {'m1': 40, 'm2': 70, 'm3': 78}}
print(d4)

# add items in the dictionary

d4['gender']="male"
# {'name': 'rahul', 'age': 25, 'marks': {'m1': 40, 'm2': 70, 'm3': 78}, 'gender': 'male'}
print(d4)


# delete items in the dictionary

d5={}
# certainly bs wo particular key ko delete krega.
del d4['gender']
# {'name': 'rahul', 'age': 25, 'marks': {'m1': 40, 'm2': 70, 'm3': 78}}
print(d4)

# ye clear pura dictionary hi khaali kr dega.
d3.clear()
# {}
print(d3)


# operations

# dictionary me concatenation ni ho paega mtlb d3+d4 ye ni ho paega.

# loops chala skte hai dictionary me.
# name
# rahul
# age
# 25
# marks
# {'m1': 40, 'm2': 70, 'm3': 78}
for key in d4:
    print(key)
    print(d4[key])

# membership operator
# True
print("name" in d4)

# len() -> no of key-value pair present in the dictionary.

# min() -> minimum in the dictionary which is lexicographically sortest

# max() -> maximum in the dictionary which is lexicographically greatest

# sum () -> krte lekin keys hamara string hai na toh kaise sum kaam ni kr paega.

# sorted() -> dict ko sort kr dete hai.

# d3.keys() -> ye hmko dictionary ka sara keys nikal krke de dega.

# d3.values() -> ye hmko dictionary ka sara values nikal krke de dega.




