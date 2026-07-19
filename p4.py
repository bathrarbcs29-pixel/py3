student={}
n=int(input("Enter number of studnets:"))
for i in range(n):
    name=input("Enter studnet name")
    marks=int(input("Enter marks"))
    student[name]=marks
search=input("Enter student to be found")
print("Marks",student[search])
print("Student name",search)
