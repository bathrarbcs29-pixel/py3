A=eval(input("Enter the value of A:"))
B=eval(input("Enter the value of B:"))
res=[[0]*len(B[0])for _ in range(len(A))]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            res[i][j]+=A[i][k]*B[k][j]
for row in res:
    print(row)
