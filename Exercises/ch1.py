#Chapter 1. Python Primer


# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.
def is_multiple(n,m):
    if n%m==0:return True
    else: return False
print(is_multiple(5,3))
print(is_multiple(6,3))
print(is_multiple(3,6))
print ("ok")

# R-1.2 Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.
def is_even(k):
    if k>0:
        while k>0:
            k=k-2
    elif k<0:
        while k<0:
            k=k+2
    # if k==0 return True  else return False
    # if k==0: return True
    # else: return False
print(is_even(3))
print(is_even(6))
print(is_even(-3))
print(is_even(-6))

"""KİTAPTAKİ ÖRNEK
def factors(n): # generator that computes factors
    k=1
    while k* k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k* k == n: # special case if n is perfect square
        yield k
    
print(factors(130))"""


# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.
def minmax(data):
    min_e=data[0]
    max_e=data[0]
    for num in data:
        if num<min_e: min_e=num
        if num>max_e:max_e= num

    return (min_e,max_e)
print (minmax((3,53,8,3,1,2,3,65,32,1,496,321,5)))

# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.
def sum_squares(n):
    current_int=n-1
    sum=0
    for i in range(current_int):
        sum+=current_int**2
        current_int=current_int-1        
    return sum
print(sum_squares(13))

# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?
for i in range(50,90,10):
    print (i)

# R-1.12 Pythonâs random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.
import random as rnd
print(rnd.choice([0,300,5,6,24,524,6523562]))
# randrange
cont=[0,300,5,6,24,524,6523562]
print(cont[rnd.randrange(len(cont))])

# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.
def reverse_list(list_1):
    for i in range(len(list_1)-1,-1,-1):
        yield (list_1[i])

list_x=[4,6,8,2]
print(reverse_list(list_x))


# C.1.17
def scale(data, factor):
    for val in data:
        val *= factor
        print(val)
        yield val       
# def scale(data, factor):
#     for j in range(len(data)):
#         data[j] *= factor
#     return data        
print(list(scale([5,3,6],2)))

# C-1.19 Demonstrate how to use Pythonâs list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

x="a"
print(ord(x))
k=0
for k in range(ord("a"),ord("z")):
    print(k)
while k<3:
    k+=1
    y=ord(x)>>1
    print(y)

# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] Â· b[i], for i = 0,...,nâ1.
def dot_prod(array1,array2):
    n= len(array1)
    c=[0]*n
    for i in range(n):
        c[i] = array1[i] * array2[i]
    return c

array1=(0,2,3)
array2=(3,1,3)
print (dot_prod(array1,array2))

#  Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# âDonât try buffer overflow attacks in Python!â
def find_index(list1,index):
    try: return list1[index]
    except IndexError:
        print("Donât try buffer overflow attacks in Python!")
    
liste=[0,1,2,3,4,5,6]
find_index(liste,7)



# P-1.29 Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.
cha=["c","a","t","d" , "o" , "g"]
all_words=[]
for i in range(len(cha)):
    word=[None]*(i+1)
    word_sm_l=[word]*len(cha)**(i+1)
    for i in range(len(word_sm_l)):
        for j in range(len(word_sm_l[i])):
            word_sm_l[i][j]=cha[(i//len(cha)**j)%len(cha)]
        print("".join(word_sm_l[i]))

# P-1.32 Write a Python program that can simulate a simple calculator, using the
# console as the exclusive input and output device. That is, each input to the
# calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output
# to the Python console what would be displayed on your calculator.
x=input("write the equation")
print(eval(x))
"""P-1.33 Write a Python program that simulates a handheld calculator. Your program should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each operation is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation"""

# P-1.34 A common punishment for school children is to write out a sentence multiple times.
 # Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the sentences and it should
# make eight different random-looking typos.
import random as rnd
for i in range(100):
    types=[" I will never spam my friends again.",
           " I will never spam my best friends again.",
           " I will neverrr spam my friends again.",
           " I will never spam my friends.",
           " I won't spam my friends again.",
           " I will never spam my friend again.",
           " I will never spam my friends again.",
           " I will never spam my friends again:)"]
    print(str(i)+types[rnd.randint(0, 7)])
    

# P-1.35 The birthday paradox says that the probability that two people in a room
# will have the same birthday is more than half, provided n, the number of
# people in the room, is more than 23. This property is not really a paradox,
# but many people find it surprising. Design a Python program that can test
# this paradox by a series of experiments on randomly ggenerated birthdays,
# which test this paradox for n = 5,10,15,20,...,100
person_group=[]
for i in range(100):
    person_group.append(rnd.randint(1, 366))

if len(set(person_group))<len(person_group):
    print("paradox")
else:
    print("Nothing")
    
import random as rnd
print(rnd.seed(5))
rnd.randint(5,100)




