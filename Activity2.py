# employee in and out. Write a program to create a class with the name employee and create a constructor and destructor and then write a function to create an object for that class and delete the object make sure you call the function to get everything implimented
class employee():
    def __init__(self):
        print("Emloyee created")
    def __del__(self):
        print("Destructor called")
def create_obj():
    print("Making object")
    obj = employee()
    print("Function end")
    return obj 
print("Calling create_obj function")
obj = create_obj()
print("Programming")