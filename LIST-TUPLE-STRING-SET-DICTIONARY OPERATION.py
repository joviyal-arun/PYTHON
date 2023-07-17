# list Operation:-
'''
a=[1,2,4,5,6,7]
b=[9]

a.append(8)  # Append

a.insert(2,'arun') # Insert

a.extend(b) # Extend input must be input

b=len(a) # count how many element present

a.remove('arun') # Removing Particular element

a.sort() # Ascending order

a.reverse() # Decending Order

a=['arun','mahesh','viki']

del a[-1] # Deleting an element by its position

a.remove('arun') # Removing an item by its value or data

b=a.pop() # pop mean get the value from the list .pop() last item will be pop

c=a.pop(-1) # pop(0) means first item will be pop

colors = ['Red', 'Blue', 'Green', 'Black', 'White']

first_three=colors[:3]

middle_three=colors[1:3]

last_three=colors[-3:]


'''

# Tuple Operation:-

'''
a=(7,8,4)

b=(9,10)

c=a+b # Concatenate a & b 

print(a[0:2]) # Slicing

print(a.count(7)) # Counting 

'''

# String Operation:-
'''
a='arun_meena_rajan'

b=len(a) # Find String Length

for row in range(0,b): # Accessing the string element 
    c=a[row]
    if 'a' not in c: # Membership operation
        print(c)

c='arun'

d=a+c # Concatenate Two String
'''

# Sets Operation:-
'''
a={1,2,3,4,5,6} # Create an Sets:-
b={6,7,8,9}

c=a.discard(5)    # Remove Data From Sets

d=(a|b)      # Adding Two Sets Using Union Operator(|)

e=(a&b)      # Intersection of Two Sets (&)

f=a-b # Difference Between Two Sets But Before It will be Taken Intersection Operation perform

g= a^b # Symmetric Element From The Two Sets 

h=a.update([100]) # Adding more element to the sets

i=a.pop() # Removing first index position data

j=a.discard(7)  # 7 data discard from the sets

k=a.add('arun') # Adding one element to sets
'''

# Dictionary:-

a={1:'vijay,super',2:'ajith',3:'suriya',4:'dhanush',5:'vijaysethupathi'} # Create an Dictionaries

a[6]='vikram' # Append the data to the dictionaries:-

# a.popitem() # Remove the last key and value from the dictionaries

# a.clear() # Clear All the data in the dictionaries final dictionaries will be empty

# del a[1] # delete the data from the dictionaries

a.update({'dhanush':41}) # Update data into the dictionaries
print(a)


'''for row in a: # Key only Print in the dictionaries:-
    print(row)'''

'''for row in a.values(): # Value only print in the dictionaries:-
    print(row) '''

'''for row in a.items(): # Both Key and Value print in the dictionaries:-
    print(row)'''

'''for key,value in a.items(): # Both Key and Values print in the dictionaries with different Variable
    print(key,value)'''


# Dictionaries example:-

# How to create Dictionaries using for loop:-

'''

import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

dictionaries={}
a=int(input("How many Data Create to the Dictionaries:-"))

for row in range(0,a):

    b=input("Enter Your Key Data must be String:-")
    c=int(input("Enter Your Dictionaries Data  must be integers':-"))
    dictionaries[b]=c

'''









    
        

    






