# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:33:08 2022

@author: seyma
"""

# R-4.3 Draw the recursion trace for the computation of power(2,18), using the
# repeated squaring algorithm, as implemented in Code Fragment 4.12.

def power_n(base,power):
    if power==0:
        return 1
    elif power%2==0:
        new_base=base*base
        return power_n(new_base,power//2)
    elif power%2==1:
        new_base=base*base
        return power_n(new_base,power//2)*base
    
print(power_n(2,18))

# C-4.14 In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,
# b, and c, sticking out of it. On peg a is a stack of n disks, each larger than
# the next, so that the smallest is on the top and the largest is on the bottom.
# The puzzle is to move all the disks from peg a to peg c, moving one disk
# at a time, so that we never place a larger disk on top of a smaller one.
# See Figure 4.15 for an example of the case n = 4. Describe a recursive
# algorithm for solving the Towers of Hanoi puzzle for arbitrary n. (Hint:
# Consider first the subproblem of moving all but the nth disk from peg a to
# another peg using the third as “temporary storage.”)
def hanoi_tower(n,p_1,p_2,p_bos):
    if n==1:
        print("{} to {}".format(p_1,p_2))
    elif n>1:
        hanoi_tower(n-1, p_1, p_bos, p_2)
        print("{} to {}".format(p_1,p_2))
        hanoi_tower(n-1, p_bos, p_2, p_1)
    # elif n==2:
    #     print("{} to {}".format(p_1,p_bos))
    #     print("{} to {}".format(p_1,p_2))
    #     print("{} to {}".format(p_bos,p_2))
    # elif n==3:
    #     hanoi_tower(2, p_1, p_bos, p_2)
    #     print("{} to {}".format(p_1,p_2))
    #     hanoi_tower(2, p_bos, p_2, p_1)
        
    # elif n==4:
    #     hanoi_tower(3, p_1, p_bos, p_2)
    #     print("{} to {}".format(p_1,p_2))
    #     hanoi_tower(3, p_bos, p_2, p_1)

# hanoi_tower(4, "A","B", "C")
    

# C-4.15 Write a recursive function that will output all the subsets of a set of n
# elements (without repeating any subsets).
sub_s=[]
def sub_sets(list_x,n):
    global sub_s
    # if n==1:
    #     for i in list_x:
    #         sub_s.append()
    # count=n*(n-1)/2
    # sub_s=[]*count
    # for i in 
    if len(list_x)==n:
        sub_s.append(list_x)
    for k in range(len(list_x)):
        a_sub=list_x[:k]+list_x[k+1:]
        if a_sub==n:
            sub_s.append(a_sub)
        else:
            sub_sets(a_sub,n)
    
    x=[]
    for elem in sub_s:
        if elem not in x:
            x.append(elem)
    return x
        
print(sub_sets([1,2,3,4,5],3))

# C-4.17 Write a short recursive Python function that determines if a string s is a
# palindrome, that is, it is equal to its reverse. For example, racecar and
# gohangasalamiimalasagnahog are palindromes.
# RECURSIVE OLMADI -BOSVERR -LOOP YERINE İÇ İÇE YAP-TMM
def palindrome(str_1):
    rt=True
    # for i in range(len(str_1)//2+1):
    #     if str_1[i]!=str_1[-i-1]:
    #         rt=False
    if len(str_1)<3:
        if str_1[0]==str_1[-1]:
            return True
    else:
        if str_1[0]==str_1[-1] and palindrome(str_1[1:-1])is True:
            return True
        else: return False
        
    return rt
print(palindrome("gohangasalamiimalasagnahog"))

# C-4.21 Suppose you are given an n-element sequence, S, containing distinct integers that are listed in increasing order. Given a number k, describe a
# recursive algorithm to find two integers in S that sum to k, if such a pair
# exists. What is the running time of your algorithm?

def find_couple(list_x,sum_n):
    for item_1 in list_x:
        if item_1==sum_n/2:
            pass
        else:
            for item_2 in list_x:
                if item_1+item_2==sum_n:
                    return (item_1,item_2)
list_x=list(range(0,60,1))

import time
start_time = time.time()
print(find_couple(list_x, 100))
print("--- %s seconds ---" % (time.time() - start_time))

# P-4.23 Implement a recursive function with signature find(path, filename) that
# reports all entries of the file system rooted at the given path having the
# given file name.

import os

def find_subfolders(path_1):
    if os.path.isdir(path_1):
        path_2=os.listdir(path_1)
        print(path_2)
        # os.walk()
        # for fold in part_2:
        # x=os.path.realpath(path_2)
        # print(x)
        for item in path_2:
            path_new=path_1+"/"+item
            if os.path.isdir(path_new):
                find_subfolders(path_new)
        # find_subfolders("r"+str(path_2))
find_subfolders(r"C:/Users/seyma/Desktop/ladybug-tools-1-4-0")
    
    
# 3 def disk usage(path):
# 4 ”””Return the number of bytes used by a file/folder and any descendents.”””
# 5 total = os.path.getsize(path) # account for direct usage
# 6 if os.path.isdir(path): # if this is a directory,
# 7 for filename in os.listdir(path): # then for each child:
# 8 childpath = os.path.join(path, filename) # compose full path to child
# 9 total += disk usage(childpath) # add child’s usage to total
# 10
# 11 print ( {0:<7} .format(total), path) # descriptive output (optional)
# 12 return total

    
        
    
    