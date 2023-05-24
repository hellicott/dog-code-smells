from datetime import date
from dateutil.relativedelta import relativedelta

class Dog:
    def __init__(self, name, breed, dob, owner_first_name, owner_last_name, owner_dob):
        self.name = name
        self.breed = breed
        self.dob = dob
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.owner_dob = owner_dob

    def get_dog_age(self):
        # calculate time since dob
        age = relativedelta(date.today(), self.dob)
        return age
    
    def get_owner_age(self):
        # calculate time since dob
        age = relativedelta(date.today(), self.owner_dob)
        return age


doggo = Dog("Casper", "Rescue", date.fromisoformat('2016-08-15'), "Hannah", "Ellicott", date.fromisoformat('1998-11-10'))
print(f"{doggo.name}'s age is {doggo.get_dog_age()}")
print(f"{doggo.owner_first_name}'s age is {doggo.get_owner_age()}")

