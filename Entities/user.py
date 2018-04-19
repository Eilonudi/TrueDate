from TrueDate.Utilities.settings import *

class person:
    '''Entitiy class for a person.
    Each person is conatined by a single user in a one to one relationship'''

    def __init__(self, name : str, city : str, age : int, bio : str, drt : RelationshipType, favMusics : list, favMovies : list, favBooks):
        self.name = name
        self.city = city
        self.age  = age
        self.bio  = bio
        self.drt  = drt
        self.favMusics = favMusics
        self.favMovies = favMovies
        self.favBooks  = favBooks

class user:
    '''Entitiy class for a user.
    Each user holds a person in a one-to-one relationship'''

    def __init__(self, person, loginDate):
        self.loginDate = loginDate
        self.isEnabled  = True
        self.isOnlinee = True #consider if usefull
        self.rating    = 0
        self.uniqueId = hash(person.name + person.city + person + self.loginDate)
        self.person = person

