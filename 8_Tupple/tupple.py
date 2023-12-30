#chepter -----8-->Tupple

#tupple vs list......*.list are changeable but tupple is not changeable*
animal= input("Enter your item = ")
li=animal.split(",")
C_tu=tuple(li)
print(C_tu)
print(type(C_tu))

pets=("cat","dog","animal")
print(type(pets))
print(pets[0])
#But not changed
pets[0]="Dogilina"
print(pets)



