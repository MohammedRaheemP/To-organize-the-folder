import os
import shutil

path='/home/dell/Documents/python_tools/organize_folder/'

names=os.listdir(path)

folder_name=['Cat','Dog']

for x in range(2):
   if not os.path.exists(path+folder_name[x]):                    #to avoid overide the folder
      os.makedirs(path+folder_name[x])

for files in names:
   if 'cat.' in files and not os.path.exists(path+'Cat/'+files):
      shutil.move(path+files,path+'Cat/'+files)
   if 'dog.' in files and not os.path.exists(path+'Dog/'+files):
      shutil.move(path+files,path+'Dog/'+files)









