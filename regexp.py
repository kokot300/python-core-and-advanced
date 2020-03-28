#!/bin/usr/python
#\d digit \D non digit
#\s space \S non space
#\w alphanumeric \W non alphanumeric

import re

str="take up one idea at once.At 0nce!!!"
r=re.search(r'o\w\w',str) #case sensitive
print(r.group()) #if not found returns None
#r'' is the syntax. above it has to start by o and be followed by two alphanumeric characters
r=re.findall(r'o\w\w',str)
print(r)
r=re.match(r't\w\w',str)
print(r.group())

r=re.split(r'\d+',str) #+ one or more
# * zero or more repetitions
# ? zero or one repetition
#{m,n} exactly preceeding expression m=minimum repetitions, n=max repetitions, by default 0 and infinitive
print(r)

r=re.sub(r'one','twice',str)
print(r)

r=re.findall(r'o\w+',str)
print(r)
r=re.findall(r'o\w?',str)
print(r)
r=re.findall(r'o\w*',str)
print(r)
r=re.findall(r'o\w{0,2}',str)
print(r)

str1="Take 1 up 1-3-2019 One 23 idea.One idea 45 at a Time 12-11-2020"
r=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str1)
print(r)

# \ escape character
# . matches every charakter exept new line
#^ searches on the beginning of the string
#$ searches on the end of the string
# [] range of values [a,z]
#[^...] matches everything except
#() match regular expresion
#(|) | specifies multiple regular expressions

r=re.findall(r'^T\w',str1)
print(r)
