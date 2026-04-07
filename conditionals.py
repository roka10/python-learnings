#Comparisons
#Equal: ==
#Not Equal: !=
#Greater Than: >
#Less Than: <
#Greater Than or Equal To: >=
#Less Than or Equal To: <=
#Object Identity: is
#Object Identity: is not

# and
# or
# not
if True:
    print("hey wassup")



a=input("enter your age:")
if(int(a)>=18):
    print("You are eligible to vote")
else:
    print("Your not eligible to vote")


num=input("enter number:")
num1=input("enter number 2:")

if(int(num)+int(num1)%2==0):
    print("The number is even:")
elif(int(num)+int(num1)%2!=0):
    print("The number is odd:")
else:
    print("The number is not a number:")


a=[1,3,4,23,73,8,0,45]
b=[1,3,4,23,73,8,0,45]

print(id(a))
print(id(b))
print(a is b)