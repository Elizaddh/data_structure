# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:07:44 2017

@author: ankit
"""

#create repeat of each element of sequence
original='atgcatgcccgt'
b=list(original)
c=[]

for alphabet in b:
        value=2*alphabet
        c.append(value)

a= ''.join(c)
print a
        



    