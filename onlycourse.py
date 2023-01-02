import csv
import os
import numpy as np
import matplotlib.pyplot as plt
path='Course.csv'
if os.path.isfile(path):
    pass
else:
    fob=open('Course.csv','a',newline='')
    wob=csv.writer(fob)
    wob.writerow(['Course ID','Course Name','Student ID-Marks Obtained'])
    fob.close()
    
def check1(id):
    l=[]
    f=open('Course.csv','r')
    r=csv.reader(f)
    for row in r:
        l.append(row[0])
    f.close()
    return (id in l)

def check2(nm):
    l=[]
    f=open('Course.csv','r')
    r=csv.reader(f)
    for row in r:
        l.append(row[1])
    f.close()
    return (nm in l)

def check3(stuid):
    c=False
    f=open('Course.csv','r')
    r=csv.reader(f)
    for row in r:
        if (stuid in eval(row[2])) == True:
            c=True
    f.close()
    return(c)

def coursepart():
    while True:
        print('a.Create a new course')
        print('b.View performance of all students in the course')
        print('c.Show course statistics')
        print('d.Exit')
        ch2=input('Enter your choice:')
        if ch2 in ('a','A'):
            while True:
                l2a2,l2a3,l2a4=[],{},[]
                a2=input('Enter Course ID:')
                b2=input('Enter Course Name:')
                if (check1(a2)==True or check2(b2)==True):
                    print("Course already present, Try again!!")
                    continue
                ask2a1=int(input('Enter the number of students in the course:'))
                for i in range(0,ask2a1):
                    c2=input(f'Student ID of no. {i+1} :')
                    while True:
                        if c2 in l2a3:
                            print('This Student already exists in this course!')
                            print('Enter again')
                            c2=input('Student ID:')
                        else:
                            break
                    d2=int(input('Enter the Total marks:'))
                    l2a3[c2]=d2
                l2a4.append([a2,b2,str(l2a3)])
                fob2=open('Course.csv','a',newline='')
                wob2=csv.writer(fob2)
                wob2.writerows(l2a4)
                fob2.close()
                sch2=input('Enter more Courses?(y/n):')
                if sch2 in ('n','N'):
                    break
        elif ch2 in('b','B'):
            while True:
                d,e={},{}
                c=input('Enter course ID:')
                with open('Course.csv','r') as f1 , open('Student.csv','r') as f2 :
                    r1=csv.reader(f1)
                    r2=csv.reader(f2)
                    for i in r1:
                        if i[0]==c:
                            print("Course Name:",i[1])
                            d=eval(i[2])
                    for i in d:
                        e[i]=[]
                    for i in r2:
                        if i[0] in d:
                            e[i[0]].append(i[1])
                            e[i[0]].append(i[2])
                if d=={} and e=={}:
                    print("Course not present.TRY again!!!")
                    continue
                for i in d:
                    print('Student ID:',i)
                    print('Name:',(e[i])[0])
                    print('Class Roll No.',(e[i])[1])
                    print('Marks in ',i,':',d[i])
                    print('-----------------------------')
                x=input("Check student details of more courses?(y/n):")
                if x in ('n','N'):
                    break
        elif ch2 in ('c','C'):
            a = np.array([22, 87, 5, 43, 56,
              73, 55, 54, 11,
              20, 51, 5, 79, 31,
              27])

            fig, ax = plt.subplots(figsize =(10, 7))
            ax.hist(a, bins = [0, 25, 50, 75, 100])
 
            plt.show()
        elif ch2 in('d','D'):
            break
        else:
            print("Invalid Input.Try again!!!")

