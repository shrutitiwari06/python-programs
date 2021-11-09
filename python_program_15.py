#1.Display float number with 2 decimal places using print()
val = float(input("Enter any number: "))
format_float = "{:.2f}".format(val)
print(format_float)
Enter any number: 4.3
4.30

#2.Takes two integer numbers and  return their product.
val1=2
val2=4
def prod(x,y):
  return x*y
print(prod(val1,val2))
8

#3.Write a Python program to get the volume of a sphere with radius 10.
pi = 3.1415926535897931
r= 10
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)
The volume of the sphere is:  4188.790204786391
  
  #4.Accept two numbers from the user and multiply them together.
val1=int(input("enter no. : "))
val2=int(input("enter no. : "))
def prod(x,y):
  return x*y
print(prod(val1,val2))
enter no. : 3
enter no. : 3
9

#5.Write a Python program that accepts an integer (a) and computes the value of a+aa+aaa.
a=int(input("enter any integer no. :"))
print(a+(a*a)+(a*a*a))
enter any integer no. :2
14

#6.Write a Python program to calculate the length of a string
string="shruti tiwari"
print(len(string))
13

#7.Write a Python program to parse a string to Float & Integer
a = "1500"
b = int(a)
c = float(a)

print(type(b))
print(b)

print(type(c))
print(c)
<class 'int'>
1500
<class 'float'>
1500.0

#8.Given two integer numbers return their sum. If the sum is greater than 100, then return their product.
val1=4
val2=97
def prod(x,y):
  return x*y
def sum(x,y):
  return x+y
sum=sum(val1,val2)
if(sum>100):
  print("product :",prod(val1,val2))
else:
  print("sum :",sum)
  sum :101
    
#9.Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum
a=5
b=0
c=5

def sum(x,y,z):
  return x+y+z
sum=sum(a,b,c)
if(a==b and a==c):
  print("sum :",sum)
else:
  print("sum :",sum*4)
  sum : 100
    
 #10.A shop will give discount of 50% if the cost of purchased quantity is more than 10000. Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.
quantity=int(input("enter quantity of item :"))
price=quantity*100
if(price>10000):
  print("total price is :",(price/100)*50)
else:
 print("total price is :",price)   
  enter quantity of item :101
total price is : 5050.0
  
 #11.To check whether a number is divisible by 8 and 12 or not.
a=int(input("enter any no. :"))
if(a%8==0 and a%12==0):
  print("{0} number is divisible by 8 and 12".format(a))
else:
  print("{0} number is not divisible by 8 and 12".format(a)) 
  enter any no. :48
24 number is divisible by 8 and 12  


#12.To check whether a given number is even or odd.
num = int(input("Enter a number to check even or odd:- "))
if (num % 2) == 0:
   print("{0} is Even number".format(num))
else:
   print("{0} is Odd number".format(num))
Enter a number to check even or odd:- 4
4 is Even number


13.Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% :  Grade F'''

phy=int(input("enter physics marks :"))
chem=int(input("enter chemistry marks :")) 
bio=int(input("enter biology marks :"))
math=int(input("enter marhematics marks :"))
comp=int(input("enter computer marks :"))
per = (phy + chem + bio + math + comp) / 5.0
print("Percentage = ", per)

if(per >= 90):
  print("Grade A");
elif(per >= 80):
  print("Grade B");
elif(per >= 70):
  print("Grade C");
elif(per >= 60):
  print("Grade D");
elif(per >= 40):
  print("Grade E");
else:
  print("Grade F")
  enter physics marks :60
enter chemistry marks :30
enter biology marks :25
enter marhematics marks :54
enter computer marks :64
Percentage =  46.6
Grade E


#14.Take input of age of 3 people by user and determine oldest and youngest among them.
person1 = int(input("Enter age of person 1 : "))
person2 = int(input("Enter age of person 2 : "))
person3 = int(input("Enter age of person 3 : "))

# check oldest
if person1 > person2 and person1 > person3:
    print("Person 1 is oldest")
elif person2 > person1 and person2 > person3:
    print("Person 2 is oldest")
elif person3 > person1 and person3 > person2:
    print("Person 3 is oldest")

# check youngest
if person1 < person2 and person1 < person3:
    print("Person 1 is youngest")
elif person2 < person1 and person2 < person3:
    print("Person 2 is youngest")
elif person3 < person1 and person3 < person2:
    print("Person 3 is youngest")
Enter age of person 1 : 2
Enter age of person 2 : 50
Enter age of person 3 : 43
Person 2 is oldest
Person 1 is youngest

'''15.Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill'''
unit = int(input("enter units of electricity : "))
if(unit<=50):
  bill=unit*0.50
  totalbill=bill+(bill/100)*20
  print("electricity bill is ",totalbill)
elif(unit<=150):
  bill=unit*0.75
  totalbill=bill+(bill/100)*20
  print("electricity bill is ",totalbill)
elif(unit<=250):
  bill=unit*1.20
  totalbill=bill+(bill/100)*20
  print("electricity bill is ",totalbill)
elif(unit>250):
  bill=unit*1.50
  totalbill=bill+(bill/100)*20
  print("electricity bill is ",totalbill)
 enter units of electricity : 200
electricity bill is  288.0
