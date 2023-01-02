# Student Examination Portal
import csv
import os
import deptonly
import examonly
import studentpart
import batchonly
import onlycourse



while True:
    print('1.Student Details')
    print('2.Course Details')
    print('3.Batch Details')
    print('4.Department Details')
    print('5.Examination Details')
    print('6.END')
    ch=int(input('Enter your choice:'))
    if ch==1:
        studentpart.studentpart()
    elif ch==2:
        onlycourse.coursepart()
    elif ch==3:
        batchonly.batchonly()
    elif ch==4:
        deptonly.deptonly()
    elif ch==5:
        examonly.exam()
    elif ch==6:
        break
    else:
        print('INVALID INPUT!!')
        print('Enter again')
