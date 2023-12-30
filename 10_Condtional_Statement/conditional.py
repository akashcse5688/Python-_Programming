#..............chepter  10_contional statement................
x=10
y=12
z=15
if(x<y and x<z):
    #body
    print(f"{x} is small number ")
elif(y<x and y<z):
    #body 
    print(f"{y} is small number ")

else:
    print(f"{z} is small number ")

#vote elegable
age=int(input("Enter your Age= "))
if(age>=18):
    print("Congraculetions")
else:
    print("NOT ELEGIABLE")    
#nested if
x=10
y=12
z=15
if(x>y):
    if(x>z):
        print(x)
elif(y>z):
    if(y>x):
     print(y)
else:
    print(z)


