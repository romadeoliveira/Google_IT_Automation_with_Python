#Pergunta 1
#The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared  by the 'comments' variable, #and returns the size of the new file. Fill in the gaps to create a script called "program.py".

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename,'w') as file:
    filesize = file.write(comments)
  return(filesize)

print(create_python_script("program.py"))

#Pergunta 2
#The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list #of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename,'w') as file:
    file.write("")

  # Return the list of files in the new directory
  os.chdir('..')
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))

#Pergunta 5
#The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias #that means "go up to the parent directory". Fill in the gaps to complete this function.

import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.abspath('..')

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())
