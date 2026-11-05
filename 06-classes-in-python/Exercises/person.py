class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def __str__(self):
        return self._name + " (" + self._gender + ") aged " + str(self._age)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.capitalize()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = int(age)

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender