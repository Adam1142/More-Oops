# Write a program to create a class IOStrings which consists of a constructor that gives our default value next up create a method that gives a string as an input from the user create another method that will print the string in thne uppercase next up create an object to get everything 
class IOString():
    def __init__(self):
        self.str1 = ""
    def get_String(self):
        self.str1 = input("Enter a string: ")
    def print_String(self):
        print("result is ",self.str1.upper())
str1 = IOString()
str1.get_String()
str1.print_String()
