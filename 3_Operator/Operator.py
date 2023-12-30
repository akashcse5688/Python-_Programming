#..................................#Chapter-03; Operators in Python..............................#

#....................Types of Operator............................

#................Arithmetic Operator........................
number_1=100
number_2=10
print(number_1+number_2)#Additation
print(number_1-number_2)#subtraction
print(number_1/number_2)#Division
print(number_1%number_2)#reminder
print(number_1**number_2)#expotional
print(number_1//number_2)#floor division remove float part
#............................Assigment Operator...............
#X=10
#Y=12
#X+=Y
#X=X+Y
#print(X)

#....................Comperasion Operator either true or false...............
x=10
y=12
comparisom=x<y
print(comparisom)


#..........................Logical Operator (and,or).........
#both side true=true........(and)
#one true other false=true.....(or)
x=10
y=12
z=15
if(x<y and x<z):
    print(f"{x} is small number ")
elif(y<x and y<z):
    print(f"{y} is small number ")
else:
    print(f"{z} is small number ")

x=12
y=1
comparisom= not x>y
print(comparisom)


