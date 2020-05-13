#Strings
mystring = "abcdefghij"

# SLICING
print(mystring.split('W'))

username = "Sammy"
color = 'blue'
print("The {} favorite is {}".format(username,color))

#Lists
mylist = ['a','b','c','d','e']
mylist.append('z')
mylist.insert(0, 'Z')
mylist.pop(0)
print(mylist)

mylist1 = [0,1,2]
mylist2 = [3,4,5]
mylist3 = [6,7,8]

mega_list = [mylist1,mylist2,mylist3]
print(mega_list)

#Dictionaries
salaries = {'John': 20, 'Sally': 30, 'Sammy': 15}
salaries['Cindy'] = 100
salaries["john"] = salaries["John"] + 40
print(salaries['Sally'])

#TUPLES
t = (1,2,3)
mylist = [1,2,3]
print(mylist)

# SETS
myset = set()
print(myset)
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(3)
myset.add(3)
print(myset)