# so here i will be making CRUD operation on file project

# so first the user should know how many files and folders are there in a project so i need to make a function for that as well. so for that i can import path to get the path
from pathlib import Path
import os


def readfileandfolder():
    path = Path("")    # if i did this " " that means i will be in the same folder/directory
    # so it reads the folder recursively and get the files
    items = list(path.rglob('*'))  # this will get me the entire list of files in the file handling and now i need to print it.
    # here i used enumerate function - so in normal for loop i can only have value or index but here i can get both in enumerate function
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")   # so this will return the index from 1 instead of 0


# to create the file 
def createfile():
    try:
        readfileandfolder()  # so first i will provide the user with all the file
        name = input("please tell your file name:-")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p, "w") as fs:
                        data = input("what you want to write in this file")
                        fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
             print("this file already exist")
       
    except Exception as err:
        print(f"an error occured {err}")

#  to read a file
def readfile():
    try:
        readfileandfolder()
        name = input("which file you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
            print("READED SUCCESSFULLY")
        else:
                   print("the file does not exist")
    except Exception as err:
         print(f"an error occured as {err}")


# to update the file - to update the file name, data overwrite, data append 
def updatefile():
    try:
        readfileandfolder()
        name = input("which file you want to update")
        p = Path(name)
        if p.exists() and p.is_file():
                 print("press 1 for changing the name of your file")
                 print("press 2 for overwriting the data of your file")
                 print("press 3 for appending some content in your file")
         
                 res = int(input("tell your response"))
         
                 if res == 1:
                      name2 = input("tell your new file name:- ")
                      p2 = Path(name2)
                      p.rename(p2)
         
                 if res == 2:
                      with open (p, "w") as fs:
                           data = input("tell what you want to write this will override the data")
                           fs.write(data)
         
                 if res == 3:
                      with open(p, "a") as fs:
                           data = input("tell what you want to append")
                           fs.write(" "+data)

    except Exception as err:
         print(f"an error occured as {err}")


# to delete the file

def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delete")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print("FILE REMOVED SUCCESSFULLY")
          
        else:
            print("no such file exists")

    except Exception as err:
         print(f"an error occured {err}")


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleton a file")

check = int(input("please tell your response:-"))

# so i am making it function based and here are function calls for each number selected
if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()