name=input("Enter your name: ")
age=input("enter your age:")
print("His Name is "+name +" and his age is "+age)


#practice program
name=input("Enter your name: ")
age=int(input("Enter your age: "))
if(age>=18):
    print(name+" is eligible to vote")
elif(age<18):
    print(name+" is not eligible to vote")