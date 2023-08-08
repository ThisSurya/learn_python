def myfunc():
    print('this is a module inside mymodule.py')

if __name__ == "__main__":
    print("mymodule.py is running")
else:
    print("mymodule.py is imported")