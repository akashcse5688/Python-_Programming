#Chepter-11.........Dictionary(multiple type data like a Structure in c)
#Syntex
'''dictionary_name={
"key":"value_1",
.............
"key":"value_n"
}'''

#Example
Persion ={
  "first_name":"AKASH",
  "last_name":"RAKIBUL",
  "age":22
 }
print(type(Persion))
print(Persion)
#Accesing Item...........................
Persion["first_name"]="Rakibul"#dictionay[key]=""
print(Persion)
#get_method()
print(Persion.get("first_name"))
#Additing value
#Remove Item pop method
Persion.pop("age")
print(Persion)
#nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"])
family={
"name":"Akash",
"Age":"23",
"db":"14/10/23"
}
print(family)
family["db"]="26/12/2023"
print(family)
print(family.get("db"))
family.pop("name")
print(family)


Famialy={
 "child_1":{
  "name":"akash",
  "age":"23" 
 },
"child_2":{
 "name":"batash",
  "age":"23" 
},
"child_3":{
  "name":"sky",
  "age":"23" 
}
}
print(Famialy["child_1"])
Famialy["child_1"]["name"]="rakib"
print(Famialy["child_1"])
