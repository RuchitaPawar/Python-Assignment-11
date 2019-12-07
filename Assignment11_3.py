import hashlib
import os
from sys import argv


def DeleteFile(dict1):
    results = list(filter(lambda x:len(x) > 1,dict1.values()))
    icnt =0
    f = open("Log.txt", "w")
    if len(results) > 0 :
        for result in results :
            for subresult in result :
                icnt +=1
                if icnt >=2:
                    print("Deleted file name:",subresult)
                    f.write(subresult)
                    f.close()
                    os.remove(subresult)
            icnt =0
    else:
        print("No duplicate files found")

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def findDup(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    dups = {}
    if exists:
        for dirName, subDirs, fileList in os.walk(path):
            print("Current folder is:", dirName)
            for fileName in fileList:
                path = os.path.join(dirName, fileName)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

            return dups;
    else:
        print("Invalid path")

def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates found")
        print("The following files are duplicate : ")
        for res in results:
            for subresult in res:
                print("\t\t%s"%subresult)
    else:
        print("No duplicate files found")

def main():
    print("---------------Application name--------------", argv[0])
    print("accept directory name and delete all duplicate files from that directory")

    if (len(argv) < 1):
        print("Invalid number of arguments")
        exit()

    if (argv[1] == '-h') or (argv[1] == '-H'):
        print("The script is used to travel specific directory and delete duplicate files")
        exit()

    if (argv[1] == '-u') or (argv[1] == '-U'):
        print("usage : Application name absolute_path_of_directory")
        exit()

    try:
        arr = {}
        arr = findDup(argv[1])
        DeleteFile(arr)

    except ValueError:
        print("Error invalid datatype of input")

    except Exception:
        print("Error : Invalid input")



if __name__ == "__main__":
    main()



