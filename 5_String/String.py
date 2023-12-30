#....................Chepter 5 Working with String
#Single or Double quations
text="Hi,i am AKASH.i love 'Python' programing language"
print(text)


#Multiline String use-'''...................''''(triple quations)
text='''The Blood Bank Management System is to create an e-Information about the donor and organization that are related to donating the blood.
Through this application any person who is interested in donating the blood can register himself in the same way if any

organization wants to register itself with this site that can also register. Moreover, if any general consumer wants to make request blood online, he can also take the help of this site. Admin is the main authority who can do addition, deletion, and modification if required.'''
print(text)

#conceting string
a="RAKIBUL "
b="HASAN "
c="AKASH "
sum=a+b+c
print(sum)

#Accesing value of string
#indexing
text="I LOVE PYTHON"
print(text)
print(text[2])

#slicing (muticharacter)
text="I LOVE PYTHON"
print(text[2:5]) #[start index:End index]
#
 #small to captital
text="abcdef"
x=text.capitalize()
print(x)

#upper case
text="abcdef"
x=text.upper()
print(x)
#loewer case is the vise versa


#length of string
#syntex=len(name)
text="abcdef"
print(len(text))

#replace world
a="rakib"
r=a.replace("r","R") #Syntex=replace("old","new")
print(r)
#...................................................................AKASH....................................................#
