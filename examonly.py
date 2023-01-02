import csv
import os
import pandas
import numpy as np
import matplotlib.pyplot as plt

def checkcid(id):
    l=[]
    f=open('Course.csv','r')
    r=csv.reader(f)
    for row in r:
        l.append(row[0])
    f.close()
    return (id in l)




def exam():
    z={}
    while True:
        print('a.Enter the marks of all students for a specific examination')
        print('b.View performance of all students in the above examination')
        print('c.Show examination statistics')
        print('d.Exit')
        ch2=input('Enter your choice:')
        m,cid={},''
        if ch2 in ('a','A'):
            cid=input('Enter Course ID:')
            while checkcid(cid)==False:
                print("The course is not present.Try again!!!")
                cid=input('Enter Course ID:')
            with open('Course.csv','r') as f:
                r=csv.reader(f)
                for i in r:
                    if i[0]==cid:
                        m=eval(i[2])
            for i in m:
                m[i]=int(input("Enter marks of student:"+i))
            z=m
        elif ch2 in('b','B'):
            print("Performance of all students enrolled in the course for ",cid," : ")
            for i in z:
                print("Student ID:"+i+"\t"+"Marks:"+str(z[i]))
        elif ch2 in('c','C'):
            x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
            y = np.array([99,86,87,88,81,86,73,87,94,78,77,85,86])
            plt.scatter(x, y)
            x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
            y = np.array([100,90,84,85,90,99,90,95,94,91,79,77,91,80,85])
            plt.scatter(x, y)
            plt.show()
        elif ch2 in('d','D'):
            break
        else:
            print("Invalid Input.Try again!!!")
          
            
