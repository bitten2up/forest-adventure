import os.path
from os import path

def main():
   answer = input("open which file $ ")
   print("Item exists:" + str(path.exists(answer)))
   print("Item is a file: " + str(path.isfile(answer)))
   file = str(path.isfile(answer))
   if file == "True":
       f = open(answer, "r")
       print(f.read())
   else:
        print("cant find that file or it is a folder")
if __name__== "__main__":
   main()
