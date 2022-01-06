import shutil, os

os.chdir("c:\\")

for dirs in os.listdir():
    try:
        os.rmdir(dirs)
        print(os.path.abspath(dirs)+ " has been deleted")
    except OSError:
        print("the dir [%s¨] isnt empty"%(os.path.abspath(dirs)))
