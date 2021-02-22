import glob
import os
cwd = os.getcwd()
textfiles = []
dir1 = os.path.join(cwd, "*.png")
for img in glob.glob(dir1):
    textfiles.append(img)
    print(textfiles)
