# print("Hello World..!")
 a=20
 b=30
 a=a+b
 b=a-b
 a=a-b
 print("after swaping A=", a,"B=",b)

 c=a//b
 print(c)

# input/ output concept..!
# practice  questions....
#1
 name=input("Enter Your Name:")
 print(f"Hello {name}, Welcome to python!")

#2
 a=int(input("first num "))
 b=int(input("sec num "))
 c= a+b
 print (f"The addition of {a},{b} is  {c}")

#3
 num=int(input("enter the num to check odd or even:"))
 if num % 2 == 0:
    
     print(f"{num} is even")

    
 else:
     print(f"{num} is odd")

#4
 age=int(input("enter your age : "))
 if age >=18:
    
   print("You are eligible for voting")

    
 else:
      print("Not eligible for voting")

#5
 sub1=float(input("enter sub1 marks:" ))
 sub2=float(input("enter sub2 marks:" ))
 sub3=float(input("enter sub3 marks:" ))
 avrg=sub1 + sub2 + sub3/3
 print("The avrg of 3 subjects is :",avrg)

#string manipulation
 #pratice questions

#1. simple greeting program....
 name=(input("Enter Your Name "))
 age =int(input("your age plz..."))
 print(f"heyy ...{age} year old {name} ,Welcome yarr...!")

#2. string maipulation exercise

 message =input("What's up...! ")
 print(message.upper())
 print(message.lower())
 print(message.replace( " ","_"))
 print(message.strip())

#3. charcter counter 

 name=input("Your name plz..")
 count=len(name)
 print(f"Your name includes {count} charcters (white space also included)")

#4. escape sequence

 print("hello \n ")
 print("\t world ")
 print(" This is backslash :\\")

#Check positive or negative number 

num=int(input("enter the value to check positive or negative"
              if(num>0):
                print("positive number")
              else:
                 print("negative number")


#simple intrest 

   p=float(input("Enter the principle ammount")
   t=float(input("Enter the time")
   r=float(input("Enter the intrest rate")
     SI=p*t*r/100

    totalAmt=p+SI

   print("simple intrest"SI)   
   print("Total amt"totalAmt)
