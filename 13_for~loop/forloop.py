#for loop------------------------------------?
lis=["Akash","bappy","abdullah","auntu","roni","sabbir","shovo"]
print(lis)
#Syntex...for new_varrable_name in list name
for name in lis:
    print(name)
#for string    
name="RAKIBUL HASAN AKASH" 
for a in name:
    print(a)   
#Range function
for I in range(9):
    print(I)
#nested for loop
a=["RAKIBUL "]
b=["Hasan "]
c=["Akash"]
for x in a:
    for y in b:
        for z in c:
            print(f"{x+y+z}")
