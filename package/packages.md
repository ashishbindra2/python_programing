# PACKAGES

## Functions:
- A Group of repeatedly required lines.
- Code reusability

## Modules:
- Python files
- A group of functions, variables, classes saved to a file.

## Packages:
- A collection of related modules into a folder 
- A collection of related modules into a single unit.
- It is an encapsulation mechanism to group related modules into a single unit.
- package is nothing but folder or directory
- * Any folder or directory contains __init__.py file, is considered as a Python package. 
  * This file can be empty.
- A package can contain sub packages also.

***Note:***
- From pythin 3.3  version onwords, it is not mandatory `__init__.py` (optional)
- but Good to use it

### The main advantages of package are:

1. We can resolve naming conflicts 
2. We can identify our components uniquely 
3. It improves the modularity of the application
4. It improves readability and maintainability of the application

Get tree directory
- `tree /f`
     -  Eg 1: D:\Python_cla> 
            |-test.py 
            |-pack1 
              |-module1.py 
              |-__init__.py

## Importance of __init__.py:
  At the time of using a package, If we want to perform any initialization activities ***automatically***, then we have to go for __init__.py
  
### Need of installing a package