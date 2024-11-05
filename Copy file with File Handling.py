try:
    with open("C:\\Users\\ankit\\OneDrive\\Desktop\\File Handling\A.txt") as F2:
        with open("C:\\Users\\ankit\\OneDrive\\Desktop\\File Handling\B.txt","w") as F3:
            for i in F2:
                F3.write(i)
except:
    print("File not available...plzz create first")
else:
    F2.close()
    print("File closed Sucessfully...!")
