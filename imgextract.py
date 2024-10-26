
from os import walk, path, listdir

"""
Function to list files in a directory and add
them to lists or dictionaries or something
"""

testpath = "/home/jules/Pictures/2024-10-06/"
print(listdir(testpath))

# print(walk(testpath))


"""
Function to read date taken from image EXIF data, and store
this so it can be retrieved with the corresponding image.
"""

"""
Create a folder / folders named with the format YYYY-MM-DD - Job Code
(Get user input for job code(s)) (use existing folder if already there)
"""

"""
Copy RAW files directly into the existing or newly created folder.
Copy JPEGs into a specific JPEG subfolder
"""

# if __name__ == '__main__':
# 	print("Hello World")