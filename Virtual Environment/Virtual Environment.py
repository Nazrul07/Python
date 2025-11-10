"""
What is a Virtual Environment?

-> A virtual environment in Python is an isolated environment on our computer, where we can run and test our Python projects.
-> It allows us to manage project-specific dependencies without interfering with other projects or the original Python installation.

"""



"""
Think of a virtual environment as a separate container for each Python project. Each container:

-> Has its own set of installed packages
-> Has its own Python interpreter
-> Is isolated from other virtual environments
-> Can have different versions of the same package

"""



"""
Using virtual environments is important because:

-> It prevents package version conflicts between projects
-> Makes projects more portable and reproducible
-> Keeps our system Python installation clean
-> Allows testing with different Python versions

"""



"""
# Creating a Virtual Environment

-> Python has the built-in venv module for creating virtual environments.
-> To create a virtual environment on a computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command:
D:\Python\Virtual Environment>python -m venv myfirstproject


This will set up a virtual environment, and create a folder named "myfirstproject" with subfolders and files, like this:

The file/folder structure will look like this:
myfirstproject
  Include
  Lib
  Scripts
  .gitignore
  pyvenv.cfg


"""




"""
Activate Virtual Environment

To use the virtual environment, you have to activate it with this command:
D:\Python\Virtual Environment>myfirstproject\Scripts\activate

After activation, your prompt will change to show that you are now working in the active environment:
(myfirstproject) D:\Python\Virtual Environment>

"""




"""
Install Packages

Once your virtual environment is activated, you can install packages in it, using pip.
We will install a package called 'cowsay':

Install 'cowsay' in the virtual environment:
(myfirstproject) D:\Python\Virtual Environment>pip install cowsay


Result

Collecting cowsay
  Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
Downloading cowsay-6.1-py3-none-any.whl (25 kB)
Installing collected packages: cowsay
Successfully installed cowsay-6.1

[notice] A new release of pip is available: 25.2 -> 25.3
[notice] To update, run: python.exe -m pip install --upgrade pip


Now that the 'cowsay' module is installed in your virtual environment, lets use it to display a talking cow.

"""




"""
Execute

Execute test.py in the virtual environment:
(myfirstproject) D:\Python\Virtual Environment>python test.py

"""




"""
Output

  _________________
| Good Mooooorning! |
  =================
                 \
                  \
                    ^__^
                    (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||


"""




"""
Deactivate Virtual Environment

Use this command:
(myfirstproject) D:\Python\Virtual Environment>deactivate

"""




"""
Result

D:\Python\Virtual Environment>

"""



"""
Execute test.py outside of the virtual environment:

$ source "D:/Python/Virtual Environment/myfirstproject/Scripts/activate"
bash: sed: command not found
bash: uname: command not found
(myfirstproject) 
Nazrul@TuringPoint MINGW64 /d/Python/Virtual Environment
$ "D:/Python/Virtual Environment/myfirstproject/Scripts/python.exe" "d:/Python/Virtual Environment/test.py"
bash: sed: command not found

"""




"""
Delete Virtual Environment

Either directly in the file system, or use the command line interface like this:
C:\Users\Your Name> rmdir /s /q myfirstproject

"""