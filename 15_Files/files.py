#file----------------------------
#creating.........
#file=open("demo.txt","x")
#writing a file
#file=open("demo.txt","w")
#file.write("Not talented\n, you have to be hard working because I haven't seen all the talent win,\nI've never seen another hardworking lose!!")
#add any line
#file=open("demo.txt","a")
#file.write("RAKIBUL")
file=open("demo.txt","r")
r=file.read()
print(r)
file.close()#close
