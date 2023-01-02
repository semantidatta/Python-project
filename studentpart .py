import csv
import os
import pandas as pd
import json
path1='Student.csv'
if os.path.isfile(path1):
    pass
else:
    fob1=open('Student.csv','a',newline='')
    wob1=csv.writer(fob1)
    wob1.writerow(['Student ID','Name','Class Roll No.','Batch ID'])
    fob1.close()

def grading(num):
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

def checkincourse(stuid):
    c,cnm={},''
    f=open('Course.csv','r')
    r=csv.reader(f)
    for row in r:
        if (stuid in eval(row[2])) == True:
            c=eval(row[2])
            cnm=row[1]
    f.close()
    if c!={} and cnm!='':
        return([cnm,c])
    else:
        return(False)

def batid(bid):
    l=[]
    f=open('Batch.csv','r')
    r=csv.reader(f)
    for row in r:
        l.append(row[0])
    f.close()
    return (bid in l)

def studentpart():
    while True:
        print('a.Create a new student')
        print('b.Update student details')
        print('c.Remove a student from the database')
        print('d.Generate report card')
        print('e.Exit')
        ch1=input('Enter your choice:')
        if ch1 in ('a','A'):
            while True:
                c=0
                id=input('Enter Student ID:')
                with open('Student.csv','r') as f:
                    r=csv.reader(f)
                    for i in r:
                        if i[0]==id:
                            c=1
                if c==1:
                    print("This student already exists.Try again!!!")
                    continue
                nm=input('Enter name of the Student:')
                croll=input('Enter class roll number:')
                B_Id=input('Enter Batch ID:')
                while batid(B_Id)==False:
                    print("Batch doesn't exist.Try again!!!")
                    B_Id=input('Enter Batch ID:')
                f=open('Student.csv','a',newline='')
                w=csv.writer(f)
                w.writerow([id,nm,croll,B_Id])
                f.close()
                c,l1,l2,s1,s2=0,[],[],'',''
                with open('Batch.csv','r') as f:
                    r=csv.reader(f)
                    for i in r:
                        if B_Id==i[0]:
                            s1=i[3]
                            s1=s1[1:(len(s1)-1)]
                            s1=s1+','
                            x=''
                            for j in s1:
                                if j==',':
                                    l1.append(x)
                                    x=''
                                    continue
                                x=x+j
                            s2=i[4]
                            s2=s2[1:(len(s2)-1)]
                            s2=s2+','
                            x=''
                            for j in s2:
                                if j==',':
                                    l2.append(x)
                                    x=''
                                    continue
                                x=x+j
                            break
                        c=c+1
                l2.append(id)
                df = pd.read_csv("Batch.csv")
                df.loc[c, 'List of Students'] = str(l2)
                df.to_csv('Batch.csv',index=False)
                for i in l1:
                    c,xd=0,{}
                    with open('Course.csv','r') as f:
                        r=csv.reader(f)
                        for j in r:
                            if i==j[0]:
                                xd=eval(j[2])
                                break
                            c=c+1
                    xd[id]=int(input("Enter marks of student in course"+i+":"))
                    df = pd.read_csv("Course.csv")
                    df.loc[c, 'Student ID-Marks Obtained'] = str(xd)
                    df.to_csv('Course.csv',index=False)
                sch1=input('Enter more records?(y/n):')
                if sch1 in ('n','N'):
                    break
        elif ch1 in('b','B'):
            while True:
                c,x=-1,0
                id=input('Enter the Student ID of the student whose details you want to update:')
                while True:
                    c,x=-1,0
                    with open('Student.csv','r') as f:
                        r=csv.reader(f)
                        for i in r:
                            if i[0]==id:
                                x=1
                                break
                            c=c+1
                    if x==0:
                        print("Student ID does not exist.Try again!!!")
                        id=input('Enter the Student ID of the student whose details you want to update:')
                    else:
                        break
                nm=input('Enter name of the Student:')
                roll=input('Enter class roll number:')
                df = pd.read_csv("Student.csv")
                df.loc[c, 'Name'] = nm
                df.loc[c, 'Class Roll No.'] = roll
                df.to_csv('Student.csv',index=False)
                sch2=input('Update more records?(y/n)')
                if sch2 in ('n','N'):
                    break
        elif ch1 in ('c','C'):
            while True:
                c,x=-1,0
                id=input('Enter the Student ID of the student whose details you want to delete:')
                while True:
                    c,x=-1,0
                    
                    with open('Student.csv','r') as f:
                        r=csv.reader(f)
                        for i in r:
                            if i[0]==id:
                                x=1
                                break
                            c=c+1
                    if x==0:
                        print("Student ID does not exist.Try again!!!")
                        id=input('Enter the Student ID of the student whose details you want to delete:')
                    else:
                        break
                df = pd.read_csv("Student.csv")
                df.drop(c,axis=0,inplace=True)
                sch3=input('Delete more records?(y/n)')
                if sch3 in ('n','N'):
                    break
        elif ch1 in('d','D'):
            while True:
                c,x,li,nm,roll=0,0,[],'',0
                id=input('Enter the Student ID of the student whose report card you want to generate:')
                while True:
                    x=0
                    
                    with open('Student.csv','r') as f:
                        r=csv.reader(f)
                        for i in r:
                            if i[0]==id:
                                nm,roll,x=i[1],i[2],1
                                break
                    if x==0:
                        print("Student ID does not exist.Try again!!!")
                        id=input('Enter the Student ID of the student whose report card you want to generate:')
                    else:
                        break
                c,d,Tmarks=0,{},0
                with open('Course.csv','r') as f :
                    r=csv.reader(f)
                    for i in r:
                        if id in i[2]:
                            d[i[1]]=(eval(i[2]))[id]
                            Tmarks=Tmarks+(eval(i[2]))[id]
                            c=c+1
                with open('Result.txt','w+') as file:
                    file.write("REPORT CARD\n")
                    file.write("Student ID: "+id+'\n')
                    file.write("Student Name: "+nm+'\n')
                    file.write("Class Roll no. of student: "+roll+'\n')
                    for i in d:
                        file.write("Marks in "+i+" : "+str(d[i])+'\t'+"Grade in "+i+" : "+str((grading(d[i]))[1])+'\n')
                    file.write("Percentage of student: "+str(Tmarks/c)+'\n')
                    file.write("Passing Status:"+str((grading(Tmarks/c))[0])+'\n')
                with open('Result.txt','r') as file:
                    print(file.read())
                sch6=input('Generate more report cards?(y/n):')
                if sch6 in ('n','N'):
                    break
        elif ch1 in('e','E'):
            break
        else:
            print('INVALID INPUT!!')
            print('Enter again')

