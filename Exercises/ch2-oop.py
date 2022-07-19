# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:11:56 2022

@author: seyma
"""

#  Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.

class Flower:
    def __init__(self,name="daisy",n_petals=7,price=13.00):
        self._name=name
        self._n_petals=n_petals
        self._price=price
    
class Rose(Flower):
    def __init__(self,name="rose",n_petals=10,price=50.00):
        self._n_petals=n_petals*3
        
X=Flower("rose",23)
Y=Rose()
print(X._price)
print(X._n_petals)
print(Y._n_petals)

# R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment
# methods of the CreditCard class to ensure that the caller sends a number
# as a parameter

balance=150  #setted value
def make_payment(amount):
    global balance
    try:
        balance-=amount
    except TypeError:
        print("Amount should be a number")

make_payment("abc")
print(balance)


        
# R-2.12 Implement the mul method for the Vector class of Section 2.3.3, so
# that the expression v 3 returns a new vector with coordinates that are 3
# times the respective coordinates of v.
# R-2.13 Exercise R-2.12 asks for an implementation of mul , for the Vector
# class of Section 2.3.3, to provide support for the syntax v 3. Implement
# the rmul method, to provide additional support for syntax 3 v.
class Vector:
    def __init__ (self, d):
        if type(d) is int:
            self. coords = [0] *d
        elif type(d) is list:
            self. coords = [0] *len(d)
            for i in range(len(d)):
                self.coords[i]=d[i]
        
    
    def __setitem__(self,j,val):
        self.coords[j]=val
        
    def __getitem__ (self, j):
        return self. coords[j]

    def __len__(self):
        return len(self.coords)
    
    def __mul__(self,k):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j]=self[j]*k
            print(result[j])
        return result
    

    def __add__ (self, other):
        if len(self) != len(other): # relies on len method
            raise ValueError( "dimensions must agree" )
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __radd__(self,other):
        if len(self) != len(other): # relies on len method
            raise ValueError( "dimensions must agree" )
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __rmul__(self,k):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j]=self[j]*k
        return result
        
    def __str__ (self):
        return "<" + str(self. coords)[1:-1] + ">"

# v=Vector(2)
# v[1]=5
# u=Vector(2)
# u[0]=-1
# # z=v-u
# z=2*v
# a=[0,3]+z
# print (a)

x=Vector([1,2])
print(x)

# C-2.24 Suppose you are on the design team for a new e-book reader. What are the
# primary classes and methods that the Python software for your reader will
# need? You should include an inheritance diagram for this code, but you
# do not need to write any actual code. Your software architecture should
# at least include ways for customers to buy new books, view their list of
# purchased books, and read their purchased books.
"""
class 
    e-book
fields
    _account
    _password
    _mylibrary
    _bookstore
behaivours
    get_account()
    check_password()--??
    get_mylibrary()
    open_bookstore()--buralarda hep "get" mi olması lazım
    
    open_book()--mylibrary de olması lazım
    buy_book()--connection to the bank?? field da bir şey oluşturup bağlantı mı olmalı?

"""


# C-2.31 Write a Python class that extends the Progression class so that each value
# in the progression is the absolute value of the difference between the previous two values. You should include a constructor that accepts a pair of
# numbers as the first two values, using 2 and 200 as the defaults.
# C-2.32 Write a Python class that extends the Progression class so that each value
# in the progression is the square root of the previous value. (Note that
# you can no longer represent each value with an integer.) Your constructor should accept an optional parameter specifying the start value, using
# 65,536 as a default.
import math as m
class Progression:
    def __init__ (self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1
    
    def __next__ (self):
        if self._current is None: # our convention to end a progression
            raise StopIteration( )
        else:
            answer = self._current # record current value to return
            self._advance( ) # advance to prepare for next time
            return answer # return the answer

    def __iter__ (self):
        return self

    def print_progression(self, n):
        print(" ".join(str(next(self)) for j in range(n)))
        
class absProgression(Progression): 
    def __init__(self,first=2,second=200):
        super().__init__(first)
        self._next=second
    def _advance(self):
        self._current,self._next=self._next,abs(self._current-self._next)
                     
class sqrProgression(Progression):
    def __init__(self,start=4):   
        self._current = start
        
    def _advance(self):
        self._current=m.sqrt(self._current)    


x=Progression(4)
x.print_progression(8)   
y=absProgression()
y.print_progression(15)
z=sqrProgression(6.47)
z.print_progression(5)







