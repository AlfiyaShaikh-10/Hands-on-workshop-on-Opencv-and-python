'''
To delete a file, you must import the OS module, and run its os.remove() function:
'''

import os

#Deleting a file

os.remove("demofile.txt")

#Checking wheather the file exists in directory or not

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")



