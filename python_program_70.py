# 16. A student will not be allowed to sit in exam if his/her attendence is less than 80%.
# Take following input from user
# Total Number of classes held
# Total Number of classes attended. And print percentage of class attended. Is student is allowed to sit in exam or not.

a=int(input("Number of classes held:"))

b=int(input("Number of classes attended:"))

percentage=b/a*100

if percentage>=80:

        print("The student is allowed to sit in the exam hall")

else:

        print("The student is not allowed to sit in the exam hall")
 Number of classes held:10
Number of classes attended:9
The student is allowed to sit in the exam hall



#17. Calculate income tax for the given income by adhering to the below rules
# Taxable Income        Rate (in %)
# First Rs.10,0000         0
# Next Rs. 10,0000       10
# The remaining           20

income=int(input("enter income :"))

if (income <= 100000):
  tax = 0

elif (income <= 200000):
  tax = (income*10)/100

else :
  tax = (income *20)/100

print("you owe", tax, "Rupees in tax!")
enter income :500000
you owe 100000.0 Rupees in tax!


#18. Program to find digital sum of a given Number
#    ex: n=123  Digital sum----->1+2+3=6
def getsum(n):
  sum=0
  num = str(n)
  for i in num:
    sum = sum + int(i)
  return sum
  
n=int(input("Enter the number:"))
print(getsum(n))
Enter the number:123
6


#19. Program to find the digital product of a given number
#    ex: n=43   Digital product ----->4*3=12
def getProduct(n):
  product = 1
  num = str(n)
  for i in num:
    product = product * int(i)
  return product
  
n=int(input("Enter the number:"))
print(getProduct(n))
Enter the number:43
12



# 20.Find the sum of the series 3 +33 + 333 + 3333 + .. n terms
n=int(input("Enter the range of number:"))
sum=0
p=3
for i in range(1,n+1):
    sum += p
    p=(p*10)+3
print("The sum of the series = ",sum)
Enter the range of number:3
The sum of the series =  369


#21.Print the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
    * 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


#22. Program to reverse a given Number.    ex: n=123   Reversed no is 321
n = 4562
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print(rev)
2654


#23.Program to check whether a given number is a palindrome or not

def reverseDigits(num) :
	rev_num = 0;
	while (num > 0) :
		rev_num = rev_num * 10 + num % 10
		num = num // 10	
	return rev_num

def isPalindrome(n) :
	rev_n = reverseDigits(n);
	if (rev_n == n) :
		return 1
	else :
		return 0


n = 121	
if isPalindrome(n) == 1 :
  print("Is", n, "a Palindrome number? ->", True)
		
else :
  print("Is", n, "a Palindrome number? ->", False)
  Is 121 a Palindrome number? -> True
  
  
  #24.Program to check whether a given number is an Armstrong number or not.
num = int(input("Enter a number: "))
sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
 Enter a number: 407
407 is an Armstrong number


#25.Program to find factorial of a given number.
fact=1
n=5
while(n!=0):
    fact=fact*n
    n=n-1

print("fact",fact)
fact 120


#26)Program to find whether a given number is a strong number or not.
 # e.g. n=145
 # 1!+4!+5!==145
def factorial(d):
   if(d==1 or d==0):
      return 1
   return d*factorial(d-1)
def isStrong(n):
   num=n
   sm=0
   while(n>0):
      digit=n%10
      sm=sm+factorial(digit)
      n=n//10
   if(sm==num):
      return True
   else:
      return False
print("Input a number")
a=int(input())
print(isStrong(a))
Input a number
145
True


#27. Program to find whether a given number is a unique number. For example, 20, 56, 9863, 145, etc. are the unique numbers
#while 33, 121, 900, 1010, etc. are not unique numbers

visited = [0,0,0,0,0,0,0,0,0,0];
num=20
while (num):
  if visited[num % 10] == 1:
    break;
  visited[num % 10] = 1;
  num = (int)(num / 10);

if num == 0:
  print("no. is unique");
else:
  print("no. is not unique")
  no. is not unique
  
  
  #28)Program to find whether a given number is a perfect number or not.
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))
True


#29)Program to find whether a given number is a prime number or not.
num = 11
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is not a prime number")
    
 11 is a prime number


