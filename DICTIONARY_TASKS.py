# Write a Python script to add a key to a dictionary. Go to the editor
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

'''a={0: 10, 1: 20}
a.update({2:30})
print(a)'''
    
'''a={0: 10, 1: 20}
b={}
for row,col in a.items():
    row=row+1
    col=col+10
    b.update({row:col})
print(b)'''

# Concatenate

'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
    print(d)
'''

# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''a=int(input("Number of Data:-"))
b={}
for row in range(1,a+1):
    key=row
    value=key*key
    diction={key:value}
    b.update(diction)
print(b)'''

#  Write a Python program to sum all the items in a dictionary
'''a={0: 10, 1: 20}
b=0
for row in a.values():
    b+=row
print(b)'''

# Write a Python program to sum all the items in a dictionary
'''a={0: 10, 1: 20}
b=1
for row in a.values():
    b*=row
print(b)'''

# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
'''a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

for row in a.values():
    five=row[4]
    print(five)'''

# Write a Python program to count number of items in a dictionary value that is a list
'''a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19,20],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29,30],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39,40]}
c=0
for row in a.values():
    b=len(row)
    c+=b
print(c)'''

# Task:-
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
# Count sum of values:-
'''a =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for row in a.values():
    for col in row:
        count+=1
print("Number of Values:->",count)'''

# Create Name and Id in Dictionary:-
'''
collection={'Name':[],'Department':[]}
for row in range(2):
    Name=input("Enter Your Name:-")
    Department=input("Enter Your Department:-")
    collection['Name'].append(Name)
    collection['Department'].append(Department)
print(collection)'''



# Create Name and Age In Dictionary:-
'''
header=['Name','Age']
output={}
for serial_number,details in enumerate(header):
    output[details]=[]
    
Total_Numbers_student=int(input('Enter Your Number Count:-'))
for row in range(Total_Numbers_student):
    a=input('Enter Your Name:-')
    b=int(input("Enter Your age:-"))
    output['Name'].append(a)
    output['Age'].append(b)
    
print(output)
'''

