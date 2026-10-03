# Day -10 if elif else 

# email -> "rahulkumarjha58978@gmail.com"
# password -> "Rahul1234"

email = input("Please Enter Your Email: ")
if '@' in email:
    password = input("Enter your Password: ")
    if email == "rahulkumarjha58978@gmail.com" and password =="Rahul1234":
        print("Welcome : ",email)
    elif email == "rahulkumarjha58978@gmail.com" and password != "Rahul1234":
        print("Sorry Password Wrong. Please try again.. You only had 1 chance left.") 
        password = input("Please Enter Your Password: ")
        if password =="Rahul1234":
            print("Yes Login Successfull, Welcome :",email) 
        else:
            print("Password Wrong, You have exhausted your Limit.")   
    else:
        print("Invalid Credentials..")
else:
    print("Sorry email itself is not correct. Please mention @ in the mail")