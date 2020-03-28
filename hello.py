#!/usr/bin/python

'''
trlalala
'''

import sys

print('hello'
      ' world')

item_one=1
item_two=2
item_three=3

#that unites lines
total = item_one + \
        item_two + \
        item_three

print (total)

daysofweek=["monday","tuesday","wensday",
    "thursday","friday"]

word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

print("type of item_one is", type(item_one))

hexa=0XFF #number in hex, prints in decimal
bina=0B011 #number in bin, prints in decimal
print(hexa)
print(bina)
print(bin(bina)) #force bin print

print(9>8) #returns True
boole1=True #bool

abc=33.6
print(int(abc)) #converts to int. just removes after . so returs 33

deef=float("22.3") #also converts
print(deef)

#raw_input("\n\npress")