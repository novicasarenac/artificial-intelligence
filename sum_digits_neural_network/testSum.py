#!/usr/bin/python
import sys

res = []
n = 0
with open('res.txt') as file:	
    data = file.read()
    lines = data.split('\n')
    for id, line in enumerate(lines):
        if(id>0):
            cols = line.split('\t')
            if(cols[0] == ''):
                continue
            cols[1] = cols[1].replace('\r', '')
            res.append(float(cols[1]))
            n += 1

correct = 0
student = []
student_results = []
with open("out.txt") as file:
    data = file.read()
    lines = data.split('\n')
    for id, line in enumerate(lines):
        cols = line.split('\t')
        if(cols[0] == ''):
            continue
        if(id==0):
            student = cols  
        elif(id>1):
            cols[1] = cols[1].replace('\r', '')
            #if (res[cols[0]] == cols):
                #correct += 1
            student_results.append(float(cols[1]))

diff = abs(sum(res) - sum(student_results))
percent = 100 - diff / sum(res) * 100
print percent

