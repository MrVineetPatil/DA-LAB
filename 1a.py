import random,time

def bin_search(A,low,high,key):
    if low<=high:
        mid=(low+high)//2
        if key==A[mid]:
            return mid+1
        elif  key<A[mid]:
            return bin_search(A,low,mid-1,key)
        else:
            return bin_search(A,mid+1,high,key)
        return None

n=int(input("Enter no of elements:"))
A=[random.randint(0,100) for i in range(n)]
A.sort()
print(A)
k=int(input("Enter the element to be found:"))
start=time.time()
time.sleep(1)
print(bin_search(A,0,n-1,k))
end=time.time()
print(end-start,"seconds")