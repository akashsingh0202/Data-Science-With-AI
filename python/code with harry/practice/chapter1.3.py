import os
# specify the directory you want to list
directory_path='/'
#list all files and directories in the specified path
content=os.listdir(directory_path)
#print each files and directory name
for item in content: 
 print(item)