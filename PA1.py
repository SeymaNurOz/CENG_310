# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:39:35 2022

@author: seyma nur oz

"""

"""
Task 1
A stone is attached to a string and rotated with the help of the string in a horizontal circle of radius. In
this task, you are given the weight of the stone (m), the speed of the string (v), and the radius of the
horizontal circle (r) as arguments to the function tensionCalculator(m, v, r). Return the tension applied
to the string. You can use the following formula to calculate the tension in the string:
T ension = m ∗ v^2/r 

Specifications:
• The arguments will be in the following order: weight (float), speed (float) and radius (float).
• The return value will be a float.
• You cannot use conditional statements, loops, etc.
• Your function must have the same name and must preserve the order of arguments for us to grade
without any trouble
Sample Input:
>>> tensionCalculator(3.0, 5.0, 2.0)
Sample Output:
37.5
"""

### TASK1

def tensionCalculator(m, v, r):
    tension=m*v**2/r
    return tension

"""
Task 2
In this task, you need to define a function named deleteConsecutiveSimilar(integerList) which takes list of
lists that contains integers. In the function you need to delete consecutive lists if both lists share at least
one common integer. This procedure should continue until there is no two consecutive lists that share a
common element. The function should return the remaining list.

For Example:
If input list is [[2,5,10],[2,-1],[3]]
The lists [2,5,10] and [2,-1] gets eliminated
Input list becomes [[3]]
If input list is [[2,5,10],[7,-1],[3,-1],[2,0]]
In the first step lists [7,-1] and [3,-1] gets eliminated
In the second step lists [2,5,10] and [2,0] gets eliminated
Input list becomes []
If input list is [[2,5,10],[7,-1],[3,-1],[2,0],[-5,0]]
Input list becomes [[2,5,10]]
"""

### TASK2

def deleteConsecutiveSimilar(integerList):
    l=len(integerList)
    k=0   
    while k<l:
        k+=2
        
        pop_indexes=[]
        for i in range(len(integerList)):
            for integer in integerList[i]:
                control_int=integer            
                if i == len(integerList)-1:pass
                else:
                    for ints in integerList[i+1]:
                        if ints==control_int:
                            pop_indexes.append(i)
                            pop_indexes.append(i+1)     
        for ind in pop_indexes[::-1]:
            integerList.pop(ind)          
                            
    return integerList

"""
Task 3
In this task, you will modify a txt file which contains information about employees. The file will consist of
a unique ID number, Name, Surname, Job, and Age fields for each person. You will implement a function
named modifyTxt(filename, mode, id, field, newValue) where
• filename is the name of the file to be modified
• mode is either "update" or "delete"
• id is a unique integer value that allows you to distinguish different entries in the file
• field(optional, required only for update operation) is the field that needs to be changed
• newValue(optional, required only for update operation) is the value that will be replaced with the
field’s old value
When a delete is encountered you need to delete that person’s information altogether. In contrast updates
will be done for individual fields. For Example assume we have the following "simplefile.txt" file:
12 Ali Do˘gru Manager 25
24 Veli Yanlı¸s Secretary 29
30 Selami Selam Intern 20
After we call
>>> modifyTxt("simplefile.txt", "update", 12, "age", 26) and
>>> modifyTxt("simplefile.txt", "delete", 30) the file becomes
12 Ali Do˘gru Manager 26
24 Veli Yanlı¸s Secretary 29
Specifications:
2
• Delete operation will not be called for non existent ID numbers
• Your function does not need to return anything, however, you need to rewrite the changes into the
file
• Every field of a person will be separated with a single white space character
• Every person entry will be separated with a newline character
• After updates you must preserve the white spaces and newlines
• Your function must have the same name and must preserve the order of arguments for us to grade
without any trouble
"""

### TASK3
   
def modifyTxt(filename, mode, id, field=None, newValue=None):
    fl=open(filename,"r",)
    all_list=[]
    standart_format=["ID number", "name", "surname", "job", "age"]
    nextline=fl.readline()
    nextline=nextline.rstrip("\n")
    ll=nextline.split()
    
    while nextline!="":
        if id==int(ll[0]):
            if mode=="delete":pass
            elif mode=="update":
                for i in range(len(standart_format)):
                    if field==standart_format[i]:
                        ll[i]=str(newValue)
                        all_list+=[ll]    
        else:
            all_list+=[ll]
        
        nextline =fl.readline()
        nextline=nextline.rstrip("\n")
        ll=nextline.split()
    fl.close()
    
    n_fl=open(filename,"w")
    for e_person in all_list:
        n_fl.write(" ".join(e_person))
        n_fl.write("\n")
    n_fl.close()
