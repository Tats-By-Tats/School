from pathlib import Path
import os

file_path = Path (r"C:\Users\USER\Downloads\IPT_Python_Practice") / "missing.txt"

if file_path.exists():

    print ("FILE PERMISSION REPORT")
    print ("--------------------------------------------------------------")

    print ("Readable:", os.access(file_path, os.R_OK))
    print ("Writable:", os.access(file_path, os.W_OK))
    print ("Executable:", os.access(file_path, os.X_OK))

else:
    print ("File not found.")