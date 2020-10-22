import glob, os
import subprocess

def getAllVideos(extension):
    print(os.getcwd())
    files = []
    for file in glob.glob("*." + extension):
        files.append(file)
    return files      

try:
    extension_type = input("Enter extension type: ")
    aspect_ratio = input("Enter aspect ratio (A:B): ")
    allvids = getAllVideos(extension_type)
    for i in range(0, len(allvids)):
        print("[", i+1, "] ", allvids[i], sep='')
        episode = allvids[i][:-4] + "_REWORKED." + extension_type
        print(episode)
        subprocess.call(["ffmpeg", "-i", allvids[i], "-aspect", aspect_ratio, "-c", "copy", episode])
except:
    print("Couldn't find")