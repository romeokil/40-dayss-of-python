# Day-7 Type conversion ke baare me sikhege

# type conversion ka mtlb hmlog agr ek type se dusre datatype me convert agr krte hai toh

# 2 types hai hmaare pass

# explicit and implicit type conversion

# implicit -> jaha pe wo apne ap type convert kr le.

print(3+ 5.4)

# explicit -> jaha pe explicitly krna pde convert.
# ye niche wla program
# same pehle wala program sum of 2 variables

def sum(first_no,second_no):
    # ya toh yha pe change kro 
    return int(first_no)+int(second_no)

if __name__ == "__main__":
    # ya phir jaha pe input liye ho
    # first_num = int(input("Enter Your First No: "))
    # second_num = int(input("Enter Your Second No: "))
    first_num = input("Enter Your First No: ")
    second_num = input("Enter Your Second No: ")
    result = sum(first_num , second_num)

    print("Your Result is : ", result)