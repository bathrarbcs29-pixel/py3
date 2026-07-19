students_list=[]
n=int(input("Enter number of students"))
for i in range(n):
    print("Students",i+1)
    id=input("Enter student id")
    name=input("Enter student name")
    m=float(input("Enter student marks"))
    students_list.append((id,name,m))
    students=tuple(students_list)
print("All Students:")
for j in range(0,len(students)):
    print(students[j][0],'\t',students[j][1],'\t',students[j][2])
search_id=input("Enter student id")
for s in students:
    if s[0]==search_id:
        print("Record found\nID:",s[0],"Name:",s[1],"Marks:",s[2])
        break
    else:
        print("Student not found")
print("Student marks less than 40")
max=0
t=0
for st in students:
    if st[2]<40:
        print(st[0],"\t",st[1],"\t",st[2])
    if st[2]>max:
        max=st[2]
        tup=(st[0],st[1],st[2])
    t+=st[2]
avg=t/n
print("Student with highest marks",tup)
print("Average",avg)
