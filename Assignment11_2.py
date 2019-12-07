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

def main():
    print("---------------Application name--------------", argv[0])
    print("Accept directory name and write names of duplicate files from that directory into log file named as Log.txt.")

    if (len(argv) < 1):
        print("Invalid number of arguments")
        exit()

    if (argv[1] == '-h') or (argv[1] == '-H'):
        print("The script is used to travel specific directory")
        exit()

    if (argv[1] == '-u') or (argv[1] == '-U'):
        print("usage : Application name absolute_path_of_directory")
        exit()

    try:
        arr = {}
        arr = findDup(argv[1])
        printResults(arr)

    except ValueError:
        print("Invalid data type of input")

    except Exception:
        print("Error : Invalid input")


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
    f = open("Log.txt", "w")
    if len(results) > 0:
        print("Duplicates found")
        print("The following files are duplicate.")
        for result in results:
            for subresult in result:
                print("\t\t%s"%subresult)
                f.write(subresult)
                f.close()
    else:
        print("No duplicate files found")


if __name__ == "__main__":
    main()