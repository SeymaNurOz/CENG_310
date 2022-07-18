# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:05:43 2022

@author: seyma
"""

# R-6.1 What values are returned during the following series of stack operations, if
# executed upon an initially empty stack? push(5), push(3), pop(), push(2),
# push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(),
# pop(), push(4), pop(), pop().
"""5"""

# R-6.2 Suppose an initially empty stack S has executed a total of 25 push operations, 12 top operations, and 10 pop operations, 3 of which raised Empty
# errors that were caught and ignored. What is the current size of S?-->18

# R-6.3 Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, so that the element that starts at the top
# of S is the first to be inserted onto T, and the element at the bottom of S
# ends up at the top of T.

def  transfer(S, T):
    while len(S)>0:
        x=S.pop()
        T.append(x)
    
S=[4,5,6,25151,51,8,4,51,5,3]
T=[]
transfer(S, T)
# print(T)

# P-6.35 The introduction of Section 6.1 notes that stacks are often used to provide
# “undo” support in applications like a Web browser or text editor. While
# support for undo can be implemented with an unbounded stack, many
# applications provide only limited support for such an undo history, with a
# fixed-capacity stack. When push is invoked with the stack at full capacity,
# rather than throwing a Full exception (as described in Exercise C-6.16),
# a more typical semantic is to accept the pushed element at the top while
# “leaking” the oldest element from the bottom of the stack to make room.
# Give an implementation of such a LeakyStack abstraction, using a circular
# array with appropriate storage capacity. This class should have a public
# interface similar to the bounded-capacity stack in Exercise C-6.16, but
# with the desired leaky semantics when full

class Empty(Exception):
    pass

class Stack():
    def __init__(self):
        self._st=[]
        
    def __len__(self):
        return len(self._st)
    
    def isempty(self):
        return len(self._st)==0
        
    def push(self,element):
        self._st.append(element)
        
    def pop(self):
        if self.isempty():
            raise Empty("Stack is empty")
        else:
            return self._st.pop()
            
    def top(self):
        if self.isempty():
            raise Empty("Stack is empty")
        else:
            return self._st[-1]



class LeakyStack(Stack):
    def __init__(self,capacity):
        self._st=[]
        self.capacity=capacity
        
    # def __len__(self):
    #     return len(self._st)
        
    def isfull(self):
        return self.capacity==len(self._st)

    def push(self,element):
        if self.isfull():
            self._st=self._st[1:]
        

        self._st.append(element)
        
    
LS=LeakyStack(3)
LS.push(1)
LS.push(2)
LS.push(3)
LS.push(4)
print(LS.isempty())
print(LS.isfull())
print(LS.pop())
print(LS.pop())
print(LS.isfull())
print(LS.pop())
# print(LS.pop())

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    