#30)Print downward Half-Pyramid Pattern with Star (asterisk)
#* * * * *  
#* * * *  
#* * *  
#* *  
#*
rows = 5 
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")
    * * * * *  
* * * *  
* * *  
* *  
*  

# 31)Print  following pattern: 
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
for i in range(10):
    print(str(i) * i)
1
22
333
4444
55555
666666
7777777
88888888
999999999

# 32)Print  following pattern: 
# 1
# 12
# 123
# 1234
# 12345
# 123456
# 1234567
# 12345678
# 123456789'''
for i in range(1,9+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
    1
12
123
1234
12345
123456
1234567
12345678
123456789


#33)Print following pattern: 
#A
#BB
#CCC
#DDDD
#EEEEE
#FFFFFF
#GGGGGGG
#HHHHHHHH'''

for i in range(8):    
      print((chr(65+i)+"")*(i+1))
    A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH

#34)Write a Python program to calculate the length of a given string.
str = "shruti"
print(len(str))
6


#35.Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string.
#Sample String : 'abc', 'xyz' 
#Expected Result : 'xbc ayz'
str1 = input("Please Enter First String : ")
str2 =input("Please Enter Second String : ")
 
x=str1[0:1]
 
str1=str1.replace(str1[0:1],str2[0:1])
 
str2=str2.replace(str2[0:1],x)
 
print("Your first string has become :- ",str1)
print("Your second string has become :- ",str2)
Please Enter First String : shruti
Please Enter Second String : tiwari
Your first string has become :-  thruti
Your second string has become :-  siwari
  
  
  #36. Write a Python program to add 'polis' at the end of a given string (length should be at least 3).
#  If the given string already ends with 'polis' then add 'polisCS' instead.
#  If the string length of the given string is less than 3, leave it unchanged. 
#  Sample String : 'abc'
#  Expected Result : 'abcpolisCS' 
#  Sample String : 'Acropolis'
#  Expected Result : 'AcropolisCS'

def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-5:] == 'polis':
      str1 += 'CSIT'
    else:
      str1 += 'polis'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('Acropolis'))
ab
abcpolis
AcropolisCSIT


