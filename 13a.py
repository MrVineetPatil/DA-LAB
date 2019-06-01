def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

import random,time
a=[random.randint(0,100)for i in range(10)]
print("Unsorted list:",a)
start=time.time()
time.sleep(1)
bubble_sort(a)
end=time.time()
print("Sorted list:",a)
print(end-start,"seconds")