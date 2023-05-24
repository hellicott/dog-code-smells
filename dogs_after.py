from datetime import date
from dateutil.relativedelta import relativedelta

class Owner:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def get_age(self):
        age = relativedelta(date.today(), self.dob)
        return age

class Dog:
    def __init__(self, name, breed, dob, owner):
        self.name = name
        self.breed = breed
        self.dob = dob
        self.owner = owner

    def calculate_age(self, dob):
        age = relativedelta(date.today(), dob)
        return age

    def get_dog_age(self):
        return self.calculate_age(self.dob)
    
    def get_dog_age_in_human_years(self):
        return (self.get_dog_age() * 7).years
    
    def compare_to_owner_age(self):
        dog_human_age = self.get_dog_age_in_human_years()
        owner_age = self.owner.get_age().years
        
        if dog_human_age > owner_age:
            print(f"{self.name}({dog_human_age}) is older than {self.owner.first_name}({owner_age})")
        elif owner_age > dog_human_age:
            print(f"{self.owner.first_name}({owner_age}) is older than {self.name}({dog_human_age})")
        else:
            print(f"{self.name} and {self.owner.first_name} are both {owner_age}")


human = Owner("Hannah", "Ellicott", date.fromisoformat('1998-11-10'))  
doggo = Dog("Casper", "Rescue", date.fromisoformat('2016-08-15'), human)
doggo.compare_to_owner_age()

iggy = Dog("Igloo", "Rescue", date.fromisoformat('2020-03-17'), human)
iggy.compare_to_owner_age()


