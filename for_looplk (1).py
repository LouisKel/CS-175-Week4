# -*- coding: utf-8 -*-
"""for-loopLK

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UOhDxvPY7N6yH9cnL-nNflVxwLXoIApR
"""

#Squares of List Elements
i = 0
for i in [2,4,6,8]:
  i = i**2
  print(i)

#Grade Calculator

marks = [85, 92, 78, 90, 88]
i = 0
l = 0
j = 0
for i in marks:
  j = i + j
  l = l + 1
print("The average of all the grades of the student is", j/l)
if 90 <j/l <100:
  print("So the student grade (", j/l,") is A")
elif 80<i<89:
  print("So the student grade (", j/l,") is B")
elif 70<i<79:
  print("So the student grade (", j/l,") is C")
elif 60<i<69:
  print("So the student grade (", j/l,") is D")
else:
  print("So the student grade (", j/l,") is F")