f=open("myfile.txt","w")
name=input("enter name= ")
print(f.write(name))
f=open("myfile.txt","r")
print(f.read())
f.close()
