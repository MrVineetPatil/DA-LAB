def sel_sort(L):
    for i in range(len(L) - 1):
        min = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min]:
                min = j
            L[i], L[min] = L[min], L[i]


import random, time

a = [random.randint(0, 100) for i in range(10)]
print("Unsorted list:", a)
start = time.time()
time.sleep(1)
sel_sort(a)
end = time.time()
print("Sorted list:", a)
print(end - start, "seconds")