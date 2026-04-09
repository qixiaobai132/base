



class Teacher:
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
    

t = Teacher("John", 30)

print(t.__dict__)