# we need to import the operating system for python to be able to interact with the OS
import os
import winreg

# define a function that recalls which user account the file was found belonging to
def sid2user(sid):
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" + "\\" + sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
    except:
        return sid
    
# define a function that locates the recycle bin directory
def returnDir():
    dirs=['C:\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

# define a function that loops the files found in the directory 
def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        file = os.listdir(recycleDir + sid)
        user = sid2user(sid)
        print('\n[*] Listing Files for User: ' + str(user))
        for file in file:
            print('[+] Found File: ' + str(file))

def main():
    recycleDir = returnDir()
    findRecycled(recycleDir)

if __name__ == '__main__':
    main()