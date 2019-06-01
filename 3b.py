import random,time

def insert_sort(L):
    n=len(L)
    for i in range(1,n):
        v=L[i]
        j=i-1
        while j>=0 and L[j]>v:
            L[j+1]=L[j]
            j-=1
        L[j+1]=v
    return L

def bucket_sort(L):
    B=[]
    for i in range (10):
        B.append([])
    n=len(L)
    for i in range(n):
        B[int(n*L[i])].append(L[i])
    for i in range(n):
        B[i]=insert_sort(B[i])
    result=[]
    for i in range(n):
        result.extend(B[i])
    return result

#n=int(input("Enter no of elements:"))
#A=[random.randint(0,100) for i in range(n)]
A=[.78,.17,.37,.26,.72,.94,.21,.12,.23,.68]
print("Unsorted list:",A)
#start=time.time()
#time.sleep(1)
#print("Sorted list:",insert_sort(A))
#end=time.time()
#print(end-start,"seconds")
A=bucket_sort(A)
print(A)