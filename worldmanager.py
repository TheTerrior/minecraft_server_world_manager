import os
import sys
import time
import shutil

curdir = os.curdir
worlds_folder = os.curdir + "/worlds"
backup_folder = os.curdir + "/backup"

# generate a unique string for the current time
def gen_time_str() -> str:
    return str(int(time.time() * 100))

# backup current world to backup folder
def backup_world():
    shutil.copytree(curdir + "/world", backup_folder + "/" + gen_time_str(), symlinks = True)

# saves the current world into the given world_name's folder
def save(world_name: str):
    if not os.path.isdir(curdir + "/world"): #if current world doesn't exist
        return
    if os.path.isdir(worlds_folder + "/" + world_name): #if target world exists
        shutil.rmtree(worlds_folder + "/" + world_name) #first remove the saved world of this name
    shutil.copytree(curdir + "/world", worlds_folder + "/" + world_name, symlinks = True) # then save the current world into that folder

# saves the current world into the backup folder and overwrites it with the given world
def retrieve(world_name: str):
    if not os.path.isdir(curdir + "/world") or not os.path.isdir(worlds_folder + "/" + world_name): #if either world doesn't exist
        return
    backup_world() #first backup the current world
    shutil.rmtree(curdir + "/world") #remove the current world
    shutil.copytree(worlds_folder + "/" + world_name, curdir + "/world", symlinks = True) #copy the saved world into the current world

# given a directory and a base, returns the highest folder other than the base
def folder_name(dir: str, base: str) -> set:
    if len(dir) <= len(base): #filter out some cases
        return None
    if (loc := dir[len(base) + 1:].find('/')) == -1: #loc must be added back to length of base and such
        return dir[len(base):]
    else:
        return dir[len(base):loc + len(base) + 1]

# will return a set of all the folders in a given directory
def folders_in(dir: str) -> set:
    folders = set()
    for (root, _, _) in os.walk(dir):
        if (res := folder_name(root, dir)) == None:
            continue
        else:
            folders.add(res)
    return folders

def main(args: list):
    if type(args) != list or len(args) != 3: #want file, and two arguments
        print("Incorrect number of arguments.")
        return
    if args[1] not in ["save", "retrieve"]:
        print("Must input one of the following commands: {save, retrieve}")
        return
    match args[1]:
        case "save":
            save(args[2])
        case "retrieve":
            retrieve(args[2])
        case _:
            return
    return

main(sys.argv)

