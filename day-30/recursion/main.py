# day -30 recursion in python

# recursion me hmlog existing function ko dubara call krte hai.

# programs we need to do here. (Using Recursion Approach)
# 1. Multiplication
# 2. Factorial
# 3. Palindrome
# 4. Rabbit Problem/ Fibonacci / Follow Up - Using Memoization Approach
# 5. Power Set (Find all combos)


# 1.Multiplication

def mul(no,freq):
    if freq==1:
        return no
    else:
        return no + mul(no,freq-1)
# 12
print(mul(3,4))


# 2.Factorial

def fact(no):
    if no==1:
        return 1
    else:
        return no*fact(no-1)
# 120
print(fact(5))


# 3.Palindrome

def palindrome(i,j,s):
    if i>=j:
        return True
    elif s[i]!=s[j]:
        return False
    else:
        return palindrome(i+1,j-1,s)
# False
print(palindrome(0,len("jkl")-1,"jkl"))
# True
print(palindrome(0,len("madam")-1,"madam"))

# 4.Rabbit Problem / Fibonacci
import time
def fib(no):
    if no==0 or no==1:
        return 1
    else:
        return fib(no-2)+fib(no-1)
# 8
start=time.time()
# print(fib(50))
# 0.0001494884490966797
# print(time.time()-start)
# 13
# print(fib(6))

# 4.1 -> Rabbit Problem / Fibonacci - Follow Up Approach Using Memoization

def memo(no,d):
    if no in d:
        return d[no]
    else:
        d[no]=memo(no-1,d)+memo(no-2,d)
        return d[no]

d={0:1,1:1}
start=time.time()
# memo(50,d)
# print(time.time()-start)


# 5. Power set -> Try / Find all combos

def allcombo(i,lt,temp,result):
    if i==len(lt) and len(temp)==0:
        return
    if i==len(lt):
        result.append(temp.copy())
        return
    # take and skip case
    temp.append(lt[i])
    allcombo(i+1,lt,temp,result)
    temp.pop()
    allcombo(i+1,lt,temp,result)

l=[1,2,3]
temp=[]
result=[]
allcombo(0,l,temp,result)
print(result)

