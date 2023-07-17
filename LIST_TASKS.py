# 1) Python program to sum all the items in a list:-

'''a=[1,2,3,4]
b=len(a)
output=0'''

# This is One Method:-
'''for row in range(0,b):
    output+=a[row]
print(output)'''

# Another Method:-

'''for row in a:
    output+=row
print(output)'''

# 2) Python program to multiplies all the items in a list 

'''    
a=[1,2,3,4]
output=1

for row in a:
    output*=row
print(output)
'''

# 3) Python program to get the largest number from a list.

'''lists=[1,5,8,16,4,5]
first_element=lists[0]
for total in lists:
    if(total > first_element):
        first_element=(total)
print(first_element)'''


# 4) Count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

'''input_words=['aruna','viiv','mahi','mahesh','naveen']
count=0
for words in input_words:
    if(len(words)>1) and (words[0]==words[-1]):
        count+=1
print(count)'''


# 5)Given List is empty or Not:-
'''
a=[]
if not a:
    print("Your are empty data:")
else:
    print("some data are present")
'''   
# 6) How many even number and odd number in the list:-
'''
a= (1, 2, 3, 4, 5, 6, 7, 8, 9)
b=list(a)
odd=[]
even=[]
for row in b:
    if(row%2==0):
        even.append(row)
    else:
        odd.append(row)

evens=0
for even_number in even:
    if(even_number>0):
        evens+=1
print('Number of  even number is:-',evens)
odds=0
for odd_numbers in odd:
    if(odd_numbers>0):
        odds+=1
print('Number of  Odd number is:-',odds)
'''
# 7) Write a Python program to find the list of words that are longer than n from a given list of words.
'''
a=input("Enter Your Data")
b=a.split(" ")
c=3
e=[]
for row in b:
    d=len(row)
    if(d>c):
        e.append(row)
print(e)
'''

# 8) Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
'''a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
c=[]
for row in a:
    b=len(row)
    if(b==5):
        c.append(row)
print(c)'''

# 9) Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30
'''c=[]
a=int(input("Enter Your value:-"))
for row in range(1,a):
    b=row*row
    c.append(b)
print(c[5:])'''

# 10 ) Difference between normal and format string:-
'''import time
starting_time=time.time()
for row in range(1,11):
    c=row*2
    b="{} * 2= {}".format(row,c)
    print(b)
ending_time=time.time()
execution_time=ending_time-starting_time
print("Your Pogram taking is",execution_time)'''

# 11) For Normal program
'''import time
starting_time=time.time()
for row in range(1,11):
    print(row,"*2=",row*2)
ending_time=time.time()
execution_time=ending_time-starting_time
print("Your Program taking is",execution_time)'''

# 12) Ascending Order from the name list:-
'''a=['viki','yuvi','mahesh','arun','siva','abi']
output=[]      
for row in range(97,122):
    for col in a:
        b=col[0]
        if(b==chr(row)):
            c=chr(row)+col[1:6]
            output.append(c)
print(output)'''

# 13) Extend the List:-
'''a= [10, 20, 30]
b= [40, 50, 60]
b.extend(a)
print(b)'''

# 14) ZIP function model Program:-
'''a=['arun','mahesh','viki','shiva']
b=[1,2,3,4]
for (row,col) in zip(a,b):
    print(row,col)'''
     

# 15) Form emp1,emp2,emp3
'''a=[1,2,3]
for row in a:
    print("emp{}".format(row))'''

# 16) Create 5 Empty Dictionaries in list:-
'''a=5
b=[{} for row in range(0,a)]
print(type(b))'''

# 17) Concate Full list
'''color = ['red', 'green', 'orange']
b=''
for row in color:
    b+=row
print(b)'''

#18)
'''list1 = ['1','2','3','4']
print(list1[0])
s = "-"
c=s.join(list1)
print(c[0])'''

#19

'''word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for row in range(97,122):
    for col in word_list:
        b=col[0]
        if(chr(row)==b):
            print(b)
            print(col)'''
'''

class family():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)
        
a=input("Enter Your Name:-")
b=int(input("Enter Your Age:-"))
obj=family(a,b)
obj.display()
'''
'''import time
starting_time=time.time()
for row in range(2,8):
    for col in range(1,11):
        output=row*col
        print('{}*{}={}'.format(col,row,output))
    print()
ending_time=time.time()
execution_time=ending_time-starting_time
print("Your Program taking is",execution_time)'''

'''import time
starting_time=time.time()
for row in range(2,8):
    for col in range(1,11):
        output=row*col
        print(col,'*',row,'=',output)
    print()
ending_time=time.time()
execution_time=ending_time-starting_time
print("Your Program taking is",execution_time) ''' 

# Write a Python program to concatenate elements of a list.
'''color = ['red', 'green', 'orange']
b=' '.join(color)
print(b)'''


# Write a Python program to replace the last element in a list with another list. 
'''a=[1, 3, 5, 7, 9, 10]
b=[2, 4, 6, 8]
a[-1:]=b
print(a)'''

# Callabrate on it.
'''a=[11, 33, 50]
b=''
for row in a:
    b+=str(row)
print(int(b))'''

# Remove Duplicate number in an list:-
'''a=[2,4,6,2,8,10]
b=[]
for row in a:
    if row not in b:
        b.append(row)

print(b)'''

# Split a list based on first character of word
'''word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

output_word_list=[]

for row in range(97,123):
    for col in word_list:
        selecting=col[0]
        if(chr(row)==selecting):
            output_word_list.append((col))

print(output_word_list)'''

