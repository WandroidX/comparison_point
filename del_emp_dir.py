import os

os.chdir("c:\\")

for folder, subfolders, files in os.walk("c:\\users\\wandroid\\downloads"):
    if folder=="c:\\users\\wandroid\\downloads":
        mode="w"
    else:
        mode="a"

    doc=open("c:\\users\\wandroid\\desktop\\folders_sorted.txt", mode)
    for subs in subfolders:
        subcarp=""+subs+"\n"


    for file in files:
        archivos=""+file+"\n"

    doc.write("the current folder is: %s\nthe subfolders inside are: \n%sthe files are: \n%s\n"%(folder,subcarp,archivos))
    doc.close()
