# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:53:42 2023

@author: sai
"""
#Advanced Python
#IMP
#list Comprehension
#Code optimization


lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)


#We can write same method using list comprehension.
lst=[num for num in range(0,20)]
print(lst)



names=['sakshi','nisha','pranjal']
lst=[name.capitalize() for name in names]
print(lst)


#List comprehension with if statements
#If statement should be at right side and business logic should 
#be at the left side


def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)


##########################################################
lst=[f"{x}{y}" for x in range(3) for y in range(3)]
print(lst)


#Set comprehension
set={x for x in range(3)}
print(set)


#Dictionary comprehension

dict={x:x*x  for x in range(3)}
print(dict)


#Find all numbers from 1-1000 that are divisible by 7
div7 = [n for n in range(1,1000) if n % 7 == 0]
print(div7)

#Find all of the numbers from 1-1000 that have a 3 in them

num = [n for n in range(1,1000) if '3' in str(n)]
print(num)


#Count the number of spaces in the string
some_string = 'the slow solid squid swan sumptuously through the slimy swamp'
spaces = [s for s in some_string if s == ' ']
print(len(spaces))

##########################################################

#create a list of all consonants in the string
#'Yellow yaks like yelling and yawning and yesterday they yodled while eating yuky yams

sentence = "Yellow yaks like yelling and yawning and yesterday they yodled while eating yuky yams"
result=[letter for letter in sentence if letter not in 'a,e,i,o,u," "']
print(result)
#when string is in one line the output will not include \n


sentence = '''Yellow yaks like yelling and yawning and 
yesterday they yodled while eating yuky yams '''
result=[letter for letter in sentence if letter not in 'a,e,i,o,u," "']
print(result)
#when string is not in one line the output will include \n as a last character.


#Find the common number in two lists without using tuple or set

list_a=[1,2,3,4]
list_b=[2,3,4,5]
common = [i for i in list_a if i in list_b]
print(common)

'''
#IMP
#Get only the numbers in sentence like 'In 1984 there 
were 13 instance of a protest with over 1000 people 
attending

'''
sentence='''In 1984 there 
were 13 instance of a protest with over 1000 people 
attending'''
words = sentence.split()
result=[number for number in words if not number.isalpha()]
print(result)

#The isalpha() method returns true if all the characters 
#are alphabet letters (a-z)

'''Given numbers = range(20), produce a list containing 
the word 'even' if a number in the '''

#in list comprehension if else sholud be at left side 
#and only if should be at the right hand side

result=[]
for n in range(20):
    if n%2==0:
        result.append('even')
    else:
        result.append('odd')
print(result)

#using list comprehension

result=['even' if n%2==0 else 'odd' for n in range(20)]
print(result)


'''
#Produce a list of tuples consisting of only the matching 
numbers in these lists 
list_a=[1,2,3,4,5,6,7,8,9],
list_b=[2,7,1,12] . Result would look like (4,4), (12,12)
'''

list_a=[1,2,3,4,5,6,7,8,9]
list_b=[2,7,1,12] 
result=[(a,b) for a in list_a for b in list_b if a == b]
print(result)

##########################################################

'''
Find all of the words in a string that are less than 4 
letters
'''
sentence = 'On a summer day Ramnath sonar went swimming in the sun and his red skin stung'

examine=sentence.split()
result=[word for word in examine if len(word)>=4]
print(result)

##########################################################
'''
#Write program to print a specified list after removing 
the 0th, 4th and 5th element
'''
color=['Red','Green','White','Black','Pink','Yellow']
color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

#########################################################
'''
Write python program that creates generator function that 
yields cubes of numbers from 1 to n. and accept n from 
user.
'''
def cube_generator(n):
    for i in range(1, n+1):
        yield i ** 3

#Accepting input from the user        
n = int(input("Enter the number:"))
#create the generator object
cubes = cube_generator(n)
#iterate over generator and print the cubes
print("cubes of numbers from 1 to", n)
for num in cubes:
    print(num)
    
#########################################################
'''
Write python program to implement a generator that 
generates random numbers within a given range

'''
import random
def random_number_generator(start, end):
    while True:
        yield random.randint(start, end)
        
#Accept input from the user
start=int(input("Enter start value:"))
end=int(input("Enter end value:"))

#generate the random value
random_numbers=random_number_generator(start,end)
print("Random numbers between",start,"and",end)
for _ in range(5):
    print(next(random_numbers))

'''
[] = 1D 
[[]] = 2D vector
[[[]]] = 3D vector
[[[[]]]] = Tensor


write a program to generate a 3*4*6 3D array whose 
each element is *.

'''
array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

####################################################################################

'''Write a python program to print the numbers of a 
specified list after removing even numbers from it.
'''
num=[7, 8, 120, 25, 44, 20, 27]
num=[x for x in num if x%2!=0]
print(num)


#############################################################

#Assignment
#Sentence matching 

sentence1 = 'Welcome to Data Science Training'
sentence2 = 'Training will be of 5hrs per day'

w1=sentence1.split() 
w2=sentence2.split()

result=[number1 for number1 in w1 for number2 in w2 if number1==number2]
print(result)






















