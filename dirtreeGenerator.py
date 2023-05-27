import os

# Place this in the preamble of your Latex project
# \usepackage{dirtree}

# E.g. C:/Users/user/Desktop/Folder/ on windows or /home/user/Desktop/Folder/ on linux.
dir = 'C:/Users/alber/OneDrive - Aalborg Universitet/GitHub/LarsVRKlo/'

# Link to the Github e.g. https://github.com/UnknownDK/LaTeX-Dirtree-Generator/
gitlink = "https://github.com/simo389b/LarsVRKlo/"

# Name of branch
branch = "master"

# List of folders to include in the dirtree.
whitelist = ['Absorption']

# List of folders and file extensions to ignore in the dirtree.
ignorelist = ['txt']

def dirtreeGenerate(startpath : str, whitelist : list, ignorelist : list):
    """dirtreeGenerate generates a directory tree for latex using the dirtree package.

    Parameters
    ----------
    startpath : string
        Directory to start the dirtree from.
    whitelist : list
        List of folders to include in the dirtree.
    ignorelist : list
        List of folders and file extensions to ignore in the dirtree.
    """
    with open("dirtree.tex", "w") as open_file:
        open_file.write("\dirtree{% \n") # start dirtree
        for dirpath, dirnames, filenames in os.walk(startpath):
            dirpath = dirpath.replace("\\", "/").replace("//", "/").replace("_", "\_")  # replace common errors with latex
            dirpath = dirpath.replace(startpath, '')                                    # remove startpath from path

            if dirpath.split("/")[0] not in whitelist and len(whitelist) != 0:          # if the last folder in the path is not in the whitelist
                continue                                                                # skip the folder

            for element in  dirpath.split("/"):                                         # if any of the folders in the path is in the ignorelist
                if element in ignorelist:                                               
                    continue                                                            # skip the folder

            directory   = dirpath.split("/")[-1]                                        # get directory name            
            indentation = dirpath.count("/") + 1                                        # calculate indentation for directory

            # write directory to dirtree
            open_file.write("." + str(indentation) + " \href{" + gitlink + "tree/" + branch + "/" + dirpath + "/}{" + directory + "/}.\n")
            for files in filenames:
                print(files.split(".")[-1])
                if files.split(".")[-1] in ignorelist:
                    continue
                # write files to dirtree
                open_file.write("." + str(indentation + 1) + " \href{" + gitlink + "blob/" + branch + "/" + dirpath + "/" + files + "}{" + files + "}.\n")

        open_file.write("}")    # end dirtree

dirtreeGenerate(dir, whitelist, ignorelist)