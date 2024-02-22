class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def description(self):
        return self.name + ' ; ' + self.breed


class ServiceDog(Dog):
    def __init__(self, name, breed, service_area):
        super().__init__(name, breed)
        self.service_area = service_area

    # Overriding 'description' method from the parent class / superclass / baseclass
    def description(self):
        return super().description() + ' ; ' + self.service_area

apchi = Dog('Apchi', 'Mixed Breed')
print(apchi.description())

jimmy = ServiceDog('Jimmy', 'German Sheppard', 'Bomb Detection')
print(jimmy.description())