#37)Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))
{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


#38. Write a Python program to change a given string to a new string where the second and last chars have been exchanged.
def change_sring(str1):
      return str1[0:1]+str1[-1:] + str1[2:-1] + str1[1:2]
	  
print(change_sring('abcd'))
print(change_sring('12345'))
adcb
15342

#39)Write a Python program to remove the characters which have even index values of a given string.
def even_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2!= 0:
      result = result + str[i]
  return result

print(even_values_string('abcdef'))
print(even_values_string('python'))
bdf
yhn


#40 .Write a Python program that takes input from the user and displays that input back in upper and lower cases.
str1=input("enter string :")
print("in upper :" ,str1.upper())
print("in lower :" ,str1.lower())
enter string :SHruti
in upper : SHRUTI
in lower : shruti
  
  
#41)Write a Python program to count occurrences of a substring in a string.
str1 = 'school collage school'
print()
print(str1.count("school"))
print()  
2


#42)Write a Python program to lowercase first n characters in a string.
str1 = 'ACROPOLIS'
print(str1[:4].lower() + str1[4:])
acroPOLIS


#43)Write a Python program to remove spaces from a given string.
def remove_spaces(str1):
  str1 = str1.replace(' ','')
  return str1
    
print(remove_spaces("A c r o p o l i s"))
print(remove_spaces("S H R U T I "))
Acropolis
SHRUTI


#44)Write a Python program to move spaces to the front of a given string.
def move_Spaces_front(str1):
  noSpaces_char = [ch for ch in str1 if ch!=' ']
  spaces_char = len(str1) - len(noSpaces_char)
  result = ' '*spaces_char
  result = '"'+result + ''.join(noSpaces_char)+'"'
  return(result)

print(move_Spaces_front("Acropolis    Collage  "))
print(move_Spaces_front("CSIT         Branch "))
"      AcropolisCollage"
"          CSITBranch"


#45)Write a Python program to find the maximum occurring character in a given string.
def get_max_occuring_char(str1):
  ASCII_SIZE = 256
  ctr = [0] * ASCII_SIZE
  max = -1
  ch = ''
  for i in str1:
    ctr[ord(i)]+=1;
 
  for i in str1:
    if max < ctr[ord(i)]:
      max = ctr[ord(i)]
      ch = i
  return ch

print(get_max_occuring_char("Acropolis"))
print(get_max_occuring_char("Shruti"))
o
S


#46)Write a Python program to capitalize first and last letters of each word of a given string.
def capitalize_first_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  
     
print(capitalize_first_last_letters("acropolis"))
print(capitalize_first_last_letters("Shruti"))
AcropoliS
ShrutI


#47)Write a Python program to compute sum of digits of a given string.
def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit
     
print(sum_digits_string("Acropolis596CI"))
print(sum_digits_string("CS35IT"))
20
8

#48)Write a Python function that takes a list of words and returns the length of the longest one.
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["CS", "ACROPOLIS", "CSIT"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
Longest word:  ACROPOLIS
Length of the longest word:  9
  
  
  #49.Write a function x(n) for computing an element in the sequence xn=n^2+1. Call the function for n=4 and write out the result.

def x(n):
  return(n**2 + 1)

print(x(4))
17

#50. Take the following Python code that stores a string: ‘str = 'Y-tatata-acropolis: 0.8475'. Use find and string slicing to extract the portion 
#of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

string = 'Y-tatata-acropolis: 0.8475'
col_pos = string.find(':')                  # Finds the colon character
number = string[col_pos + 1:]                 # Extracts portion after colon
confidence = float(number)                  # Converts to floating point number
print(confidence)
0.8475


#51. Write a function that returns the middle value among three integers. (Hint: make use of min() and max()). Write code to test this function with different inputs.

def middleOfThree(a, b, c) :
	if a > b :
		if (b > c):
			return b
		elif (a > c) :
			return c
		else :
			return a
	else:
		if (a > c) :
			return a
		elif (b > c) :
			return c
		else :
			return b

a = 20
b = 45
c = 40
print( middleOfThree(a, b, c) )
40


#52.Write a function that computes the area of a rectangle. Then, write a second function that calls this function three times to compute the surface area of a rectangular solid.
def secondfun():
  for i in range(3):
    print(area(i+1,i+3))

def area(h,w):
  area=h*w
  return area
height=2
width=3
print(area(height,width))

secondfun()
6
3
8
15


#53.Create an outer function that will accept three parameters, a, b and c. Create an inner function inside an outer function that will calculate the
#addition of a, b and c. At last, an outer function will add 5 into addition and return it 
def num1(x,y,z):
  def num2(a,b,c):
    return a+b+c
  outer=num2(x,y,z)+5
  return outer

print(num1(5,4,5))
19

#54.Write a program to create a recursive function to calculate the product of numbers from 10 to 100.

def recur(n):
   if n == 10:
       return n
   else:
       return n*recur(n-1)

print("the product of numbers from 10 to 100 : " "is", recur(100))
the product of numbers from 10 to 100 : is 257182031095525112107857249934597388918419224714455526533820998388496472644482792132224051962512451185663850090463028434334174412800000000000000000000000
  
  
  #55.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number : "))
print(factorial(n))
Input a number : 5
120


#56.Write a Python function to display all the multiples of  7 & 9 within the range 100 to 500.
nl=[]
for x in range(100, 501):
    if (x%7==0) and (x%9==0):
        nl.append(str(x))
print (','.join(nl))
126,189,252,315,378,441

#57.Write a Python function  to check whether the given integer is a prime number or not.
num = 27
flag = False
def prime(n):
  flag1=False
  if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag1 = True
            break
  return flag1

flag=prime(num)
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
 27 is not a prime number


#58. Write a Python function that checks whether a passed interger is armstrong or not.

n = int(input("Enter a number: "))

def armstrong(num):
  sum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  return sum

summ=armstrong(n)
if n == summ:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
    Enter a number: 407
407 is an Armstrong number


#59. Program to return a function from another function.

def B():
	print("Inside the method B.")
	
def A():
	print("Inside the method A.")
	return B

returned_function = A()

returned_function()
Inside the method A.
Inside the method B.

#60. First, def a function, start_process, that takes one argument p. Then, if the start_process function receives an p equal to "Yes",
# it should return "Start Process" Alternatively, elif p is equal to "No", then the function should return "Start Process Aborted".
#  Finally, if start_process gets anything other than those inputs, the function should return "Sorry for the input".

def start_process(p):
  if p=="Yes":
    return "Start Process"
  elif p=="No":
    return "Start Process Aborted"
  else:
    return "Sorry for the input"

command= input("Enter a command: ")
print(start_process(command))
Enter a command: Yes
Start Process


#61. First, def a function called calculate_distance, with one argument (choose any argument name you like).
#   If the type of the argument is either int or float, the function should return the absolute value of the function input.
#   Otherwise, the function should return "No value". Check if it works calling the function with  9.6 and "what?".

def calculate_distance(argument):
  if type(argument) == int or type(argument) == float:
      return abs(argument)
  else:
      print("No value")

print("the absolute value : " ,calculate_distance(33.20))

calculate_distance("what?")
the absolute value :  33.2
No value


#62.Python program to display the sum of input (n) numbers using a list.

list1 = [11, 5, 17, 18, 23]
total=0
for i in range(0, len(list1)):
    total = total + list1[i]
 
print("Sum of all elements in given list: ", total)
Sum of all elements in given list:  74
  
  
  #63)Python program to insert a number to given position in a list.
print("Enter 10 Elements of List: ")
nums = []
for i in range(10):
    nums.insert(i, input())
print("Enter an Element to Insert at End: ")
elem = input()
nums.append(elem)
print("\nThe New List is: ")
print(nums)
Enter 10 Elements of List: 
2
3
4
5
6
1
8
6
9
5
Enter an Element to Insert at End: 
4

The New List is: 
['2', '3', '4', '5', '6', '1', '8', '6', '9', '5', '4']



#64. Write the program that prompts the user for a list of numbers and prints out the maximum and minimum of the 
# numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and 
# use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

my_list = []                     
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(number)

if my_list:
    print('Maximum: ', max(my_list) or None)
    print('Minimum: ', min(my_list) or None)
    Enter a number: 4
Enter a number: 55
Enter a number: 7
Enter a number: 4
Enter a number: done
[4.0, 55.0, 7.0, 4.0]
Maximum:  55.0
Minimum:  4.0
  
  
 #65.Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers.
my_list = []                     
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(number)

if my_list:
    print('Maximum: ', max(my_list) or None)
    print('Minimum: ', min(my_list) or None)
    Enter a number: 3
Enter a number: 4
Enter a number: 9
Enter a number: 1
Enter a number: done
Maximum:  9.0
Minimum:  1.0
  
  
  #66.Python program to delete an element from a list by index which is given by the user.

print("Enter 10 Elements: ")
arr = []
for i in range(10):
    arr.append(input())

print("\nEnter the Value to Delete: ")
val = input()

arr.remove(val)
print(arr)
Enter 10 Elements: 
3
4
6
9
76
23
65
41
54
55

Enter the Value to Delete: 
76
['3', '4', '6', '9', '23', '65', '41', '54', '55']



#67)Write a Python program to print a specified list after removing the 1st, 2nd and 5th elements.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (1,2,5)]
print(color)
['Red', 'Black', 'Pink']


#68)Write a Python program to generate all sublists of a list.
from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs


l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print("Original list:")
print(l1)
print("S")
print(sub_lists(l1))
print("Sublists of the said list:")
print(sub_lists(l1))
print("\nOriginal list:")
print(l2)
print("Sublists of the said list:")
print(sub_lists(l2))
Original list:
[10, 20, 30, 40]
S
[[], [10], [20], [30], [40], [10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40], [10, 20, 30], [10, 20, 40], [10, 30, 40], [20, 30, 40], [10, 20, 30, 40]]
Sublists of the said list:
[[], [10], [20], [30], [40], [10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40], [10, 20, 30], [10, 20, 40], [10, 30, 40], [20, 30, 40], [10, 20, 30, 40]]

Original list:
['X', 'Y', 'Z']
Sublists of the said list:
[[], ['X'], ['Y'], ['Z'], ['X', 'Y'], ['X', 'Z'], ['Y', 'Z'], ['X', 'Y', 'Z']]



#69)Write a Python program to find all the values in a list are greater than a given number.
list1 = [220, 330, 500]
list2 = [12, 17, 21]
print(all(x >= 200 for x in list1))
print(all(x >= 15 for x in list2))
True
False


#70)Python program to find the even numbers in a List.
list1 = [10, 21, 4, 45, 66, 93]
for num in list1:
    if num % 2 == 0:
        print(num, end=" ")
  10 4 66       
