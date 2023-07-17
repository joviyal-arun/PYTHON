# 1) Write a Python program to calculate the length of a string.
'''a=input("Enter Your Name")
b=a.split()
count=0
for row in b:
    for column in row:
        count+=1
print(count)'''

# 2) Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself
'''a='restart'
b=a[0]
c=a.replace(b,'$')
print(type(c))
d=b+c[1:]
print(d)'''


# 3) separated by a space and swap the first two characters of each string
'''a='abc'
b='xyz'
c=b[2:]; e=a[:-1]; output=e+c; print(output)
f=b[:-1]; g=a[-1]; out=f+g; print(out)'''

# 4) Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
'''a=input('enter Your String')
b=len(a)
c='ing'
d='gly'
if(b<=6):
    if(a[-1]=='g' and a[-2]=='n' and a[-3]=='i'):
        e=a[:-1]
        out=e+d
        print(out)
    else:
        out=a+c
        print(out)'''

# 5) Write a Python function that takes a list of words and returns the length of the longest one
'''
a=["PHP", "Exercises", "Backend"]
b=[]
for row in a:
    b.append((len(row),row))
b.sort()
print(b)
c=b[-1][-1]
print(c)'''

# 6) Write a Python program to remove the nth index character from a nonempty string.
'''a=input("Enter Your String")
b=int(input("Index of String"))
first_part = a[:b] 
last_part = a[b+1:]
print(first_part)
print(last_part)
output=first_part+last_part
print(output)'''

# 7) Python program to remove the characters which have odd index values of a given string
'''a=input("Enter Your Data:-")
b=len(a)
d=''
for row in range(0,b):
    if(row%2==0):
        d=d + a[row]
print(d)'''

# 8) Write a Python program that accepts a comma separated sequence of words form (alphanumerically).
'''a=input("Enter Your Data:-")
b=a.split()
c=[]
for row in b:
    c.append(row)
c.sort()
print(c)'''

# 9) Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)
'''a=input("Enter Your String:-")
b=a[-2:]
c=len(b)
if(c<=2):
    d=b*4
    print(d)'''

# 10) Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string
'''a=input("Enter Your Data:-")
c=len(a)
if(c>3):
    b=a[:3]
    print(b)'''

# 11) Write a Python function to reverse a string if it's length is a multiple of 4.
'''a=input("Enter Your Data:-")
b=len(a)
if(b%4==0):
    output=''.join(reversed(a))
    print(output)
else:
    print("Your Data Lenght is Minimum Three",a)'''

# 12) Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
'''a=input("Enter Your Data:-")
b=a[:4]
count=0
for row in b:
    if row.upper() in row:
        count+=1
    if (count<=2):
        output=a.upper()
    else:
        output=a
print(output)'''

# 13) Count and display the vowels of a given text
'''a=input("Enter Your Data:-")
b=a.split()
c=["a","e","i","o","u"]
count=0
output=''
for row in b:
    for column in row:
        if column in c:
            count+=1
            output=output + column
print("Vowel Letter From Given Letter:-",output)
print("Vowels Count in Given String:-",count)'''

# 14) Count the Character From the input:-
'''a=input("Enter Your Data:-")
b=input("Which SIngle Character You Want To Find it?")
count=0
for row in a:
    if(row==b):
        count+=1
print(count)'''

# 15) Write a Python program to compute sum of digits of a given string.
'''a=input("Enter Your Data:-")
summing=0
for row in a:
    if row.isdigit():
        b=int(row)
        summing+=b
print(summing)'''

# 16) Write a Python program to find smallest and largest word in a given string.
'''a=input("Enter Your Data:-")
b=a.split()
output=[]
for row in b:
    c=len(row)
    output.append((c,row))
output.sort()   
print("You smallest Word is",output[0][1])
print("You Largest word is",output[-1][1])'''

# 17) Write a Python program to count characters at same position in a given string (lower and uppercase characters) as in English alphabet.
'''a=input("Enter Your Data:-")
b=len(a)
count=0
for i in range(b):
    if((i==ord(a[i])- ord('a')) or (i==ord(a[i])-ord('a'))):
        count+=1
print(count)'''

# 18) Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
'''a=input("Enter Your Data:-")
count_digit=0
count_upper=0
count_lower=0
cout_special_character=0
for row in a:
    if(row.isdigit()):
        count_digit+=1
    elif(row.isupper()):
        count_upper+=1
    elif(row.islower()):
        count_lower+=1
    else:
        cout_special_character+=1
print(count_digit," Digits present in the given Data ")
print(count_upper," Upper Character present in the given Data ")
print(count_lower," Lower Character present in the given Data ")    
print(cout_special_character,"Special Character Present in the given Data")'''       

# 19) Write a Python program to count the number of characters (character frequency) in a string.
'''str1='google.com'
dict = {}
for n in str1:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print(dict)'''   


# 20 Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

'''a='The lyrics is not that poor!'
snot=a.find('not')
spoor=a.find('poor')
if spoor>snot and snot>0 and spoor>0:
    out=a.replace(a[snot:spoor+5],'good')
    print(out)'''

# 21 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
'''a=(input("Enter Your String:-"))
a=str(a)
b=len(a)
c=a[0:2]
d=a[-2:]
if(b>2):
    output=str(c)+ str(d)
elif(b==2):
    output=c+c
else:
    output=''
print(output)'''

# 22 
'''str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])'''

# 23 Convert a string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters
'''a='Python'
b=a[:4]
count=0
for row in a:
    if row.isupper():
        count+=1
if count>=2:
    c=a.replace(a,'PYTHON')
    print(c)
else:
    print (a)'''

# 24 input --> arun was born in sivakasi  output --> Arun Was Born In Sivakasi

'''a='arun was born in sivakasi'

splitting=a.split(' ')
output=''
full_sentense=' '

for row in splitting:
    first_char=row[0]
    upper_case=first_char.upper()
    replacing=row[0].replace(first_char,upper_case)
    final=replacing+row[1:]

    output=final+' '
    full_sentense+=output

print(full_sentense)'''

# 25 Swap cases of a given string
'''
a='Python'
b=''
for row in a:
    if row.isupper():
        b+=row.lower()
    else:
        b+=row.upper()
print(b)
'''

# 26 To find smallest and largest word in a given string
'''
input_data='Write a Java program to sort an array of given integers using Quick sort Algorithm'
splitting=input_data.split(' ')
storage=[]
for row  in splitting:
    storage.append((len(row),row))

storage.sort()
print(storage[0][-1],':-is smallest Letter in the given data')
print(storage[-1][-1],':-is smallest Letter in the given data')'''

#27  Count characters at same position in a given string as in English alphabet
'''
str1='xbcefg'
count_chars=0
for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
print(count_chars)'''

#28 Converting Small Letter to Captial Letter:-
'''
def converting_captial_letter(a):
    output=''
    for i in a:
        for j in range(97,122):
            if(ord(i)==j):
                sample=j-32
                output+=chr(sample)
    print(output)

a=input("Enter Your Small Letter Data:-")
converting_captial_letter(a)

'''
# 29 Converting Small Letter to Captial Letter squence of Letter:-
'''
def converting_multiple_squence_captial_letter(a):
    b=a.split()
    empty_string=''
    for row in b:
        string=' '
        for col in row:
            for i in range(97,122):
                if(ord(col)==i):
                    sample=i-32
                    empty_string+=chr(sample)
        empty_string+=string
    print(empty_string)

a='arunachalam was born in sivakasi'
converting_multiple_squence_captial_letter(a)
'''

# 

                
