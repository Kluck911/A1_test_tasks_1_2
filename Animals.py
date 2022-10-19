class Animal:
    """A animal structure"""

    def __init__(self, name, color, voice):
        self.name = name
        self.color = color
        self.voice = voice

def says_voice(animal):
    print(animal.voice)