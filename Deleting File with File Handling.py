import os
if os.path.exists("C:\\Users\\ankit\\OneDrive\\Desktop\\File Handling\B.txt"):
    os.remove("C:\\Users\\ankit\\OneDrive\\Desktop\\File Handling\B.txt")
    print("File Deleted sucessfully...!")
else:
    print("File not available...!")
