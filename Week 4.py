# Mutability
fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)
#************************************
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)   # ['a' , 'x' , 'y' , 'd' , 'e', 'f']
#************************************
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)  # ['a' , 'd' , 'e', 'f']
#************************************ # cant do it for a strings that are alone 
#how to do it : 
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was
 #************************************
phrase = "many moons"
phrase_expanded = phrase + " and many stars"
phrase_larger = phrase_expanded + " litter"
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
excited_phrase_complete = phrase_complete[:-1] + "!"
print(phrase_complete)
print(excited_phrase_complete)
#************************************ 
#The Del command 
a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)
#************************************
a = "banana"
b = "banana"

print(a is b)  #True

#************************************
a = [81,82,83]
b = [81,82,83]

print(a is b)  # False

print(a == b)  # True

print(id(a))  #diff than b 
print(id(b))
#************************************
a = [81,82,83]
b = [81,82,83]
print(a is b)  #F

b = a
print(a == b) #T
print(a is b) #T

b[0] = 5
print(a)  # [5,82,83]
#************************************
# cloning lists
a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b) #T
print(a is b) #F

b[0] = 5

print(a) #same not changed
print(b) # changed 
#************************************
# Methods on Strings and Lists 
mylist = []
mylist.append(5) 
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)  #[5,27,3,12]

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12)) # [5 , 12 , 27 , 3 , 12]

print(mylist.index(3))   #3
print(mylist.count(5))   #1

mylist.reverse()
print(mylist)   #[ 12 ,3,27,12 , 5]

mylist.sort()
print(mylist)   #[3 ,5, 12 , 12 , 27 ]  

mylist.remove(5)
print(mylist)   #[3 , 12 , 12 , 27]

lastitem = mylist.pop()
print(lastitem) #27
print(mylist) #[ 3 , 12 , 12] 
#***************************************
origlist = [45,32,88]
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list before changes
newlist = origlist + ['cat']
print("newlist:", newlist)
print("the identifier:", id(newlist))              #id of the list after concatentation
origlist.append('cat')
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list after append is used
#***************************************
ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)
#***************************************
ss = "    Hello, World    "

els = ss.count("l") #3
print(els)

print("***"+ss.strip()+"***") # ***Hello World***

news = ss.replace("o", "***") #Hell*** w***rld 
print(news)
#***************************************
#format statment 
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))
#****
person = input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)
#****
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)

#*************************************** 
#The Accumulator Pattern with Lists 
nums = [3, 5, 8]
accum = []
for w in nums:
    x = w**2
    accum.append(x)
print(accum)    # [ 9 , 25 , 64 ] 
#*************************************** 
#The Accumulator Pattern with Strings 
s = input("Enter some text")
ac = ""
for c in s:
    ac = ac + c + "-" + c + "-"

print(ac)  # c-c-a-a-t-t 
#*************************************** 

