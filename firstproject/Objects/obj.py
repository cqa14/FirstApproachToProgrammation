
class Object:
   
    def __init__(self, name, size):
        self.name = name
        self.size = size

        print(name, "/", size)

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def set_name(self, name):
        self.name = name
        print(name)
    
    def set_size(self, size):
        self.size = size
        print(size)

    def get_another_name(self, target_object):
        print(target_object.get_name(),"/", target_object.get_size())

class Cube(Object):

    def __init__(self, name, size, is_cube):
        self.is_cube = is_cube
        super().__init__(name, size)
    
    def is_cubic(self):
        if bool(self.is_cube) == True:
            print("V")
        else:
            print("F")