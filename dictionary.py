my_dict={1:"shruti",2:"tiwari"}
print(my_dict)
{1: 'shruti', 2: 'tiwari'}

my_dict={"fist_name":"shruti","last_name":"tiwari","hobby":["football","cricket"]}
print(my_dict["hobby"])
['football', 'cricket']

my_dict=dict({1:"shruti",2:"tiwari"})
print(my_dict)
{1: 'shruti', 2: 'tiwari'}

my_dict=dict([(1,"shruti"),(2,"tiwari")])
print(my_dict)
{1: 'shruti', 2: 'tiwari'}

my_dict=dict([(1,"shruti"),(2,"tiwari")])
my_dict["age"]=20
print(my_dict)
{1: 'shruti', 2: 'tiwari', 'age': 20}

my_dict={1:"shruti",2:"tiwari",5:"name"}
print(my_dict.pop(5))
print(my_dict)
print(len(my_dict))
name
{1: 'shruti', 2: 'tiwari'}
2
x = my_dict.values()
print(x)
y= my_dict.keys()
print(y)
dict_values(['shruti', 'tiwari', 'CS', 20])
dict_keys([1, 2, 'Field', 'age'])
x= my_dict.get(1)
print (x)
x= my_dict.keys()
print (x)
my_dict["Field"]="CS"
my_dict["age"]=20
print (x)
print(my_dict)
shruti
dict_keys([1, 2, 'Field'])
dict_keys([1, 2, 'Field', 'age'])
{1: 'shruti', 2: 'tiwari', 'Field': 'CS', 'age': 20}
my_dict={1:"shruti",2:"tiwari",5:"name"}
print(my_dict.popitem())
print(my_dict)
(5, 'name')
{1: 'shruti', 2: 'tiwari'}
my_dict={1:"shruti",2:"tiwari",5:"name"}
my_dict.clear()
print(my_dict)
{}
my_dict={1:"shruti",2:"tiwari",5:"name"}
del my_dict
my_dict={1:"shruti",2:"tiwari",5:"name"}
for i in my_dict.values():
  print(i)
shruti
tiwari
name

my_dict={1:"shruti",2:"tiwari",5:"name"}
for i in my_dict.keys():
  print(i)
1
2
5
my_dict={1:"shruti",2:"tiwari",5:"name"}
for i in my_dict.keys():
  print(i ," : ",my_dict[i])
1  :  shruti
2  :  tiwari
5  :  name
my_dict={1:"shruti",2:"tiwari",5:"name"}
for x, y in my_dict.items():
  print(x," : ", y)
1  :  shruti
2  :  tiwari
5  :  name
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
li=[1,2,3,4,5]
myDict = {x: x**3 for x in li}
print (myDict)
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
