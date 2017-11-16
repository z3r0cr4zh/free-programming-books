import os

path = "/home/username/Virus/Virus to scan for comparson/"
path2 = "/home/username/Virus/Virus to scan for comparson"
for filename in os.listdir(path2):
  
    for filenames in os.listdir(path2):
 
        with open(path + filename, 'r') as file1:
             with open(path + filenames, 'r') as file2:
                  fname = set(file1).intersection(file2)
                  print fname
same.discard('\n')

with open('/home/z3r0cr4zh/Desktop/some_output_file.txt', 'a+') as file_out:
    for line in same:
        #file_out.write(line)
        print line
