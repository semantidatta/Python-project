import csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path3='Batch.csv'
if os.path.isfile(path3):
    pass
else:
    f=open('Batch.csv','a',newline='')
    w=csv.writer(f)
    w.writerow(['Batch ID','Batch Name','Department Name','List of Courses','List of Students'])
    f.close()

def batchid(bid):
    l=[]
    f=open('Batch.csv','r')
    r=csv.reader(f)
    for row in r:
        l.append(row[0])
    f.close()
    return (bid in l)

def grad(num):
    var='PASS'
    if num>=90:
        grade='A'
    elif num>=80 and num<90:
        grade='B'
    elif num>=70 and num<80:
        grade='C'
    elif num>=60 and num<70:
        grade='D'
    elif num>=40 and num<60:
        grade='E'
    elif num<40:
        grade='F'
        var='FAIL'
    return([var,grade])

def batchname(bnm):
    l=[]
    f=open('Batch.csv','r')
    r=csv.reader(f)
    for row in r:
        l.append(row[1])
    f.close()
    return (bnm in l)

def batchonly():
    while True:
        print('a.Create a new batch')
        print('b.View list of all students in a batch')
        print('c.View list of all courses taught in the batch')
        print('d.View complete performance of all students in a batch')
        print('e.Pie chart of percentage of all students in a batch')
        print('f.EXIT')
        ch3=input('Enter your choice:')
        if ch3 in ('a','A'):
            while True:
                l1,l2,l3=[],[],[]
                bid=input('Enter Batch ID:')
                while batchid(bid)==True:
                    print("Batch already exists.Try again!!!")
                    bid=input('Enter Batch ID:')
                bnm=input('Enter Batch Name:')
                
                while batchname(bnm)== True:
                    print("Batch already exists.Try again!!!")
                    bnm=input('Enter Batch Name:')
                deptnm=input('Enter Department Name:')
                n1=int(input('Enter the number of courses in the batch:'))
                n2=int(input('Enter the number of students in the batch:'))
                for i in range(n1):
                    cid=input(f'Enter Course ID of No.{i+1}:')
                    while cid in l1:
                        print("Course already exists.Try again!!!")
                        cid=input(f'Enter Course ID of No.{i+1}:')
                    l1.append(cid)
                for i in range(n2):
                    stuid=input(f'Enter Student ID of No.{i+1}:')
                    while stuid in l2:
                        print("Student already exists.Try again!!!")
                        stuid=input(f'Enter Student ID of No.{i+1}:')
                    l2.append(stuid)
                l3.append([bid,bnm,deptnm,str(l1),str(l2)])
                f=open('Batch.csv','a',newline='')
                w=csv.writer(f)
                w.writerows(l3)
                f.close()
                sch3=input('Enter more records?(y/n):')
                if sch3 in ('n','N'):
                    break
        elif ch3 in('b','B'):
            li=[]
            bid=input('Enter the required batch ID:')
            while batchid(bid)==False:
                print("Batch doesn't exist.Try again!!!")
                bid=input('Enter Batch ID:')
            with open('Batch.csv','r') as f:
                r=csv.reader(f)
                for i in r:
                    if i[0]==bid:
                        li=i[4]
            print('The students enrolled in the given batch are:')
            print(li)
        elif ch3 in('c','C'):
            li,s1=[],''
            bid=input('Enter the required batch ID:')
            while batchid(bid)==False:
                print("Batch doesn't exist.Try again!!!")
                bid=input('Enter Batch ID:')
            with open('Batch.csv','r') as f:
                r=csv.reader(f)
                for i in r:
                    if i[0]==bid:
                        s1=i[3]
                        s1=s1[1:(len(s1)-1)]
                        s1=s1+','
                        x=''
                        for j in s1:
                            if j==',':
                                li.append(x.strip("'"))
                                x=''
                                continue
                            x=x+j
            print('The courses in the given batch are:')
            for i in li:
                print(i,end=' ')
            print()
        elif ch3 in('d','D'):
            li,s1=[],''
            bid=input('Enter the required batch ID:')
            while batchid(bid)==False:
                print("Batch doesn't exist.Try again!!!")
                bid=input('Enter Batch ID:')
            with open('Batch.csv','r') as f:
                r=csv.reader(f)
                for i in r:
                    if i[0]==bid:
                        s1=i[4]
                        s1=s1[1:(len(s1)-1)]
                        s1=s1+','
                        x=''
                        for j in s1:
                            if j==',':
                                li.append((x.strip()).strip("'"))
                                x=''
                                continue
                            x=x+j
            for i in li:
                print("Student ID:",i)
                with open('Student.csv','r') as f:
                    r=csv.reader(f)
                    for j in r:
                        if i in j[0]:
                            print("Student Name:",j[1])
                            print("Class Roll No. of student:",j[2])
                c,Tmarks=0,0
                with open('Course.csv','r') as f:
                    r=csv.reader(f)
                    for j in r:
                        if i in j[2]:
                            print("Marks in ",j[1],":",(eval(j[2]))[i])
                            print("Marks in ",j[1],":",grad((eval(j[2]))[i])[1])
                            Tmarks=Tmarks+(eval(j[2]))[i]
                            c=c+1
                print("Percentage of student:",Tmarks/c)
                print("Passing Status:",grad(Tmarks/c)[0])
                print("----------------------------------")
        elif ch3 in('e','E'):
            li,s1,perc,sumperc=[],'',[],0
            bid=input('Enter the required batch ID:')
            while batchid(bid)==False:
                print("Batch doesn't exist.Try again!!!")
                bid=input('Enter Batch ID:')
            with open('Batch.csv','r') as f:
                r=csv.reader(f)
                for i in r:
                    if i[0]==bid:
                        s1=i[4]
                        s1=s1[1:(len(s1)-1)]
                        s1=s1+','
                        x=''
                        for j in s1:
                            if j==',':
                                li.append((x.strip()).strip("'"))
                                x=''
                                continue
                            x=x+j
            for i in li:
                print("Student ID:",i)
                c,Tmarks=0,0
                with open('Course.csv','r') as f:
                    r=csv.reader(f)
                    for j in r:
                        if i in j[2]:
                            Tmarks=Tmarks+(eval(j[2]))[i]
                            c=c+1
                perc.append(Tmarks/c)
                sumperc=sumperc+(Tmarks/c)
            for i in range(0,len(li)):
                perc[i]=(perc[i]/sumperc)*100
            y=np.array(perc)
            plt.pie(y,labels=li)
            plt.show()
        elif ch3 in('f','F'):
            break
        else:
            print("Invalid Input.Try again!!!")
