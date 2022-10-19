class Animal:
    """A animal structure"""

    def __init__(self, name, color, voice):
        self.name = name
        self.color = color
        self.voice = voice

def says_voice(animal):
    print(animal.voice)

cow = Animal(name="Burka", color="black", voice="myyy")
cat = Animal(name="Kuzia", color="white", voice="miau")
dog = Animal(name='Proton', color="red", voice="gav")

animal_list = (cow, cat, dog)

for i in animal_list:
    print(f"{i.name} is {i.color}. It sais {i.voice}")