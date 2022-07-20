# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:39:35 2022

@author: seyma nur oz

"""
### ☻TASK1

def tensionCalculator(m, v, r):
    tension=m*v**2/r
    return tension


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