#chepter -9...................function in python

#syntex of function
#def function_name(parameter):
#workinkg tools

#print hello_World using function
def hello_World():
    #function body
    print("hello Python!")
    
#function callin
hello_World()    
#add two value user input
def Addition(a,b):
    sum=int(a)+int(b)
    print(sum)
Addition(12,15)        
#return type function
def Addition(a,b):
    sum=int(a)+int(b)
    return sum
print(f"{Addition(12,15)}")
