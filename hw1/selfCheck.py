import sys
import ntpath
from zipfile import ZipFile
from tarfile import TarFile

def main():
    # check arguments
    if len(sys.argv) != 2:
        sys.exit("Error: You should provide 1 argument which is the path to your zip/tar file (" + str(len(sys.argv) - 1) + " provided)")
        return 0
    
    # check valid path name
    pathName = sys.argv[1]
    try:
        f = open(pathName)
    except IOError:
        sys.exit("Error: File \"" + pathName + "\" does not exist.")

    # check zip or tar
    fileName = ntpath.basename(pathName)
    isZip, isTar = False, False
    if fileName[-4:].lower() == ".zip": isZip = True
    if fileName[-4:].lower() == ".tar": isTar = True
    if not (isZip or isTar):
        sys.exit("Error: Invalid file format (only .zip/.tar files accepted)")

    # check zip/tar file name
    if fileName[0:4] != "hw1_":
        sys.exit("Error: \"" + fileName + "\" is not a valid name.")
    studentID = fileName[4:-4]

    # define correct file structure here
    fileListRef = ["p1/p1a_" + studentID + ".py", 
                   "p1/p1b_" + studentID + ".py", 
                   "p1/tools.py",
                   "p2/p2a_" + studentID + ".py", 
                   "p2/p2b_" + studentID + ".py", 
                   "report_" + studentID + ".pdf"]

    # zip
    if isZip:
        Zip = ZipFile(pathName)
        fileList = Zip.namelist()
        fileError = False

        for f in fileListRef:
            if f not in fileList:
                fileError = True; print("Error: " + f + " missing!")
        
        if fileError: sys.exit()
        else:
            print("Passed! Your student ID is " + studentID + ".")       

    # tar
    if isTar:
        Tar = TarFile(pathName)
        fileList = Tar.getnames()
        fileError = False

        for f in fileListRef:
            if f not in fileList:
                fileError = True; print("Error: " + f + " missing!")
        
        if fileError: sys.exit()
        else:
            print("Passed! Your student ID is " + studentID + ".") 
  
if __name__== "__main__":
    main()