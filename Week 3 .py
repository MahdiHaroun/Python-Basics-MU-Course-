print(True)
print(False)
print(type(True))
print(type(False))
print(5==5)
print(5==6) 
print(type(True))
print(type("True"))
print(5 == 5)
print(5 == 6)
#******************************************************
x=5 
print(x>0 and x<10 ) #T
n=25
print(x%2 == 0 or n%3 ==0)#F
#******************************************************
#The in and not in operators 
print('p' in "apple") # T
print('i' in "apple") # F
print('ap' in "apple")# T
print('pa' in "apple")#F
print('a' in 'a')  # T
print('apple' in 'apple') # T
print('' in 'a')  #T
print('' in "apple") #T 
print ('x' not in 'apple ') #T
print ('a' in ["madhi" , "suiii" , "apple" , "appp"]) #F
#******************************************************
# The conditional Execution 
x = 15
if x %2 == 0 :
    print ( x , "is even")
else : 
    print (x , "is odd")
#******************************************************
x = 10 
if x < 0 : 
    print ("the negative number " ,  x , " is not valid here") 
print("this always will be printed")

x= 10 
y = 10 
if(x<y):
    print (" x is less than y ")
else : 
    if (x>y) :
         print ("x is greater than y") 
    else : 
        print("x and y must be equal")

#******************************************************
# The Accumulator Pattern With Conditionals and Accumulating a Maximum Value 
phrase = "what a wonderful day to program"
tat = 0 
for char in phrase : 
    if char != " " : 
        tat = tat+1 
print (tat) 

s= "what if we went to the zoo"
x=0 
for i in s : 
    if i in ['e' , 'a' , 'i' , 'o' , 'u'] :
        x+=1 
print (x) 
#to compute the max value 
nums = [ 9 , 3 , 8 , 11 , 5 , 29 , 2 ]
best_num = nums [0]
for n in nums : 
    if n > best_num : 
        best_num = n 
print (best_num)

 
