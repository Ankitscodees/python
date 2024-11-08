F=open("data.dat","a")

while(True):
   id=input("Enter Id:")
   name=input("Enter Name:")
   salary=input("Enter Salary:")

   data="{0},{1},{2}\n".format(id,name,salary)
   F.write(data)

   ch=input("Continue y/n?")

   if(ch=="n"):break
F.close()
