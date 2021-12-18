# STACKS

class Stack:
    # Last In First Out

    def __init__(self):
        self._data = []
    
    
#     Checks if the stack is empty 
    def is_empty(self):
        return len(self._data) == 0
            
# Returns the length of the stack
    def length(self):
        if len(self._data) == 0:
            print("Empty Stack")
        return len(self._data)

# Return top element
    def topEl(self):
        if self.is_empty():
            print("Cannot return as Stack is Empty")
        else:
            return self._data[-1]
            

    # Add Element
    def addEl(self, element):
        return self._data.append(element)

    # Remove Element

    def removeEl(self):
        #If stack is empty
        if self.is_empty():
            raise TypeError("Bhai stack empty hai")
        else:
            return self._data.remove(self._data[-1])

        
#         This is basically not a stack feature but still to see data I have included this function which return the stack data
    def seeData(self):
       return (self._data)


s = Stack()
s.addEl(34)
s.length()
s.addEl(56)
s.addEl(78)
print(s.topEl())
print(s.length())
print(s.seeData())











