my_set={1,2,3}
print(my_set)
{1, 2, 3}

my_set={5.654,"Python",(1,2,3)}#Set can have only float int tuple string values as set's elements are immutable 
#but set itself is mutable
print(my_set)
{5.654, (1, 2, 3), 'Python'}

my_set={1.123,"python",[1,2,3] }
#This code will give error as we know that the element of set is immutable and list is mutable
#so [1,2,3] can't be a element in set
my_set=([1,2,3]) #Here {} is not used so that why it is considered as list
print(my_set)
type(my_set)
[1, 2, 3]
list

a={} #here empty {} will define dictionary to define set we have to use set function
print(a)
type(a)
{}
dict

a=set()
print(a)
type(a)
set()
set

my=set([1,2,3]) #Here it is accepting list but treating the each element of list as the element of set
print(my)
type(my)
{1, 2, 3}
set


my=set()
my.add(2)
my
{2}

my.add(2) #set does not have duplicate value
my
{2}

my.update([1,2,3])
my
{1, 2, 3}

my.update({1,2,3}, {1,6,8})
my #update will update more than 1 element at time and add will add 1 element in set
{1, 2, 3, 6, 8}

my.discard(3)
my
{1, 2, 6, 8}

my.pop()
1

my=set("HelloWorld")
my
{'H', 'W', 'd', 'e', 'l', 'o', 'r'}

my.clear()
print(my)
set()

A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B) # | is for union
{1, 2, 3, 4, 5, 6, 7, 8}

A.union(B)
{1, 2, 3, 4, 5, 6, 7, 8}

print(A)
print(B)
{1, 2, 3, 4, 5}
{4, 5, 6, 7, 8}


print(A&B) # & is for intersection
{4, 5}

A.intersection(B)
{4, 5}

print(A-B) # - is for difference
{1, 2, 3}

A.difference(B)
{1, 2, 3}

print(A^B) # ^ is for symmetric difference
{1, 2, 3, 6, 7, 8}

A.symmetric_difference(B)
{1, 2, 3, 6, 7, 8}

print(1 in A) #This shows that sets are iterable
true

my=set("Acropolis")
for letter in my:
  print(letter)
  p
c
r
l
o
i
A
s

my=set("banana")
for letter in my:
  print(letter)
  a
b
n
