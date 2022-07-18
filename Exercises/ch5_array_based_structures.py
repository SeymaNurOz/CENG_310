# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:05:16 2022

@author: seyma
C-5.21

"""
#  Execute the experiment from Code Fragment 5.1 and compare the results
# on your system to those we report in Code Fragment 5.2.
import sys # provides getsizeof function
data = []
for k in range(20): # NOTE: must fix choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    # print("Length: {0:3d}; Size in bytes: {1:4d}" .format(a, b))
    data.append(None)

#  The shuffle method, supported by the random module, takes a Python
# list and rearranges it so that every possible ordering is equally likely.
# Implement your own version of such a function. You may rely on the
# randrange(n) function of the random module, which returns a random
# number between 0 and n−1 inclusive    
import random as rnd
# print(rnd.randrange(0,100))

# C-5.21 In Section 5.4.2, we described four different ways to compose a long
# string: (1) repeated concatenation, (2) appending to a temporary list and
# then joining, (3) using list comprehension with join, and (4) using generator comprehension with join. Develop an experiment to test the efficiency
# of all four of these approaches and report your findings

def ver_1(str_x):
    letters=""
    a=[]
    for c in str_x:
        a.append(c)
        letters+=c
        if c.isalpha():
            print(c)
            letters+=c
    return a
    
# def ver_2(str_x):
#     letters ="" # start with empty string
#     for c in str_x:
#         if c.isalpha():
#             print(c)
#             letters += c
#     # return letters   


str_1="fmsk"   
print(ver_1(str_1))


# P-5.35 Implement a class, SubstitutionCipher, with a constructor that takes a
# string with the 26 uppercase letters in an arbitrary order and uses that for
# the forward mapping for encryption (akin to the self. forward string in
# our CaesarCipher class of Code Fragment 5.11). You should derive the
# backward mapping from the forward version

class myCaesarCipher:

    def __init__ (self,shift):
        self.shift=shift
        encoder=['q', 'w', 'e', 'r', 't', 'y', 'u', 'ı', 'o', 'p', 'ğ', 'ü', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ş', 'i', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ö', 'ç']
        decoder=[]
        decoder+=encoder
        decoder.reverse()

        self._encoder=encoder
        self._decoder=decoder


    def encrypt(self, message):
        return self. transform(message, self._encoder)

    def decrypt(self, secret):
        return self. transform(secret, self._decoder)
    
    def transform(self, original_msg, code):
        msg = list(original_msg)
        for k in range(len(msg)):
            if msg[k] in code:
                new_index=(code.index(msg[k])+self.shift)%len(code)
                msg[k]=code[new_index]
            # if msg[k].isupper():
        #     j = ord(msg[k]) - (self.shift ) 
        #     msg[k] = code[j%len(self._forward)] # replace this character
        return "".join(msg)


if __name__ == "__main__" :
    cipher = myCaesarCipher(3)
    message = "Bugün kritik almalıyım."
    coded = cipher.encrypt(message)
    print(" Secret:" , coded)
    answer = cipher.decrypt(coded)
    print( "Message: ", answer)

