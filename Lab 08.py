# Write a python program to implement a stack class that has the following functions
# *push item
# *pop item
# *print the items in the stack
# *size of stack
# *the top item in the stack
# *check if the stack is empty


class Stack:
    def __init__(self):
        self.stack = []
# pushing the item
    def pushitem(self,item_name):
        self.stack.append(item_name)
        print(self.stack)
# finding the length
    def length(self):
        print(len(self.stack))
# removing the item
    def popitems(self):
        self.stack.pop()
        print (self.stack)
#check if it is empty
    def check(self):
        if len(self.stack)==0:
            print("Empty")
        else:
            print("Not empty")
# The top item
    def item_name(self):
        print(self.stack[len(self.stack)-1])
obj1=Stack()
# obj1.pushitem('paint')
# obj1.pushitem('Brush')
# obj1.length()
# obj1.popitems()
# obj1.check()
# obj1.item_name()
while True:
    option = int(input("Enter your option:").strip())

    if option == 1:
        obj1.pushitem(input("Enter the items to be added"))
    elif option == 2:
        obj1.length()
    elif option == 3:
        obj1.popitems(int(input("Enter the items to be removed")))
    elif option == 4:
        obj1.check()
    elif option == 5:
        obj1.item_name()
        exit()
    else:
        print("invalid choice")
    






        
        