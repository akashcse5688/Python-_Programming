#list is like a array
# <......................................................list...in.....python..............................>
#create
pets=["Pets","cats","rabit"]
print(pets)
#indexing
#positive index 0,1,2
#negative index -3,-2,-1
# Range of index

print(pets[0:2])

#Additing of list
pets.append("Elephent")
print(pets)
#insert(any index)
pets.insert(0,"Bird")
print(pets)
#additing two list extend
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
#membership
country=["bangladesh","india"]
check_item="bangladesh" in country
print(check_item)
#user input
n=input("Enter the= ")
li=n.split()
  
