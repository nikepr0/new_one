#f = open("demofile.txt", "rt")

#--------------------------

#f = open("demofile.txt")
#print(f.read()) 

#f = open("D:\\myfiles\welcome.txt")
#print(f.read())

'''with open("demofile.txt") as f:
  print(f.read()) 

f = open("demofile.txt")
print(f.readline())
f.close() 

with open("demofile.txt") as f:
  print(f.read(5)) 

with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline()) 
  
with open("demofile.txt") as f:
  for x in f:
    print(x) '''
    
#--------------------------------
'''with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read()) 
  
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read()) 
  
f = open("myfile.txt", "x")'''


#-----------------------------------------
'''Remove the file "demofile.txt":
import os
os.remove("demofile.txt") 

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
Remove the folder "myfolder":
import os
os.rmdir("myfolder") '''