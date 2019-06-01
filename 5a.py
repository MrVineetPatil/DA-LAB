print("Given function is:7n^2+7n+5")
print("g(n)=c.n^2")
c1=int(input("Enter value of c1:"))
c2=int(input("Enter value of c2:"))
for i in range(10,31):
    a1=7*(i*i)+7*i+5
    a2=c1*i*i
    a3=c2*i*i
    if a1>=a2 and a3>=a1:
        n0 = i
        break
print("Value is ",n0)
print("Value\t\tc1.g(n)\t\tf(n)\t\tc2.g(n}")
for i in range(10,31):
    a1=7*(i*i)+7*i+5
    a2=c1*i*i
    a3=c2*i*i

    print(i, "\t\t", a1, "\t\t", a2, "\t\t", a3)