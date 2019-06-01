print("Given function is 3n^2+4n+3:")
print("g(n)=n")
c=int(input("Enter value of c:"))
for i in range(10,31):
    a1=3*(i*i)+4*i+3
    a2=c*i
    if a1>=a2:
        n0=i
        break
print("Value of n0:",n0)
print("Value\t\tf(n)\t\tc.g(n}")
for i in range (10,31):
    a1 = 3 * (i * i) + 4 * i + 3
    a2 = c * i
    print(i,"\t\t",a1,"\t\t",a2)
