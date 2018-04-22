
loc_map = {}


class User(object):
    def __init__(self, name):
        self.list = []  #create a list for the object
        loc_map[self] = self.list   #in the map, create a key for the object, and the value is the list
        self.name = name  #this the the var name given to each object when declaring the class
    def add_loc(self, location):
        loc_map[self].append(location)  #add the given location to the object's list in the map
    def return_loc(self):
        print(loc_map[self][-1])  #return the 1 to last (i.e. the last) element of the objects' list in the map
    def test(self):
        print(self.name)

rohan = User('Rohan Kulkarni')
rohan.add_loc('abbott poc')
rohan.add_loc('car')
rohan.add_loc('home')
rohan.add_loc('bed')


neha = User('Neha Kulkarni')
neha.add_loc('abbott poc')
neha.add_loc('car')
neha.add_loc('home')

rohan.return_loc()
rohan.test()
