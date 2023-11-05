import os
for (root,dirs,files) in os.walk('.'):
    list1=files
    list2=list1.copy()
depts=["cs","ec"]
deptf=["4MW20CS","4MW20EC"]
cs=[]
ec=[]
for fname1 in list2:
    if ".py" in fname1:
        list2.remove(fname1)
for fname1 in list2:
    if deptf[0] in fname1:
        cs.append(fname1)
    if deptf[1] in fname1:
        ec.append(fname1)

student=input("Enter Student Name: ")
def showmarks(dept,student):
    dept=dept
    stdent=student
    f1=open(cs[0],"r")
    list3=f1.readlines()
    len3=len(list3)
    for i in range(0,len3,1):
        if student in list3[i]:
            print(list3[i])
    f1=open(cs[1],"r")
    list3=f1.readlines()
    len3=len(list3)
    for i in range(0,len3,1):
        if student in list3[i]:
            print(list3[i])
showmarks("cs",student)
