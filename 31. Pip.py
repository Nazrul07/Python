"""
What is PIP?

-> PIP is a package manager for Python packages, or modules if you like.
"""


"""
What is a Package?

-> A package contains all the files you need for a module.
-> Modules are Python code libraries you can include in your project.
"""


"""
Check if PIP is Installed

-> pip --version

If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/
"""


"""
Download a Package

Download a package named "camelcase"
-> pip install camelcase

Wow you have downloaded and installed your first package!
"""


# Using a Package   -> Once the package is installed, it is ready to use.
import camelcase as cc
c = cc.CamelCase()

txt = "hello world...!"
print(c.hump(txt))  # This method capitalizes the first letter of each word.


"""
Remove a Package

-> pip uninstall camelcase

Uninstalling camelcase-02.1:
  Would remove:
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase-0.2-py3.6.egg-info
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase\*
Proceed (y/n)?

Press y and the package will be removed.

"""




"""
List Packages

-> pip list

List installed packages on my computer only:

Package   Version
--------- -------
camelcase 0.2
pip       25.3
"""