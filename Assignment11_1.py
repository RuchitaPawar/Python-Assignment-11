import os
from sys import argv
import hashlib


def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def DisplayCheckSum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName,subDirs,fileList in os.walk(path):
            print("Current folder is:",dirName)
            for fileName in fileList:
                path = os.path.join(dirName,fileName)
                file_hash = hashfile(path)
                print("File name  and size : ",fileName,file_hash)

   #   print("Invalid arguments Directory does not exists")
    #  exit()

    if(argv[1] == '-h') or (argv[1] == '-H'):
        print("The script is used to travel specific directory")
        exit()

    if (argv[1] == '-u') or (argv[1] == '-U'):
        print("usage : Application name absolute_path_of_directory")
        exit()

    try:
        DirectoryWatcher(argv[1])
    except ValueError:
        print("Invalid data type of input")

    except Exception:
        print("Error : Invalid input")


def main():
    print("---------------Application name--------------",argv[0])
    print("Accept directory name and display checksum of all files")

    if(len(argv) < 1):
        print("Invalid number of arguments main")
        exit()

    if(argv[1] == '-h') or (argv[1] == '-H'):
        print("The script is used to travel specific directory")
        exit()

    if (argv[1] == '-u') or (argv[1] == '-U'):
        print("usage : Application name absolute_path_of_directory")
        exit()

    try:
         arr = DisplayCheckSum(argv[1])

    except ValueError:
        print("Invalid data type of input")

    except Exception:
        print("Error : Invalid input")


def DirectoryWatcher(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    if exists:
        for dirName, subDirs, fileList in os.walk(path):
            print("Current folder is:", dirName)
            for subf in subDirs:
                print("Sub Floder name",subf)
            for fileName in fileList:
              #  print("File name:", fileName)
              print('')
    else:
      print("Invalid number of arguments dir")


if __name__ == "__main__":
    main();



