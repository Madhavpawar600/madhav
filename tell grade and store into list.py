a=int(input("enter the no you want store info"))
list1=[]

for i in range(0,a):
    b=input("enter the name")
    c=int(input("enter the marks"))

    if c<=100 and c>80:
        g="A+"
    elif c<=80 and c>70:
        g="a"
    else:
        g="fail"

    list1.append([b,g])

print(list1)
